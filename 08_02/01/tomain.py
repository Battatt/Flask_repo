from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route("/<title>")
@app.route("/index/<title>")
def first_index(title):
    return render_template('base.html', title=title)


@app.route("/training/<prof>")
def second_index(prof):
    if 'ИНЖЕНЕР' in prof.upper() or 'СТРОИТЕЛ' in prof.upper():
        prof = 0
    else:
        prof = 1
    return render_template('prof.html', prof=prof, title="Профессия")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
