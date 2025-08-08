from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app) # Arrange (Organizar - fase 1 do teste)

    response = client.get('/') # Act (Agir - fase 2 do testo)

    assert response.status_code == HTTPStatus.OK # Assert (Afirmar - fase 3 do teste)
    assert response.json() == {'message': 'Olá Mundo'} # Assert (Afirmar - fase 3 do teste)


def test_root_deve_retornar_html():
    client = TestClient(app) # Arrange (Organizar - fase 1 do teste)

    response = client.get('/exercicio-1-html') # Act (Agir - fase 2 do testo)

    assert response.status_code == HTTPStatus.OK # Assert (Afirmar - fase 3 do teste)
    assert '<h1>Olá Mundo</h1>' in response.text # Assert (Afirmar - fase 3 do teste)
