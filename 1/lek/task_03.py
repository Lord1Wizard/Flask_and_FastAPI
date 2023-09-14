from flask import Flask
from flask import render_template

app = Flask(__name__)

html = """
<h1>Привет, меня зовут Сергей</h1>
<p>Уже много лет я занимаюсь программированием.<br/>Посмтори на мои программы</p>
"""
@app.route('/')
@app.route('/<name>/')
def hello(name='незнакомец'):
    return f'Привет, {name.capitalize()}!'

@app.route('/file/<path:file>/')
def set_path(file):
    print(type(file))
    return f'Путь до файла "{file}"'

@app.route('/number/<float:num>')
def set_number(num):
    print(type(num))
    return f'Переданное число {num}'

@app.route('/poems/')
def poems():
    poem = ['Вот не думал, не гадал,',
            'Программистом взял и стал.',
            'Хитрый знает он язык,',
            'Он к другому не привык.',
            ]
    txt = '<h1>Стихотворение</h1>\n<p>'+'<br/>'.join(poem)+'</p>'
    return txt

@app.route('/text/')
def text():
    return html


if __name__ == '__main__':
    app.run()
