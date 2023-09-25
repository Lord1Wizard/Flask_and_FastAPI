# Задание №1
# Создать страницу, на которой будет кнопка "Нажми меня", при
# нажатии на которую будет переход на другую страницу с
# приветствием пользователя по имени.

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def index():
    context = {
        'title': 'Hoom',
        'products': [{'name': 'clothes',
                      'title': 'Одежда'},
                     {'name': 'shoes',
                      'title': 'Обувь'}
                     ]
    }
    return render_template('index.html', **context)

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        return f'Hello {name}!'
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
