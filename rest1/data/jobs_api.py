import sqlite3
from datetime import datetime

import flask
import sqlalchemy
from flask import jsonify, request

from . import db_session
from .jobs import Jobs

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    print(jobs)
    return jsonify(
        {
            'jobs':
                [item.to_dict(only=('job',))
                 for item in jobs]
        }
    )


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['GET'])
def get_one_jobs(jobs_id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).get(jobs_id)
    if not jobs:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'jobs': jobs.to_dict(only=(
                'job', 'user.name', 'user.surname', 'work_size', 'collaborators'))
        }
    )

@blueprint.route('/api/jobs', methods=['POST'])
def create_jobs():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['job', 'work_size', 'team_leader']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    try:
        jobs = Jobs(
            id=2,
            job=request.json['job'],
            team_leader=request.json['team_leader'],
            work_size=request.json['work_size'],
            collaborators=request.json['collaborators'],
            start_date=datetime.now().date(),
            end_date=datetime.now().date(),
            is_finished=False
        )
        db_sess.add(jobs)
        db_sess.commit()
    except sqlalchemy.exc.IntegrityError:
        return jsonify({'error': 'id'})
    return jsonify({'success': 'OK'})