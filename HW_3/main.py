"""
1. Создать таблицу phones с полями contactName, phone
2. Реализовать CRUD операции для таблицы phones
(/phones/create/, /phones/read/, /phones/update/, /phones/delete/)
"""
from flask import Flask

app = Flask(__name__)


@app.route('/phones/create/')
def create_db():
    return 'Emails Create'


@app.route('/phones/read/')
def read_db():
    return str(emails)


@app.route('/phones/update/')
def update_db():
    return 'Emails Delete'


@app.route('/phones/delete/')
def delete_db():
    return 'Emails Update'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
