from flask import Flask, url_for, request

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
                                                 f' alt="not found"><p>Вот она какая, '
                                                 f'красная планета</p></body></html>')


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


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h2 align="center" color="#000000">Анкета претендента</h2>
                            <h2 align="center">на участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="surname" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                    <input type="name" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    </br></br>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="graduationSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="classSelect" name="graduation" type="graduation">
                                          <option>Начальное</option>
                                          <option>Среднее общее</option>
                                          <option>Среднее специальное</option>
                                          <option>Высшее</option>
                                          <option>Нет</option>
                                        </select>
                                     </div>
                                     <label for="professionSelect">Какие у Вас есть профессии?</label></br>
                                     <div class="form-group form-check">
                                    <input type="checkbox" class="form-check-input" value="Инженер-исследователь" name="profession">Инженер-исследователь</br>
                                    <input type="checkbox" class="form-check-input" value="Инженер-строитель" name="profession">Инженер-строитель</br>
                                    <input type="checkbox" class="form-check-input" value="Пилот" name="profession">Пилот</br>
                                    <input type="checkbox" class="form-check-input" value="Метеоролог" name="profession">Метеоролог</br>
                                    <input type="checkbox" class="form-check-input" value="Инженер по жизнеобеспечению" name="profession">Инженер по жизнеобеспечению</br>
                                    <input type="checkbox" class="form-check-input" value="Инженер по радиационной защите" name="profession">Инженер по радиационной защите</br>
                                    <input type="checkbox" class="form-check-input" value="Врач" name="profession">Врач</br>
                                    <input type="checkbox" class="form-check-input" value="Экзобиолог" name="profession">Экзобиолог</br>
                
                                    </div>
                                      <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        try:
            print(request.form['email'])
            print(request.form['name'])
            print(request.form['surname'])
            print(request.form['file'])
            print(request.form['graduation'])
            print(request.form['sex'])
            print(request.form.getlist('profession'))
        except Exception as e:
            return f'<h2 background-color="#FF0000">{str(e)}</h2>'
        else:
            return "Форма отправлена"


@app.route('/choice/<planet_name>')
def greeting(planet_name):
    prom = ['На ней много необходимых ресурсов;', 'На ней есть вода и атмосфера;',
            'На ней есть небольшое магнитное поле;', 'Наконец, она просто красива!']
    counter = ['success', 'secondary', 'primary', 'danger']
    info = ''
    for i in range(len(prom)):
        info += f'<div class="alert alert-{counter[i]}" role="alert">'
        info += prom[i] + '</div>'
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                   <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                    <title>Варианты выбора</title>
                  </head>
                  <body>
                    <h1>Мое предложение: {planet_name}</h1>
                    <h2>Эта планета близка к земле;</h2>{info}
                  </body>
                </html>'''


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def result(nickname, level, rating):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                   <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                    <title>Результаты</title>
                  </head>
                  <body>
                    <h1>Результаты отбора</h1>
                    <h2>Претендента на участие в миссии {str(nickname)}:</h2>
                    <div class="alert alert-success" role="alert">Поздравляем! Ваш рейтинг после {str(level)} этапа отбора</div>
                    <h3>Составляет {str(rating)}!</h3>
                    <div class="alert alert-danger" role="alert">Желаем удачи!</div>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
