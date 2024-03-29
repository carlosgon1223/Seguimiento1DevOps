import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'una-llave-secreta-por-defecto'
    SQLALCHEMY_DATABASE_URI = 'postgresql://carlosgon:carlos123@localhost:5440/carlosgon'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test_database.db'

class ProductionConfig(Config):
    pass

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}



