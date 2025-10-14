import os
import re
import shutil
import logging
import traceback
from flask import Flask, render_template, request, send_file, jsonify, flash, redirect, url_for
from flask_cors import CORS
from pytubefix import YouTube
from pytubefix.exceptions import VideoUnavailable, RegexMatchError
from datetime import datetime

# Configuração de logs
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Initialize Flask app com configuração específica para IIS
app = Flask(__name__, static_url_path="/youtube/static", static_folder="static")
app.secret_key = os.environ.get('SECRET_KEY', 'youtube-downloader-secret-key-2024')

# Configuração CORS para IIS
CORS(app, 
     origins=["*"], 
     methods=["GET", "POST", "OPTIONS"],
     allow_headers=["Content-Type", "Authorization"],
     supports_credentials=True)

# Configurações específicas para IIS
HOST = '127.0.0.1'
PORT = 6001
DEBUG = True

# Diretório de downloads
DOWNLOADS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'downloads')

# Create downloads directory if it doesn't exist
def ensure_downloads_dir():
    """Garante que o diretório de downloads existe"""
    try:
        if not os.path.exists(DOWNLOADS_DIR):
            os.makedirs(DOWNLOADS_DIR)
            logger.info(f"Diretório de downloads criado: {DOWNLOADS_DIR}")
        return True
    except Exception as e:
        logger.error(f"Erro ao criar diretório de downloads: {e}")
        return False

