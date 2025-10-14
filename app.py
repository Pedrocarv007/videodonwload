import os
import re
import shutil
from flask import Flask, render_template, request, send_file, jsonify, flash, redirect, url_for
from pytubefix import YouTube
from pytubefix.exceptions import VideoUnavailable, RegexMatchError
import tempfile
import threading
from urllib.parse import urlparse
from datetime import datetime
from config import config

# Initialize Flask app
app = Flask(__name__)

# Load configuration
config_name = os.environ.get('FLASK_CONFIG', 'default')
app.config.from_object(config[config_name])

# Create downloads directory if it doesn't exist
DOWNLOADS_DIR = app.config['DOWNLOADS_DIR']
if not os.path.exists(DOWNLOADS_DIR):
    os.makedirs(DOWNLOADS_DIR)

# Store download progress
download_progress = {}

def clean_downloads_folder():
    """Clean all files from downloads folder"""
    try:
        for filename in os.listdir(DOWNLOADS_DIR):
            file_path = os.path.join(DOWNLOADS_DIR, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f'Erro ao deletar {file_path}: {e}')
    except Exception as e:
        print(f'Erro ao limpar pasta de downloads: {e}')

def progress_function(stream, chunk, bytes_remaining):
    """Callback function to track download progress"""
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded / total_size) * 100
    
    # Store progress for the current download
    download_id = getattr(stream, 'download_id', 'default')
    download_progress[download_id] = {
        'percentage': round(percentage, 2),
        'downloaded': bytes_downloaded,
        'total': total_size
    }

def is_valid_youtube_url(url):
    """Validate if the URL is a valid YouTube URL"""
    youtube_regex = re.compile(
        r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/'
        r'(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})'
    )
    return youtube_regex.match(url) is not None

def sanitize_filename(filename):
    """Remove invalid characters from filename"""
    # Remove invalid characters for Windows filenames
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    return filename[:100]  # Limit filename length

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download', methods=['GET', 'POST'])
def download_video():
    if request.method == 'POST':
        try:
            url = request.form.get('url', '').strip()
            quality = request.form.get('quality', 'highest')
            
            if not url:
                flash('Por favor, insira uma URL do YouTube.', 'error')
                return redirect(url_for('home'))
            
            if not is_valid_youtube_url(url):
                flash('URL inválida. Por favor, insira uma URL válida do YouTube.', 'error')
                return redirect(url_for('home'))
            
            # Limpar pasta de downloads antes do novo download
            clean_downloads_folder()
            
            # Create YouTube object
            yt = YouTube(url, on_progress_callback=progress_function)
            
            # Set download ID for progress tracking
            download_id = str(datetime.now().timestamp())
            
            # Get video info
            video_title = sanitize_filename(yt.title)
            video_length = yt.length
            
            # Select stream based on quality preference
            if quality == 'audio':
                stream = yt.streams.filter(only_audio=True).first()
                file_extension = '.mp3'
            elif quality == 'lowest':
                stream = yt.streams.filter(progressive=True).order_by('resolution').first()
                file_extension = '.mp4'
            else:  # highest quality
                stream = yt.streams.get_highest_resolution()
                file_extension = '.mp4'
            
            if not stream:
                flash('Não foi possível encontrar um stream disponível para este vídeo.', 'error')
                return redirect(url_for('home'))
            
            # Set download ID for progress tracking
            stream.download_id = download_id
            
            # Create filename
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"{video_title}_{timestamp}{file_extension}"
            filepath = os.path.join(DOWNLOADS_DIR, filename)
            
            # Download the video
            stream.download(output_path=DOWNLOADS_DIR, filename=filename)
            
            # Clean up progress tracking
            if download_id in download_progress:
                del download_progress[download_id]
            
            flash(f'Vídeo "{yt.title}" baixado com sucesso!', 'success')
            
            # Return file for download
            return send_file(
                filepath,
                as_attachment=True,
                download_name=filename,
                mimetype='application/octet-stream'
            )
            
        except VideoUnavailable:
            flash('Vídeo não disponível. Verifique se o vídeo existe e é público.', 'error')
        except RegexMatchError:
            flash('Erro ao processar a URL. Verifique se a URL está correta.', 'error')
        except Exception as e:
            flash(f'Erro inesperado: {str(e)}', 'error')
        
        return redirect(url_for('home'))
    
    return redirect(url_for('home'))

@app.route('/video_info')
def get_video_info():
    """Get video information without downloading"""
    url = request.args.get('url', '').strip()
    
    if not url or not is_valid_youtube_url(url):
        return jsonify({'error': 'URL inválida'}), 400
    
    try:
        yt = YouTube(url)
        
        # Get available streams
        video_streams = []
        for stream in yt.streams.filter(progressive=True):
            video_streams.append({
                'resolution': stream.resolution,
                'fps': stream.fps,
                'filesize': stream.filesize
            })
        
        return jsonify({
            'title': yt.title,
            'length': yt.length,
            'views': yt.views,
            'author': yt.author,
            'thumbnail': yt.thumbnail_url,
            'streams': video_streams
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/progress/<download_id>')
def get_progress(download_id):
    """Get download progress"""
    progress = download_progress.get(download_id, {'percentage': 0})
    return jsonify(progress)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(
        debug=app.config['DEBUG'],
        host=app.config['HOST'],
        port=app.config['PORT']
    )
