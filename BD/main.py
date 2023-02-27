import datetime

from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_name = "db/mars_explorer.db"
    db_session.global_init(db_name)
    job = Jobs()
    job.team_leader = 1
    job.job = "deployment of residential modules 1 and 2"
    job.work_size = 15
    job.collaborators = '2, 3'

    job.start_date = datetime.datetime.now().date()
    # job.end_date = 'datetime.'
    job.is_finished = False

    db_sess = db_session.create_session()
    db_sess.add(job)
    db_sess.commit()
    # app.run()


if __name__ == '__main__':
    main()