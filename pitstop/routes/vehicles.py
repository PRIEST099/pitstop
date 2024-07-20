from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user
from pitstop.models.models import Vehicle, Booking
from pitstop.extensions import db
from pitstop.config import Config
import uuid

vehicles = Blueprint('vehicles', __name__)

@vehicles.route('/vehicles')
def vehicle_list():
    """
    Renders the list of vehicles for the current user.
    - Queries vehicles belonging to the current user.
    - Renders the 'vehicles.html' template with the list of vehicles.
    """

    vehicles = Vehicle.query.filter_by(user_id=current_user.id)
    return render_template('vehicles.html', title='Portfolio Project', vehicles=vehicles)

@vehicles.route('/vehicles/new', methods=['GET', 'POST'])
def new_vehicle():
    """
    Handles the addition of a new vehicle.
    - On GET: Renders the 'new_vehicle.html' template for adding a new vehicle.
    - On POST: Processes the form data to add a new vehicle.
    """

    if request.method == 'POST':
        plate = request.form.get('license_plate')

        exists = Vehicle.query.filter_by(license_plate=plate).first()

        if exists:
            flash('That car is already managed by another user!')
        else:
            vehicle = Vehicle(
                id=uuid.uuid4().hex,
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
            flash(f'{request.form.get("vehicle_brand")} {request.form.get("vehicle_model")} successfully added!')
            return redirect(url_for('vehicles.vehicle_list'))
    return render_template('new_vehicle.html', title="Portfolio project")


@vehicles.route('/vehicle/<string:vehicle_id>', methods=['GET'])
def delete_vehicle(vehicle_id):
    """
    Handles the deletion of a vehicle.
    - Finds the vehicle by ID.
    - Updates bookings associated with the vehicle to indicate deletion.
    - Deletes the vehicle from the database.
    """

    vehicle = Vehicle.query.get_or_404(vehicle_id)
    booking = Booking.query.filter_by(vehicle_id=vehicle.id).all()
    for order in booking:
        order.vehicle_id = f'Was owned by {current_user.first_name} {current_user.last_name}'
        order.status = 'vehicle deleted'
        order.technician_bookings.comment = 'repair cancelled'
    db.session.delete(vehicle)
    db.session.commit()
    return redirect(url_for('vehicles.vehicle_list'))
