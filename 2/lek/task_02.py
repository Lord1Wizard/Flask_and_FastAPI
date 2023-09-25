from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hi'

@app.route('/base/<int:num>/')
def base(num):
    print(url_for('index', next='then'))
    text = f'В num лежит {num}<br>'
    # text += f'Функция {url_for("base",num=42) = }<br>'
    # text += f'Функция {url_for("base",num=42,data="new_data") = }<br>'
    # text += f'Функция {url_for("base",num=42,data="new_data",pi=3.14159) = }<br>'
    text += f'Функция {url_for("base",num=42) = }<br>'
    text += f'Функция {url_for("index",data="new_data") = }<br>'
    text += f'Функция {url_for("index",num=42,data="new_data",pi=3.14159) = }<br>'
    text += f'В num лежит {num}<br>'
    return text


# @app.route('/number/<float:num>')
# def set_number(num):
#     print(type(num))
#     return f'Переданное число {num}'


if __name__ == '__main__':
    app.run()
