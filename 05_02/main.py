from flask import Flask, url_for

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


@app.route('/image_mars')
def number_four_index():
    return (('<!doctype html>'
             '<html lang="en">'
             '<head><meta charset="utf-8">'
             '<title>Привет, Марс!</title>'
             '</head>'
             '<body>'
             '<h1><i>Жди нас, Марс!</i></h1>') + f'<img src="{url_for('static', filename='img/Mars.png')}"'
                                                 f' alt="not found"></body></html>')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
