from flask import Blueprint, render_template, jsonify, request, redirect, url_for
from flask_login import login_user, logout_user,login_required, current_user
from pitstop.models.models import User, Vehicle, Service, Booking, Technician, TechnicianBooking, Admin
from pitstop.extensions import bcrypt, db
from datetime import datetime

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

@routes.route('/services/new', methods=['GET', 'POST'])
def service_request():
    if request.method == 'POST':
        vehicle_name = request.form.get('vehicle_id')
        service = request.form.get('service_id')
        description = request.form.get('description')
        service_id = Service.query.filter_by(name=service).first()
        vehicle_id = Vehicle.query.filter_by(make=vehicle_name).first()
        appointment_time = request.form.get('appointment_time')
        print(vehicle_name)
        print(vehicle_id, service_id)
        # Create a new booking with the provided data
        new_booking = Booking(
            user_id=current_user.id,
            service_id=service_id.id,
            appointment_time=datetime.fromisoformat(appointment_time),
            status='Pending',
            description=description,
            vehicle_id=vehicle_id.id
        )
        
        # Add the new booking to the database session and commit it
        db.session.add(new_booking)
        db.session.commit()
        
        # Redirect to the dashboard after successful booking
        return redirect(url_for('routes.dashboard'))
    
    # Query the user's vehicles and all available services
    user_vehicles = Vehicle.query.filter_by(user_id=current_user.id).all()
    services = Service.query.all()
    
    # Render the service request template with user vehicles and services
    return render_template('service_request.html', title='Request a New Service', user=current_user, vehicles=user_vehicles, services=services)

@routes.route('/vehicles')
def vehicles():
    vehicles = Vehicle.query.filter_by(user_id=current_user.id)
    return render_template('vehicles.html', title='Portfolio Project', vehicles=vehicles)

@routes.route('/vehicles/new', methods=['GET', 'POST'])
def new_vehicle():
    if request.method == 'POST':
        vehicle = Vehicle(
            user_id=current_user.id,
            make=request.form.get('vehicle_brand'), 
            model=request.form.get('vehicle_model'),
            year=request.form.get('year'),
            type=request.form.get('type'),
            color=request.form.get('color'),
            license_plate=request.form.get('license_plate')
        )
        db.session.add(vehicle)
        db.session.commit()
        print('done')
        return redirect(url_for('routes.vehicles'))
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
    
@routes.route('/api/vehicles', methods=['GET'])
def get_vehicles():
    vehicles = Vehicle.query.all()
    vehicles_list = []
    for vehicle in vehicles:
        vehicle_data = {
            'id': vehicle.id,
            'user_id': vehicle.user_id,
            'make': vehicle.make,
            'model': vehicle.model,
            'year': vehicle.year,
            'type': vehicle.type,
            'color': vehicle.color,
            'license_plate': vehicle.license_plate
        }
        vehicles_list.append(vehicle_data)
    return jsonify(vehicles_list)


@routes.route('/all', methods=['GET'])
def display_all_json():
    users = User.query.all()
    vehicles = Vehicle.query.all()
    services = Service.query.all()
    bookings = Booking.query.all()
    technicians = Technician.query.all()
    admins = Admin.query.all()
    technician_bookings = TechnicianBooking.query.all()

    # Serialize data into JSON format using dict() constructor
    users_json = [dict(user.__dict__) for user in users]
    vehicles_json = [dict(vehicle.__dict__) for vehicle in vehicles]
    services_json = [dict(service.__dict__) for service in services]
    bookings_json = [dict(booking.__dict__) for booking in bookings]
    technicians_json = [dict(technician.__dict__) for technician in technicians]
    admins_json = [dict(admin.__dict__) for admin in admins]
    technician_bookings_json = [dict(tb.__dict__) for tb in technician_bookings]

    # Clean up unnecessary attributes from each dictionary
    for item in users_json + vehicles_json + services_json + bookings_json + technicians_json + admins_json + technician_bookings_json:
        item.pop('_sa_instance_state', None)  # Remove SQLAlchemy internal attribute

    # Combine all JSON data into a single dictionary
    data = {
        'users': users_json,
        'vehicles': vehicles_json,
        'services': services_json,
        'bookings': bookings_json,
        'technicians': technicians_json,
        'admins': admins_json,
        'technician_bookings': technician_bookings_json
    }

    return jsonify(data)

@routes.route('/database', methods=['GET'])
def display_database():
    # Fetch all entries from different tables
    users = User.query.all()
    vehicles = Vehicle.query.all()
    services = Service.query.all()
    bookings = Booking.query.all()
    technician_bookings = TechnicianBooking.query.all()
    
    return render_template('database.html', 
                           users=users, 
                           vehicles=vehicles, 
                           services=services, 
                           bookings=bookings, 
                           technician_bookings=technician_bookings)