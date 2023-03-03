import datetime

from flask import Flask, render_template, redirect
from data import db_session
from data.users import User
from data.jobs import Jobs
from form import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route('/')
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()

    return render_template('journal_work.html', title="start", jobs=jobs)

@app.route('/register', methods=['GET', 'POST'])
def login():
    form = RegisterForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('register.html', title='Регистрация', form=form)

@app.route('/success')
def success():
    return 'success'

def main():
    db_name = "db/mars_explorer.db"
    db_session.global_init(db_name)
    app.run()


if __name__ == '__main__':
    main()