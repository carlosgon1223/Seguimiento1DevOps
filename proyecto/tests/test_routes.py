def test_obtener_usuarios(client):
    response = client.get('/usuarios')
    assert response.status_code == 200

def test_obtener_productos(client):
    response = client.get('/productos')
    assert response.status_code == 200

