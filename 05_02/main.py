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


@app.route('/promotion_image')
def promotion_image():
    prom = (['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
                         'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!',
                         'Присоединяйся!'])
    counter = ['secondary', 'primary', 'success', 'info', 'danger']
    promoute = ''
    for i in range(len(prom)):
        promoute += f'<div class="alert alert-{counter[i]}" role="alert">'
        promoute += prom[i] + '</div></br>'
    res = f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" 
                    href="{url_for('static', filename='css/style.css')}" />
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/Mars.png')}" alt="not found">
                    {promoute}
                  </body>
                  </html>"""
    return res


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
