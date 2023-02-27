from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.db")
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    user.hashed_password = "cap"

    user1 = User()
    user1.surname = "Scott"
    user1.name = "Warter"
    user1.age = 24
    user1.position = "engineer"
    user1.speciality = "search engineer"
    user1.address = "module_2"
    user1.email = "scott_warter@mars.org"
    user1.hashed_password = "scott"

    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.add(user1)
    db_sess.commit()
    # app.run()


if __name__ == '__main__':
    main()