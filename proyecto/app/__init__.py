
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import config  # Importa la variable config

# Initialize Flask app
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])  # Utiliza la variable config
    db.init_app(app)
    return app

# Create SQLAlchemy instance
db = SQLAlchemy()

# Import routes after db initialization to avoid circular imports
from .routes import usuarios_bp, productos_bp, ordenes_bp



