@echo off
echo Iniciando YouTube Video Downloader...
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
python -c "import flask, pytubefix" >nul 2>&1
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
echo Iniciando servidor web...
echo.
echo Acesse no navegador: http://localhost:5000
echo.
echo Pressione Ctrl+C para parar o servidor
echo.

python app.py