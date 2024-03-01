from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_name)

    db.init_app(app)

    from .routes import usuarios_bp, productos_bp
    app.register_blueprint(usuarios_bp)
    app.register_blueprint(productos_bp)

    return app

