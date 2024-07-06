from flask import Blueprint, jsonify ,request, url_for
from pitstop.models.models import User
from pitstop.extensions import db, bcrypt

api = Blueprint('api', __name__)


@api.route('/api/status', methods=['GET'])
def status():
    return jsonify({'Status': 'Ok'}), 200

@api.route('/api/check_user', methods=['GET'])
def check_user():
    username = request.args.get('username')
    email = request.args.get('email')

    if not username or not email:
        return jsonify({'error': 'Username of email is required.'}), 400
    
    user = None

    if username:
        user = User.query.filter_by(username=username).first()
    elif email:
        user = User.query.filter_by(email=email).first()

    if user:
        return jsonify({
            'exists': True,
            'message': 'User already exists!'
        })
    else:
        return jsonify({
            'exists': False,
            'message': 'User does not exist.'})
    
@api.route('/api/check_login', methods=['GET'])
def check_login():
    email = request.args.get('email')
    password = request.args.get('password')
    if not email or not password:
        return jsonify({'error': 'username and password required!'})
    
    user = User.query.filter_by(email=request.args.get('email')).first()

    if user and bcrypt.check_password_hash(user.password, request.args.get('password')):
        return jsonify({'login': True}), 200
    return jsonify({'login': False}), 401
