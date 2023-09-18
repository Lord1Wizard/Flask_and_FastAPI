# Задание №9
# Создать базовый шаблон для интернет-магазина,
# содержащий общие элементы дизайна (шапка, меню,
# подвал), и дочерние шаблоны для страниц категорий
# товаров и отдельных товаров.
# Например, создать страницы "Одежда", "Обувь" и "Куртка",
# используя базовый шаблон.

from flask import Flask, render_template

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


@app.route('/clothes/')
def clothes():
    context = {
        'title': 'Hoom',
        'products': [{'name': 'jackets',
                     'title': 'Куртки'},
                     {'name': 'coat',
                     'title': 'пальто'},
                     {'name': 'raincoats',
                      'title': 'Плащи'}
                     ]
    }
    return render_template('clothes.html', **context)


@app.route('/jackets/')
def jackets():
    return render_template('jackets.html')
@app.route('/coat/')
def coat():
    return render_template('coat.html')
@app.route('/raincoats/')
def raincoats():
    return render_template('raincoats.html')
@app.route('/shoes/')
def shoes():
    return render_template('shoes.html')


if __name__ == '__main__':
    app.run()
