import sqlalchemy
from flask import jsonify
from flask_restful import Resource, abort, reqparse
from data import db_session
from data.users import User

parser = reqparse.RequestParser()
parser.add_argument('surname', required=True)
parser.add_argument('name', required=True)
parser.add_argument('age', required=True)
parser.add_argument('position', required=True)
parser.add_argument('address', required=True)
parser.add_argument('speciality', required=True)
parser.add_argument('email', required=True)
parser.add_argument('hashed_password', required=True)

def abort_if_user_not_found(user_id):
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    if not user:
        abort(404, message=f"User {user_id} not found")

class UsersResource(Resource):
    def get(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        return jsonify({'users': user.to_dict(
            only=('name', 'surname'))})

class UsersListResource(Resource):
    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        user = User(
            surname=args['surname'],
            name=args['name'],
            age=args['age'],
            position=args['position'],
            email=args['email'],
           # hashed_password=args['hashed_password']
        )
        user.set_password(args['hashed_password'])
        try:
            session.add(user)
            session.commit()
        except sqlalchemy.exc.IntegrityError:
            return jsonify({'error': 'wrong email'})
        return jsonify({'success': 'OK'})

    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'users': [user.to_dict(
            only=('name', 'surname')) for user in users]})

