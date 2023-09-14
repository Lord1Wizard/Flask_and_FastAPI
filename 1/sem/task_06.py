# Задание №6
# Написать функцию, которая будет выводить на экран HTML
# страницу с таблицей, содержащей информацию о студентах.
# Таблица должна содержать следующие поля: "Имя",
# "Фамилия", "Возраст", "Средний балл".
# Данные о студентах должны быть переданы в шаблон через
# контекст.
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/index/')
def index():
    context = {
        'title': 'Личный блог',
        'name': 'Харитон'
        }
    return render_template('index.html')

@app.route('/students/')
def students():
    context = {
        'title': 'Список студентов с оценками',
        'students': [
            {
            "name": "John",
            "surname": "Doe",
            "age": 20,
            "average": 85
            },
            {
            "name": "Jane",
            "surname": "Smith",
            "age": 22,
            "average": 92
            },
            ]
    }
    return render_template('students.html', **context)

if __name__ == '__main__':
    app.run()