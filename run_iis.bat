@echo off
echo Iniciando YouTube Video Downloader para IIS...
echo.

REM Verifica se o Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ERRO: Python não encontrado. Por favor, instale o Python 3.8 ou superior.
    pause
    exit /b 1
)

REM Verifica se as dependências estão instaladas
echo Verificando dependências...
python -c "import flask, pytubefix, flask_cors" >nul 2>&1
if errorlevel 1 (
    echo Instalando dependências...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ERRO: Falha ao instalar dependências.
        pause
        exit /b 1
    )
)

echo Dependências verificadas com sucesso!
echo.
echo Iniciando servidor Flask na porta 6001 para IIS...
echo.
echo IMPORTANTE: Configure sua regra do IIS para:
echo ^<rule name="Youtube" stopProcessing="true"^>
echo   ^<match url="^youtube/(.*)" /^>
echo   ^<action type="Rewrite" url="http://localhost:6001/{R:1}" /^>
echo ^</rule^>
echo.
echo Acesse via IIS: http://seudominio/youtube/
echo Acesse direto: http://localhost:6001
echo.
echo Pressione Ctrl+C para parar o servidor
echo.

REM Define variáveis de ambiente para IIS
set FLASK_CONFIG=production
set FLASK_HOST=127.0.0.1
set FLASK_PORT=6001

python app.py