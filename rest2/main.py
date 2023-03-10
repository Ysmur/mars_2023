import datetime

from flask import Flask, render_template, redirect
from data import db_session, users_resource
from data.users import User
from data.jobs import Jobs
from form import LoginForm, RegisterForm, WorksForm
from flask_login import LoginManager, login_user, logout_user, login_required
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)

# для списка объектов
api.add_resource(users_resource.UsersResource, '/api/v2/users/<int:user_id>')

@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)

@app.route('/')
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()

    return render_template('journal_work.html', title="start", jobs=jobs)

@app.route('/add_work', methods=['GET', 'POST'])
def add_work():
    form = WorksForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        job = Jobs(
            # team_leader=form.team_leader.data,
            job=form.job.data,
            # work_size=form.work_size.data,
            # is_finished=form.is_finished.data
        )
        db_sess.add(job)
        db_sess.commit()
        return redirect('/')
    return render_template('add_work.html', title='Добавление работ', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
            # about=form.about.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        # return redirect('/login')
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