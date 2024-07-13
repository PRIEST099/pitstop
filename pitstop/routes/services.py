from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user
from pitstop.models.models import Service, Booking, Vehicle
from pitstop.extensions import db
from datetime import datetime

services = Blueprint('services', __name__)

@services.route('/services')
def service_list():
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    bookings = db.session.query(
        Booking.id,
        Booking.description,
        Booking.appointment_time,
        Booking.status,
        Service.name.label('service_name')
    ).join(Service, Booking.service_id == Service.id).filter(Booking.user_id == current_user.id).order_by(Booking.id.desc()).all()

    return render_template('services.html', time=date, title='Portfolio project', bookings=bookings)

@services.route('/services/new', methods=['GET', 'POST'])
def service_request():
    if request.method == 'POST':
        vehicle_name = request.form.get('vehicle_id')
        service = request.form.get('service_id')
        description = request.form.get('description')
        service_id = Service.query.filter_by(name=service).first()
        vehicle_id = Vehicle.query.filter_by(make=vehicle_name).first()
        appointment_time = request.form.get('appointment_time')
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
        flash(f'{service} service scheduled')
        # Redirect to the dashboard after successful booking
        return redirect(url_for('dashboard.dashboard_route'))

    # Query the user's vehicles and all available services
    user_vehicles = Vehicle.query.filter_by(user_id=current_user.id).all()
    services = Service.query.all()

    # Try to pass service from dashboard
    spec_service = request.args.get('service')
    print(f'Spec value: {spec_service}')

    #requesting a vehicle maintenance from vehicles route
    spec_vehicle = request.args.get('vehicle') 

    # Render the service request template with user vehicles and services
    return render_template('service_request.html',
                           title='Request a New Service',
                           user=current_user,
                           vehicles=user_vehicles,
                           services=services,
                           spec_service=spec_service,
                           spec_vehicle=spec_vehicle)
