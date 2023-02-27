from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_name = input()  # "db/mars_explorer.db"
    db_session.global_init(db_name)
    db_sess = db_session.create_session()
    for user in db_sess.query(User).filter(User.address.like("%module_1%")):
        print(user)
    # app.run()


if __name__ == '__main__':
    main()