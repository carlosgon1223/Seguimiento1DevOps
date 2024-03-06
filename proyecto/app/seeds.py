from app import db
from app.models import Usuario, Producto, OrdenCompra
import random

def crear_usuarios():
    nombres_usuarios = ["Ana García", "Carlos López", "María Rodríguez", "Juan Martínez", "Laura Pérez"]
    for nombre in nombres_usuarios:
        usuario = Usuario(nombre=nombre)
        db.session.add(usuario)
    db.session.commit()

def crear_productos():
    nombres_productos = ["Camiseta básica", "Pantalones vaqueros", "Zapatos deportivos", "Abrigo de invierno", "Vestido de fiesta"]
    precios_productos = [19.99, 29.99, 59.99, 79.99, 99.99]
    for nombre, precio in zip(nombres_productos, precios_productos):
        producto = Producto(nombre=nombre, precio=precio)
        db.session.add(producto)
    db.session.commit()

def crear_ordenes_compra():
    usuarios = Usuario.query.all()
    productos = Producto.query.all()
    for usuario in usuarios:
        for _ in range(4):
            producto = random.choice(productos)
            cantidad = random.randint(1, 10)
            orden_compra = OrdenCompra(usuario_id=usuario.id, producto_id=producto.id, cantidad=cantidad)
            db.session.add(orden_compra)
    db.session.commit()

if __name__ == '__main__':
    crear_usuarios()
    crear_productos()
    crear_ordenes_compra()
