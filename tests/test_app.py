from http import HTTPStatus

from fast_zero.schemas import UserPublic


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')  # Act (Agir - fase 2 do testo)

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo'}


def test_root_deve_retornar_html(client):
    response = client.get('/exercicio-1-html')  # Act (Agir - fase 2 do testo)

    assert response.status_code == HTTPStatus.OK
    assert '<h1>Olá Mundo</h1>' in response.text


def test_root_deve_retornar_html_formulario(client):
    response = client.get('/test-form')

    assert response.status_code == HTTPStatus.OK
    assert '<h1>Teste de Criação de Usuário</h1>' in response.text


def test_root_deve_retornar_pagina_html(client):
    response = client.get('/test-all-endpoints')

    assert response.status_code == HTTPStatus.OK
    assert '<h1>Teste de Todos os Endpoints de Usuários</h1>' in response.text


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'alice',
        'email': 'alice@example.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': []}


def test_update_user(client):
    # Primeiro criar um usuário
    client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )

    response = client.put(
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'bob',
        'email': 'bob@example.com',
        'id': 1,
    }


def test_delete_user(client, user):
    response = client.delete(f'/users/{user.id}')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


def test_delete_user_not_found(client):
    response = client.delete('/users/500')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_update_user_not_found_exercicio_01_aula03(client):
    respose = client.put(
        '/users/500',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )
    assert respose.status_code == HTTPStatus.NOT_FOUND
    assert respose.json() == {'detail': 'User not found'}


def test_get_no_return_id_exercicio_02_aula03(client):
    response = client.get('/users/789')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_get_return_id__exercicio_04_aula05(client, user):
    response = client.get(f'/users/{user.id}')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': user.username,
        'email': user.email,
        'id': user.id,
    }


def test_read_users_with_users(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get('/users/')
    assert response.json() == {'users': [user_schema]}


def test_update_integrity_error(client, user):
    client.post(
        '/users/',
        json={
            'username': 'fausto',
            'email': 'fausto@example.com',
            'password': 'secret',
        },
    )

    response_update = client.put(
        f'/users/{user.id}',
        json={
            'username': 'fausto',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )

    assert response_update.status_code == HTTPStatus.CONFLICT
    assert response_update.json() == {
        'detail': 'Username or Email already exists'
    }


def test_create_username_integrity_error(client, user):
    response_create = client.post(
        '/users/',
        json={
            'username': user.username,
            'email': 'teste@test.com',
            'password': 'teste123456789',
        },
    )

    assert response_create.status_code == HTTPStatus.CONFLICT
    assert response_create.json() == {'detail': 'Username already exists'}


def test_create_email_integrity_error(client, user):
    response_create = client.post(
        '/users/',
        json={
            'username': 'Leandro',
            'email': user.email,
            'password': 'testtest',
        },
    )

    assert response_create.status_code == HTTPStatus.CONFLICT
    assert response_create.json() == {'detail': 'Email already exists'}
