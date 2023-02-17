from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def selection():
    param = {}
    # param['username'] = "Ученик Яндекс.Лицея"
    param['title'] = 'Форма'
    return render_template('selection.html', **param)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')