from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user
from pitstop.models.models import Service, Booking, Vehicle, TechnicianBooking, Technician
from pitstop.extensions import db
from pitstop.utils import send_custom_email, send_sms
from datetime import datetime
from pitstop.config import Config
import uuid

services = Blueprint('services', __name__)

@services.route('/services')
def service_list():
    """
    Displays a list of services booked by the current user.
    - Fetches bookings for the current user.
    - Joins related Service, TechnicianBooking, and Technician data.
    - Paginates the results to show 5 bookings per page.
    - Renders the 'services.html' template with the bookings.
    """

    if not current_user.is_authenticated:
        flash('You must first log in to access that page')
        return redirect(url_for('home.home_testing'))
    
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    page = request.args.get('page', 1, type=int)

    bookings = db.session.query(
        Booking.id,
        Booking.appointment_time,
        Booking.status,
        Service.name.label('service_name'),
        Technician.name.label('technician_name'),
        TechnicianBooking.comment.label('technician_comment')
    ).join(Service, Booking.service_id == Service.id)\
        .join(TechnicianBooking, TechnicianBooking.booking_id == Booking.id)\
            .join(Technician, Technician.id == TechnicianBooking.technician_id)\
                .filter(Booking.user_id == current_user.id)\
                    .order_by(Booking.id.desc())\
                        .paginate(page=page, per_page=5)


    return render_template('services.html', time=date, title='Portfolio project', bookings=bookings)

@services.route('/services/new', methods=['GET', 'POST'])
def service_request():
    """
    Handles the service request form.
    - On GET: Displays the form to request a new service.
    - On POST: Processes the form submission, creates a new booking, and assigns a technician.
    - Sends an email and SMS notification to the admin.
    """

    if not current_user.is_authenticated:
        flash('You must first log in to access that page')
        return redirect(url_for('home.home_testing'))
    
    if request.method == 'POST':
        vehicle_name = request.form.get('vehicle_id')
        service = request.form.get('service_id')
        description = request.form.get('description')
        appointment_time = request.form.get('appointment_time')

        # Check if service exists in the database
        service_type = Service.query.filter_by(name=service).first()
        if not service_type:
            service_type = Service(
                id=uuid.uuid4().hex,
                name=service,
                price=300.00
            )
            db.session.add(service_type)
            db.session.commit()



        # Check if the vehicle exists in the database
        vehicle_id = Vehicle.query.filter_by(make=vehicle_name).first()
        if not vehicle_id:
            flash('Selected vehicle does not exist.')
            return redirect(url_for('services.service_request'))
        
        # Create a new booking with the provided data
        new_booking = Booking(
            id=uuid.uuid4().hex,
            user_id=current_user.id,
            service_id=service_type.id,
            appointment_time=datetime.fromisoformat(appointment_time),
            status='Pending',
            description=description,
            vehicle_id=vehicle_id.id
        )
        # Add the new booking to the database session and commit it
        db.session.add(new_booking)
        
        '''
            THE BELOW CODE IS JUST FOR TESTING AND THE REAL IMPLEMENTATION OF FINDING
            THE REAL TECHNICIAN WILL BE IMPLEMENTED IN THE NEAR FUTURE - STAY TUNED
        '''
        tech = Technician.query.first()
        
        assign_tech = TechnicianBooking(
            id=uuid.uuid4().hex,
            technician_id=tech.id,
            booking_id=new_booking.id,
            comment='working on it!'
        )
        # Add the new tech to the database session and commit it
        db.session.add(assign_tech)
        '''
            THE ABOVE CODE IS JUST FOR TESTING AND THE REAL IMPLEMENTATION OF FINDING
            THE REAL TECHNICIAN WILL BE IMPLEMENTED IN THE NEAR FUTURE - STAY TUNED
        '''
        db.session.commit()
        message = f'''Greetings Admin,
A user {current_user.first_name} {current_user.last_name} has requested a service
for his vehicle {vehicle_id.make} {vehicle_id.model} and expects his service to be done by the date: {appointment_time}.

service: {service}
service description: {description}

contact information:
    Email: {current_user.email}
    Phone number: {current_user.phone}

Check your dashboard for more information about this.
Have a nice day!


'''
        # try:
        #     send_custom_email(
        #     subject='New Scheduled service',
        #     recipient=[Config.MAIL_USERNAME], # 🔐|📒 This is to be changed later when we have admins to our platform
        #     message=message
        #     )
        #     flash(f'{service} service scheduled')
        # except Exception as e:
        #     flash('An error occured. Please try again!')
        #     return redirect(url_for('services.service_request'))
        
        # # This function handles the errors, that's why it is not sorrounded with a try/except block
        # send_sms(message)
       
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
