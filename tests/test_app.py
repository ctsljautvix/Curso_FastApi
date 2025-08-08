from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')  # Act (Agir - fase 2 do testo)

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo'}


def test_root_deve_retornar_html(client):
    response = client.get('/exercicio-1-html')  # Act (Agir - fase 2 do testo)

    assert response.status_code == HTTPStatus.OK
    assert '<h1>Olá Mundo</h1>' in response.text


def test_create_user():
    Client = TestClient(app)

    response = Client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username':  'alice',
        'email': 'alice@example.com',
        'id': 1,

    }
