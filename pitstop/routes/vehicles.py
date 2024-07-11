from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user
from pitstop.models.models import Vehicle
from pitstop.extensions import db

vehicles = Blueprint('vehicles', __name__)

@vehicles.route('/vehicles')
def vehicle_list():
    vehicles = Vehicle.query.filter_by(user_id=current_user.id)
    return render_template('vehicles.html', title='Portfolio Project', vehicles=vehicles)

@vehicles.route('/vehicles/new', methods=['GET', 'POST'])
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
        flash(f'{request.form.get("vehicle_brand")} {request.form.get("vehicle_model")} successfully added!')
        return redirect(url_for('vehicles.vehicle_list'))
    return render_template('new_vehicle.html', title="Portfolio project")
