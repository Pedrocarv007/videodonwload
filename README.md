# 🎥 YouTube Video Downloader

Um aplicativo web profissional para download de vídeos do YouTube, desenvolvido em Python com Flask. Interface moderna, responsiva e funcional para baixar vídeos diretamente para seu computador.

![YouTube Downloader](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Funcionalidades

- 🎬 **Preview de Vídeos**: Visualize informações do vídeo antes do download
- 📱 **Design Responsivo**: Interface moderna que funciona em desktop e mobile
- 🎯 **Múltiplas Qualidades**: Escolha entre máxima qualidade, qualidade baixa ou apenas áudio
- ⚡ **Download Direto**: Baixe arquivos diretamente para seu computador
- 🔒 **Validação de URLs**: Verificação automática de URLs do YouTube
- 📊 **Feedback Visual**: Mensagens de status e barras de progresso
- 🛡️ **Tratamento de Erros**: Sistema robusto de tratamento de erros
- 🎨 **Interface Intuitiva**: Design limpo e fácil de usar

## 🚀 Demonstração

### Tela Principal
- Interface limpa com campo para URL do YouTube
- Botão de preview para visualizar informações do vídeo
- Opções de qualidade de download

### Funcionalidades Principais
- **Preview de Vídeo**: Thumbnail, título, autor, duração e visualizações
- **Opções de Download**: 
  - Máxima qualidade (MP4)
  - Qualidade baixa (MP4 - arquivo menor)
  - Apenas áudio (MP3)
- **Download Automático**: Arquivo baixado diretamente para o seu PC

## 📋 Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

## 🔧 Instalação

1. **Clone o repositório**
```bash
git clone https://github.com/Pedrocarv007/videodownload.git
cd videodownload
```

2. **Crie um ambiente virtual (recomendado)**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. **Instale as dependências**
```bash
pip install flask pytubefix
```

4. **Execute a aplicação**

**Para uso local:**
```bash
python app.py
```

**Para uso com IIS:**
```bash
run_iis.bat
```

5. **Acesse no navegador**

**Acesso direto:**
```
http://localhost:5000
```

**Via IIS (após configuração):**
```
http://seudominio/youtube/
```

## 📦 Dependências

- **Flask**: Framework web para Python
- **Flask-Cors**: Suporte a CORS para requisições cross-origin (necessário para IIS)
- **pytubefix**: Biblioteca para download de vídeos do YouTube (fork atualizado do pytube)
- **Font Awesome**: Ícones (via CDN)
- **Google Fonts**: Fonte Inter (via CDN)

### Dependências Python Completas:
```
Flask==2.3.3
Flask-Cors==4.0.0
pytubefix==5.6.1
Werkzeug==2.3.7
Jinja2==3.1.2
MarkupSafe==2.1.3
click==8.1.7
itsdangerous==2.1.2
blinker==1.6.3
```

## 🎯 Como Usar

1. **Acesse a aplicação** no seu navegador
2. **Cole a URL** do vídeo do YouTube no campo de entrada
3. **Clique em "Visualizar"** para ver as informações do vídeo
4. **Escolha a qualidade** desejada:
   - Máxima qualidade para melhor resolução
   - Qualidade baixa para arquivos menores
   - Apenas áudio para formato MP3
5. **Clique em "Baixar Vídeo"**
6. **O arquivo será baixado** automaticamente para seu computador

## 📁 Estrutura do Projeto

```
videodownload/
│
├── app.py                 # Aplicação principal Flask
├── config.py             # Configurações da aplicação
├── README.md             # Documentação principal
├── GUIA_USO.md          # Guia de uso básico
├── GUIA_IIS.md          # Guia específico para IIS
├── requirements.txt      # Dependências Python
├── run.bat              # Script para execução local
├── run_iis.bat          # Script para execução com IIS
├── web.config           # Configuração de exemplo para IIS
│
├── downloads/           # Pasta para arquivos baixados (criada automaticamente)
│
├── static/
│   └── style.css        # Estilos CSS modernos
│
└── templates/
    ├── index.html       # Página principal
    ├── 404.html         # Página de erro 404
    └── 500.html         # Página de erro 500
```

## 🌐 Integração com IIS

Este projeto possui suporte completo para integração com **Internet Information Services (IIS)**.

### Configuração Rápida:
1. Execute: `run_iis.bat`
2. Configure as regras do IIS conforme descrito em `GUIA_IIS.md`
3. Acesse via: `http://seudominio/youtube/`

### Recursos para IIS:
- ✅ **CORS habilitado** para requisições cross-origin
- ✅ **URLs absolutas** configuradas automaticamente
- ✅ **Porta personalizada** (6001) para evitar conflitos
- ✅ **Regras de rewrite** otimizadas
- ✅ **Suporte a métodos POST** para downloads

### Arquivos de Configuração:
- `run_iis.bat` - Script para iniciar com configurações IIS
- `web.config` - Configuração de exemplo para IIS
- `GUIA_IIS.md` - Guia completo de configuração

## ⚙️ Configurações

### Variáveis de Ambiente
Você pode configurar as seguintes variáveis:

- `SECRET_KEY`: Chave secreta para sessões Flask (mude em produção)
- `FLASK_CONFIG`: Configuração do ambiente (`development`, `production`)
- `FLASK_HOST`: Host do servidor (padrão: `0.0.0.0` local, `127.0.0.1` IIS)
- `FLASK_PORT`: Porta do servidor (padrão: `5000` local, `6001` IIS)
- `FLASK_DEBUG`: Modo debug (`True`/`False`)
- `DOWNLOADS_DIR`: Diretório para salvar downloads

### Personalização
- Modifique `static/style.css` para personalizar o design
- Ajuste `app.py` para adicionar novas funcionalidades
- Personalize templates em `templates/`

## 🛡️ Segurança

- ✅ Validação de URLs do YouTube
- ✅ Sanitização de nomes de arquivos
- ✅ Tratamento de erros robusto
- ✅ Proteção contra caracteres inválidos
- ✅ Limitação de tamanho de nome de arquivo

## 📱 Compatibilidade

- **Navegadores**: Chrome, Firefox, Safari, Edge
- **Dispositivos**: Desktop, Tablet, Mobile
- **Sistemas**: Windows, Linux, macOS

## 🚀 Deploy

### Desenvolvimento Local
```bash
python app.py
# ou
run.bat
```

### Produção com IIS
```bash
run_iis.bat
```
*Configure as regras do IIS conforme `GUIA_IIS.md`*

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Docker (opcional)
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

## 🔄 Atualizações Futuras

- [ ] Sistema de autenticação
- [ ] Histórico de downloads
- [ ] Download de playlists
- [ ] API REST
- [ ] Suporte a outros sites
- [ ] Download em lote

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## ⚠️ Disclaimer

Este projeto é apenas para fins educacionais. Respeite os termos de uso do YouTube e as leis de direitos autorais. Use apenas com vídeos que você tem permissão para baixar.

## 📞 Suporte

Se você encontrar algum problema ou tiver sugestões:

1. Verifique as [Issues existentes](https://github.com/Pedrocarv007/videodownload/issues)
2. Crie uma nova issue se necessário
3. Forneça detalhes sobre o problema

## 🙏 Agradecimentos

- [pytube](https://github.com/pytube/pytube) - Biblioteca original para YouTube
- [pytubefix](https://github.com/JuanBindez/pytubefix) - Fork mantido e atualizado
- [Flask](https://flask.palletsprojects.com/) - Framework web minimalista
- [Font Awesome](https://fontawesome.com/) - Ícones incríveis

---

**Feito com ❤️ para a comunidade**