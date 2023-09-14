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
def hello_world():
    return 'Hello World'


@app.route('/index/')
def index():
    context = {
        'title': 'Hoom',
        'news': [
            {
                "title": "Путин подарил Ким Чен Ыну",
                "description": "Путин подарил Ким Чен Ыну карабин и побывавшую в космосе перчатку от скафандра",
                "date": '2023-09-14'
            },
            {
                "title": "саммит G20",
                "description": "Spiked: саммит G20 завершился крупной победой России и потерей влияния Запада",
                "date": '2023-09-14'
            },
        ]
    }
    return render_template('index.html', **context)


@app.route('/news/')
def news():
    context = {
        'title': 'Новости',
        'news': [
            {
                "title": "Путин подарил Ким Чен Ыну",
                "description": "Путин подарил Ким Чен Ыну карабин и побывавшую в космосе перчатку от скафандра",
                "date": '2023-09-14'
            },
            {
                "title": "саммит G20",
                "description": "Spiked: саммит G20 завершился крупной победой России и потерей влияния Запада",
                "date": '2023-09-14'
            },
        ]
    }
    return render_template('news.html', **context)


if __name__ == '__main__':
    app.run()
