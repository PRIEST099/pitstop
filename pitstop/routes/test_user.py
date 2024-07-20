from flask import Blueprint, render_template, jsonify
from pitstop.models.models import User, Vehicle, Service, Booking, Technician, TechnicianBooking, Admin
#============= TEST API ==============#


test = Blueprint('test', __name__)



# This route is only uncommented in the development but we would not want sensitive information like this to be exposed to the internet ofcourse😂
# @test.route('/database', methods=['GET'])
# def display_database():
#     # Fetch all entries from different tables
#     users = User.query.all()
#     vehicles = Vehicle.query.all()
#     services = Service.query.all()
#     bookings = Booking.query.all()
#     technicians = Technician.query.all()
#     technician_bookings = TechnicianBooking.query.all()
#     return render_template('database.html', 
#                            users=users, 
#                            vehicles=vehicles, 
#                            services=services, 
#                            bookings=bookings, 
#                            technicians=technicians,
#                            technician_bookings=technician_bookings)

@test.route('/about')
def about():
    """
    Renders the 'about' page.
    - Displays the 'about.html' template with the title 'About'.
    """
    return render_template('about.html', title='About')