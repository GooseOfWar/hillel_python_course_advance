"""
1. Создать таблицу phones с полями contactName, phone
2. Реализовать CRUD операции для таблицы phones
(/phones/create/, /phones/read/, /phones/update/, /phones/delete/)
"""
from flask import Flask, request
from utils import DBOperator

app = Flask(__name__)


@app.route('/')
def first_start_db():
    result = '''
    <a href="phones/create/?Name=Example_Name&Phone=+1010101010101">
    localhost:8000/phones/create/?Name=Example_Name&Phone=+1010101010101</br></a>
    
    <a href="phones/read/"> localhost:8000/phones/read/</br></a>
    
    <a href="phones/update/?Name=Example_Name&Phone=+2020202002020">
    localhost:8000/phones/update/?Name=Example_Name&Phone=+2020202002020</br></a>
    
    <a href="phones/delete/?Name=Example_Name">
    localhost:8000/phones/delete/?Name=Example_Name</br></a>'''

    return result


@app.route('/phones/create/')
def create_db():
    name: str = request.args['Name']
    phone: str = request.args['Phone']
    new_data = DBOperator()
    result = new_data.set_db('-c', data=(name, phone))
    return f'<h1>{result}</h1>'


@app.route('/phones/read/')
def read_db():
    read_data = DBOperator()
    result = read_data.set_db()
    return f'<h1>{result}</h1>'


@app.route('/phones/update/')
def update_db():
    name: str = request.args['Name']
    phone: str = request.args['Phone']
    up_data = DBOperator()
    result = up_data.set_db('-u', name=name, new_phone=phone)

    return f'<h1>{result}</h1>'


@app.route('/phones/delete/')
def delete_db():
    name: str = request.args['Name']

    up_data = DBOperator()
    result = up_data.set_db('-d', delete=str(name))

    return f'<h1>{result} {type(name)}</h1>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
