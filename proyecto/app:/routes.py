from flask import Blueprint, jsonify
from .models import Usuario, Producto

usuarios_bp = Blueprint('usuarios', __name__, url_prefix='/usuarios')
productos_bp = Blueprint('productos', __name__, url_prefix='/productos')

@usuarios_bp.route('/')
def obtener_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([usuario.__dict__ for usuario in usuarios])

@productos_bp.route('/')
def obtener_productos():
    productos = Producto.query.all()
    return jsonify([producto.__dict__ for producto in productos])
