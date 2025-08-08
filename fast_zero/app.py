from http import HTTPStatus

from fastapi import FastAPI
from starlette.responses import HTMLResponse

from fast_zero.schemas import Message, UserDB, UserPublic, UserSchema

app = FastAPI()

database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo'}


@app.get('/exercicio-1-html', response_class=HTMLResponse)
def exercicio_1_html_aula_2():
    return """
    <html>
        <head>
            <title>Exercício 1</title>
        </head>
        <body>
            <h1>Olá Mundo</h1>
        </body>
    </html>
    """


@app.post('/users', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)

    database.append(user_with_id)

    return user_with_id
