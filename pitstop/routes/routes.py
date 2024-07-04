from flask import Blueprint, render_template, jsonify

routes = Blueprint('routes', __name__)

@routes.route('/')
def home_testing():
    return render_template('home.html', title='Portfolio Project')

@routes.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', title="Portfolio project")

@routes.route('/register')
def register():
    return render_template('register.html', title='Portfolio project')

@routes.route('/login')
def login():
    return render_template('login.html', title="Portfolio project")

@routes.route('/request')
def service_request():
    return render_template('service_request.html', title='Portfolio Project')

@routes.route('/vehicles')
def vehicles():
    return render_template('vehicles.html', title='Portfolio Project')

@routes.route('/vehicles/new')
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





# test database !!!!!!! to be deleted after testing !!!!!!!

'''@routes.route('/admin')
def admin():
    users = User.query.all()
    users_list = []
    for user in users:
        user_data = {
            'id': user.id,
            'username': user.username,
            'email': user.email
            # Add other fields if needed
        }
        users_list.append(user_data)
    return jsonify(users_list)'''