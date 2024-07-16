from flask import Blueprint, render_template, jsonify
from pitstop.models.models import User, Vehicle, Service, Booking, Technician, TechnicianBooking, Admin
#============= TEST API ==============#


test = Blueprint('test', __name__)

@test.route('/api/users', methods=['GET'])
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
    
@test.route('/api/vehicles', methods=['GET'])
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


@test.route('/about')
def about():
    return render_template('about.html', title='About')