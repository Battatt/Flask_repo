from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Миссия колонизация Марса"


@app.route('/index')
def second_index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def third_index():
    return "</br>".join(['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
                         'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!',
                         'Присоединяйся!'])


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
