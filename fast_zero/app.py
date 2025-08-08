from http import HTTPStatus

from fastapi import FastAPI
from starlette.responses import HTMLResponse

from fast_zero.schemas import Message

app = FastAPI()


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
