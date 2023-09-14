from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hi!'

@app.route('/index/')
def html_index():
    return render_template('index.html')

@app.route('/index2/')
def html_index2():
    context = {
        'title': 'Личный блог',
        'name': 'Харитон'
    }
    return render_template('index2.html', **context)

@app.route('/if/')
def show_if():
    context = {
        'title': 'Ветвление',
        'user': 'Хакер!',
        'number': 1
    }
    return render_template('show_if.html', **context)

@app.route('/for/')
def show_for():
    context = {'title': 'Цикл',
            'poem': ['Вот не думал, не гадал,',
                    'Программистом взял и стал.',
                    'Хитрый знает он язык,',
                    'Он к другому не привык.',
                    ]}
    return render_template('show_for.html', **context)

@app.route('/users/')
def users():
    _user = [{'name': 'Никанор',
              'mail': 'nik@mail.ru',
              'phone': '+7-903-444-32-10'},
             {'name': 'Феофан',
              'mail': 'feo@mail.ru',
              'phone': '+7-913-444-32-10'},
             {'name': 'Оверран',
              'mail': 'over@mail.ru',
              'phone': '+7-923-444-32-10'},
             ]
    context = {'users': _user,
               'title': 'Точечная нотация'}
    return render_template('users.html', **context)


if __name__ == '__main__':
    app.run(debug=True)