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
```bash
python app.py
```

5. **Acesse no navegador**
```
http://localhost:5000
```

## 📦 Dependências

- **Flask**: Framework web para Python
- **pytubefix**: Biblioteca para download de vídeos do YouTube
- **Font Awesome**: Ícones (via CDN)
- **Google Fonts**: Fonte Inter (via CDN)

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
├── README.md             # Documentação
├── requirements.txt      # Dependências (criar se necessário)
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

## ⚙️ Configurações

### Variáveis de Ambiente
Você pode configurar as seguintes variáveis:

- `SECRET_KEY`: Chave secreta para sessões Flask (mude em produção)
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
```

### Produção (exemplo com Gunicorn)
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
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