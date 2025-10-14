# 🚀 GUIA DE INICIALIZAÇÃO RÁPIDA

## Como executar o YouTube Video Downloader

### Método 1: Script Automático (Recomendado)
1. Clique duas vezes no arquivo `run.bat`
2. O script verificará e instalará automaticamente as dependências
3. A aplicação será iniciada automaticamente

### Método 2: Manual
1. Abra o terminal/prompt de comando
2. Navegue até a pasta do projeto:
   ```
   cd "c:\Users\pedro\Documents\GitHub\videodonwload"
   ```
3. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```
4. Execute a aplicação:
   ```
   python app.py
   ```

## 🌐 Acessando a Aplicação

Após executar qualquer um dos métodos acima:

1. Abra seu navegador
2. Acesse: **http://localhost:5000**
3. A interface do YouTube Downloader será carregada

## 📱 Como Usar

1. **Cole a URL** do vídeo do YouTube
2. **Clique em "Visualizar"** para ver as informações
3. **Escolha a qualidade** (Máxima, Baixa ou Apenas Áudio)
4. **Clique em "Baixar Vídeo"**
5. **O arquivo será baixado** automaticamente para seu PC

## 📁 Localização dos Downloads

Os vídeos baixados ficam salvos na pasta:
`c:\Users\pedro\Documents\GitHub\videodonwload\downloads\`

## ⚠️ Importante

- Mantenha o terminal/prompt aberto enquanto usar a aplicação
- Para parar o servidor, pressione `Ctrl+C` no terminal
- Use apenas URLs válidas do YouTube
- Respeite os direitos autorais dos vídeos

## 🆘 Resolução de Problemas

### Python não encontrado
- Instale o Python 3.8+ do site oficial: https://python.org

### Erro de dependências
- Execute: `pip install --upgrade pip`
- Em seguida: `pip install -r requirements.txt`

### Porta 5000 ocupada
- Feche outros programas que possam estar usando a porta 5000
- Ou altere a porta no arquivo `config.py`

## 🎯 Dicas

- Use URLs diretas do YouTube (ex: https://www.youtube.com/watch?v=...)
- Para melhor qualidade, escolha "Máxima Qualidade"
- Para economizar espaço, escolha "Qualidade Baixa"
- Para música, escolha "Apenas Áudio" (MP3)