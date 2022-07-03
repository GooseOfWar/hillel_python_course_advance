"""
Home work 2

1. Возвращать содержимое файла с пайтон пакетами (requirements.txt)
PATH: /requirements/ открыть файл requirements.txt и вернуть его содержимое

2. Вывести 100 случайно сгенерированных юзеров (почта + имя)
'Dmytro aasdasda@mail.com'
PATH: /generate-users/ ( https://pypi.org/project/Faker/ )
+ параметр который регулирует количество юзеров

3. Вывести количество космонавтов в настоящий момент
(http://api.open-notify.org/astros.json) (https://pypi.org/project/requests/)
PATH: /space/

import requests
r = requests.get('https://api.github.com/repos/psf/requests')
r.json()["description"]
* Считать файл hw.csv и посчитать средний рост, средний вес в см и кг соответственно
PATH: /mean/

!!! прислать 3 файла main.py, utils.py, requirements.txt !!!
"""
import requests

from flask import Flask, request
from utils import FakeUserData


app = Flask(__name__)


#
# @app.route('/')
# def hello_world():
#     return 'Hello, World!'


@app.route('/requirements/')
def requirements():
    """
    Return requierments.txt content
    """
    with open('requirements.txt', mode='r', encoding='utf-16LE') as f:
        file_content: list = f.readlines()
        file_content: str = '\n</br>'.join(file_content)
    return file_content


@app.route('/generate-users/')
def fake_users_data():
    """
    Function return some nambers of fake users and email
    """
    number = request.args['number']
    result = FakeUserData(int(number))
    return result.oh_so_many_fake_users()


@app.route('/space/')
def astronauts_on_orbit():
    """
    Function show how many astronauts on Earth orbit now
    """
    req = requests.get('http://api.open-notify.org/astros.json')
    number_of_astronauts_on_orbit = req.json()["number"]
    return str(number_of_astronauts_on_orbit)



# 1-25000

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    print(requirements())
    print(fake_users_data())
    print(astronauts_on_orbit())

# http://192.168.88.240:5000/
