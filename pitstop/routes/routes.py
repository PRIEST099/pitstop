from flask import Blueprint, render_template, jsonify, request, redirect, url_for
from flask_login import login_user, logout_user, current_user
from pitstop.models.models import User
from pitstop.extensions import bcrypt, db

routes = Blueprint('routes', __name__)

@routes.route('/')
def home_testing():
    if current_user.is_authenticated:
        return redirect(url_for('routes.dashboard'))
    return render_template('home.html', title='Portfolio Project')

@routes.route('/dashboard')
def dashboard():
    if not current_user.is_authenticated:
        return redirect(url_for('routes.home_testing'))    
    return render_template('dashboard.html', title="Portfolio project", user=current_user)

@routes.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('routes.dashboard'))
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        user_password = bcrypt.generate_password_hash(password).decode('utf-8')

        new_user = User(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=user_password
            )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('routes.login'))



    return render_template('register.html', title='Portfolio project')

@routes.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('routes.dashboard'))
    if request.method == 'GET':
        email = request.args.get('email')
        password = request.args.get('password')

        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user, remember=True)
            return redirect(url_for('routes.dashboard'))
    return render_template('login.html', title="Portfolio project")

@routes.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('routes.home_testing'))

@routes.route('/request')
def service_request():
    return render_template('service_request.html', title='Portfolio Project')

@routes.route('/vehicles')
def vehicles():
    return render_template('vehicles.html', title='Portfolio Project')

@routes.route('/vehicles/new', methods=['GET', 'POST'])
def new_vehicle():
    return render_template('new_vehicle.html', title="Portffolio project")

@routes.route('/services')
def services():
    services = [
        {
            'id': 1,
            'type': 'Oil Change',
            'description': 'Full synthetic oil change',
            'date_requested': '2024-06-01',
            'estimated_completion': '2024-06-02',
            'status': 'In Progress',
            'mechanic': 'John Doe'
        },
        {
            'id': 2,
            'type': 'Tire Replacement',
            'description': 'Replacing all four tires',
            'date_requested': '2024-06-10',
            'estimated_completion': '2024-06-11',
            'status': 'Pending',
            'mechanic': 'Jane Smith'
        },
        {
            'id': 2,
            'type': 'Tire Replacement',
            'description': 'Replacing all four tires',
            'date_requested': '2024-06-10',
            'estimated_completion': '2024-06-11',
            'status': 'Pending',
            'mechanic': 'Jane Smith'
        },
        {
            'id': 2,
            'type': 'Tire Replacement',
            'description': 'Replacing all four tires',
            'date_requested': '2024-06-10',
            'estimated_completion': '2024-06-11',
            'status': 'Pending',
            'mechanic': 'Jane Smith'
        }
    ]
    return render_template('services.html', services=services, title='Portfolio project')



#============= TEST API ==============#

@routes.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    users_list = []
    for user in users:
        user_data = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'firstname': user.first_name,
            'lastname': user.last_name,
            'password': user.password
        }
        users_list.append(user_data)
    return jsonify(users_list)
