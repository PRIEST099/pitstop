from flask import Blueprint, jsonify ,request
from pitstop.models.models import User

api = Blueprint('api', __name__)


@api.route('/api/check_user', methods=['GET'])
def check_user():
    username = request.args.get('username')
    email = request.args.get('email')
    phone = request.args.get('phone')

    if not username or not email:
        return jsonify({'error': 'Username and email are required.'}), 400

    user = User.query.filter((User.username == username) | (User.email == email) | (User.phone == phone)).first()

    if user:
        return jsonify({
            'exists': True,
            'message': 'User already exists!'
        })
    else:
        return jsonify({
            'exists': False,
            'message': 'User does not exist.'
        })