from flask import Flask, render_template, request, redirect
from loginform import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route('/', methods=['POST', 'GET'])
def selection():
    if request.method == 'GET':
        param = {}
        # param['username'] = "Ученик Яндекс.Лицея"
        param['title'] = 'Форма'
        return render_template('selection.html', **param)
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/success')
def success():
    return 'success'


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')