def clean_downloads_folder():
    """Limpa todos os arquivos da pasta de downloads"""
    try:
        if os.path.exists(DOWNLOADS_DIR):
            for filename in os.listdir(DOWNLOADS_DIR):
                file_path = os.path.join(DOWNLOADS_DIR, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                        logger.info(f"Arquivo removido: {filename}")
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                        logger.info(f"Diretório removido: {filename}")
                except Exception as e:
                    logger.warning(f'Erro ao deletar {file_path}: {e}')
            logger.info("Limpeza da pasta de downloads concluída")
        return True
    except Exception as e:
        logger.error(f'Erro ao limpar pasta de downloads: {e}')
        return False

def is_valid_youtube_url(url):
    """Valida se a URL é uma URL válida do YouTube"""
    youtube_regex = re.compile(
        r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/'
        r'(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})'
    )
    return youtube_regex.match(url) is not None

def sanitize_filename(filename):
    """Remove caracteres inválidos do nome do arquivo"""
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    # Remove espaços duplos e limita tamanho
    filename = ' '.join(filename.split())[:100]
    return filename

@app.route('/')
def home():
    """Página principal"""
    try:
        logger.info("Acessando página principal")
        ensure_downloads_dir()
        return render_template('index.html')
    except Exception as e:
        logger.error(f"Erro na página principal: {e}")
        return f"Erro interno: {str(e)}", 500

@app.route('/test')
def test():
    """Rota de teste para verificar se a aplicação está funcionando"""
    return jsonify({
        'status': 'ok',
        'message': 'Aplicação funcionando',
        'timestamp': datetime.now().isoformat(),
        'host': HOST,
        'port': PORT,
        'downloads_dir': DOWNLOADS_DIR
    })

@app.route('/video_info', methods=['POST', 'OPTIONS'])
def get_video_info():
    """Obtém informações do vídeo via POST JSON"""
    # Handle CORS preflight
    if request.method == 'OPTIONS':
        return jsonify({'status': 'ok'})
    
    try:
        logger.info("=== REQUISIÇÃO DE INFORMAÇÕES DO VÍDEO ===")
        logger.info(f"Method: {request.method}")
        logger.info(f"Content-Type: {request.content_type}")
        
        # Obter dados JSON
        try:
            data = request.get_json(force=True)
            logger.info(f"JSON recebido: {data}")
        except Exception as e:
            logger.error(f"Erro ao parsear JSON: {e}")
            return jsonify({'error': 'Dados JSON inválidos'}), 400
        
        if not data or 'url' not in data:
            logger.warning("URL não fornecida na solicitação")
            return jsonify({'error': 'URL não fornecida'}), 400
        
        url = data['url'].strip()
        logger.info(f"URL a processar: {url}")
        
        # Validação da URL
        if not url or not is_valid_youtube_url(url):
            logger.warning(f"URL inválida: {url}")
            return jsonify({'error': 'URL do YouTube inválida'}), 400
        
        # Obtém informações do vídeo
        logger.info("Criando objeto YouTube...")
        yt = YouTube(url)
        
        logger.info("Obtendo informações do vídeo...")
        
        # Obter streams disponíveis para mostrar opções
        video_streams = []
        try:
            for stream in yt.streams.filter(progressive=True).order_by('resolution').desc():
                if stream.resolution:
                    video_streams.append({
                        'resolution': stream.resolution,
                        'fps': stream.fps or 'N/A',
                        'filesize_mb': round(stream.filesize / (1024*1024), 2) if stream.filesize else 'N/A'
                    })
        except:
            video_streams = []
        
        video_info = {
            'title': yt.title or 'Título não disponível',
            'author': yt.author or 'Autor não disponível',
            'length': yt.length or 0,
            'views': yt.views or 0,
            'thumbnail_url': yt.thumbnail_url or '',
            'description': (yt.description[:200] + '...') if yt.description and len(yt.description) > 200 else (yt.description or 'Descrição não disponível'),
            'streams': video_streams[:5]  # Mostra apenas os 5 primeiros
        }
        
        logger.info(f"Informações obtidas para: {video_info['title']}")
        return jsonify(video_info)
        
    except VideoUnavailable:
        logger.error("Vídeo não disponível")
        return jsonify({'error': 'Vídeo não disponível. Verifique se o vídeo existe e é público.'}), 400
    except RegexMatchError:
        logger.error("Erro no regex da URL")
        return jsonify({'error': 'Erro ao processar a URL. Verifique se a URL está correta.'}), 400
    except Exception as e:
        logger.error(f"Erro ao obter informações do vídeo: {e}")
        logger.error(traceback.format_exc())
        return jsonify({'error': f'Erro ao obter informações: {str(e)}'}), 500

@app.route('/download', methods=['POST'])
def download_video():
    """Baixa o vídeo"""
    try:
        logger.info("=== REQUISIÇÃO DE DOWNLOAD ===")
        logger.info(f"Method: {request.method}")
        logger.info(f"Form data: {dict(request.form)}")
        
        url = request.form.get('url', '').strip()
        quality = request.form.get('quality', 'high')
        
        logger.info(f"Download - URL: {url}, Qualidade: {quality}")
        
        if not url:
            logger.warning("URL não fornecida para download")
            return jsonify({'error': 'URL não fornecida'}), 400
        
        # Validação da URL
        if not is_valid_youtube_url(url):
            logger.warning(f"URL inválida para download: {url}")
            return jsonify({'error': 'URL do YouTube inválida'}), 400
        
        # Garante que o diretório existe
        if not ensure_downloads_dir():
            return jsonify({'error': 'Erro ao criar diretório de downloads'}), 500
        
        # Limpa a pasta de downloads
        clean_downloads_folder()
        
        # Cria objeto YouTube
        logger.info("Criando objeto YouTube para download...")
        yt = YouTube(url)
        
        # Sanitiza o nome do arquivo
        safe_title = sanitize_filename(yt.title)
        logger.info(f"Título sanitizado: {safe_title}")
        
        # Seleciona o stream baseado na qualidade
        stream = None
        filename = None
        
        if quality == 'audio':
            logger.info("Buscando stream de áudio...")
            stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
            filename = f"{safe_title}.mp3"
        elif quality == 'low':
            logger.info("Buscando stream de baixa qualidade...")
            stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').first()
            filename = f"{safe_title}_low.mp4"
        else:  # high quality
            logger.info("Buscando stream de alta qualidade...")
            stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            if not stream:
                # Fallback para qualquer stream progressivo
                stream = yt.streams.filter(progressive=True).first()
            filename = f"{safe_title}.mp4"
        
        if not stream:
            logger.error("Nenhum stream disponível para download")
            return jsonify({'error': 'Nenhum formato disponível para download'}), 400
        
        logger.info(f"Stream selecionado: {stream}")
        logger.info(f"Resolução: {stream.resolution}")
        logger.info(f"Tamanho: {stream.filesize} bytes")
        
        # Caminho completo do arquivo
        file_path = os.path.join(DOWNLOADS_DIR, filename)
        logger.info(f"Baixando para: {file_path}")
        
        # Faz o download
        stream.download(output_path=DOWNLOADS_DIR, filename=filename)
        
        # Verifica se o arquivo foi criado
        if not os.path.exists(file_path):
            logger.error(f"Arquivo não foi criado: {file_path}")
            return jsonify({'error': 'Erro ao criar arquivo'}), 500
        
        file_size = os.path.getsize(file_path)
        logger.info(f"Download concluído: {filename} ({file_size} bytes)")
        
        # Retorna o arquivo para download
        return send_file(
            file_path,
            as_attachment=True,
            download_name=filename,
            mimetype='application/octet-stream'
        )
        
    except VideoUnavailable:
        logger.error("Vídeo não disponível para download")
        return jsonify({'error': 'Vídeo não disponível. Verifique se o vídeo existe e é público.'}), 400
    except RegexMatchError:
        logger.error("Erro no regex da URL para download")
        return jsonify({'error': 'Erro ao processar a URL. Verifique se a URL está correta.'}), 400
    except Exception as e:
        logger.error(f"Erro no download: {e}")
        logger.error(traceback.format_exc())
        return jsonify({'error': f'Erro no download: {str(e)}'}), 500

@app.errorhandler(404)
def not_found_error(error):
    """Página de erro 404"""
    logger.warning(f"Página não encontrada: {request.url}")
    return jsonify({'error': 'Página não encontrada'}), 404

@app.errorhandler(500)
def internal_error(error):
    """Página de erro 500"""
    logger.error(f"Erro interno do servidor: {error}")
    return jsonify({'error': 'Erro interno do servidor'}), 500

@app.before_request
def log_request_info():
    """Log de todas as requisições"""
    logger.info(f">>> {request.method} {request.url}")

@app.after_request
def log_response_info(response):
    """Log de todas as respostas"""
    logger.info(f"<<< {response.status_code}")
    return response

if __name__ == '__main__':
    print("=" * 60)
    print("    YOUTUBE DOWNLOADER - VERSÃO IIS")
    print("=" * 60)
    print(f"Host: {HOST}")
    print(f"Port: {PORT}")
    print(f"Debug: {DEBUG}")
    print(f"Downloads Dir: {DOWNLOADS_DIR}")
    print(f"URL Local: http://{HOST}:{PORT}")
    print(f"URL Teste: http://{HOST}:{PORT}/test")
    print("=" * 60)
    
    logger.info("Iniciando aplicação YouTube Downloader para IIS")
    
    try:
        ensure_downloads_dir()
        app.run(
            host=HOST,
            port=PORT,
            debug=DEBUG,
            threaded=True
        )
    except Exception as e:
        logger.error(f"Erro ao iniciar aplicação: {e}")
        logger.error(traceback.format_exc())
        print(f"\n❌ ERRO: {e}")
        input("Pressione Enter para sair...")