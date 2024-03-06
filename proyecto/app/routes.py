from flask import Blueprint, render_template

# Blueprint para usuarios
usuarios_bp = Blueprint('usuarios_bp', __name__)

# Ruta para listar usuarios
@usuarios_bp.route('/usuarios')
def listar_usuarios():
    return render_template('usuarios.html',usuarios=usuarios)

# Blueprint para productos
productos_bp = Blueprint('productos_bp', __name__)

# Ruta para listar productos
@productos_bp.route('/productos')
def listar_productos():
    return render_template('productos.html',productos=productos)

# Blueprint para ordenes de compra
ordenes_bp = Blueprint('ordenes_bp', __name__)

# Ruta para listar ordenes de compra
@ordenes_bp.route('/ordenes')
def listar_ordenes():
    return render_template('ordenes.html',ordenes=ordenes)




