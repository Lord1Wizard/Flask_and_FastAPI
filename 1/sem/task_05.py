# Написать функцию, которая будет выводить на экран HTML
# страницу с заголовком "Моя первая HTML страница" и
# абзацем "Привет, мир!".
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

@app.route('/<int:num>/<int:num2>/')
def add_nums(num, num2):
    return str(num+num2)

@app.route('/str-len/<str_inp>/')
def str_len(str_inp):
    return f'{len(str_inp)= }'

@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/contact2/')
def contact2():
    context = {
        'title': 'Личный блог',
        'name': 'Харитон'
    }
    return render_template('contact2.html',**context)

if __name__ == '__main__':
    app.run()