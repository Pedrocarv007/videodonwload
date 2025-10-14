import os

class Config:
    """Configurações da aplicação"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    DOWNLOADS_DIR = os.path.join(os.path.dirname(__file__), 'downloads')
    MAX_CONTENT_LENGTH = 500 * 1024 * 1024  # 500MB max file size
    
    # YouTube download settings
    DEFAULT_QUALITY = 'highest'
    SUPPORTED_QUALITIES = ['highest', 'lowest', 'audio']
    
    # Flask settings
    DEBUG = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    HOST = os.environ.get('FLASK_HOST', '0.0.0.0')
    PORT = int(os.environ.get('FLASK_PORT', 5000))

class DevelopmentConfig(Config):
    """Configurações de desenvolvimento"""
    DEBUG = True

class ProductionConfig(Config):
    """Configurações de produção"""
    DEBUG = False
    
    def __init__(self):
        secret_key = os.environ.get('SECRET_KEY')
        if secret_key:
            self.SECRET_KEY = secret_key
        else:
            # Em produção, use uma chave mais segura
            import secrets
            self.SECRET_KEY = secrets.token_hex(16)

# Configuração padrão
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}