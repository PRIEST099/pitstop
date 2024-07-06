#!/usr/bin/pytho3
from flask_login import UserMixin
from pitstop.extensions import db, login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

'''
database models used in this project
'''
class User(db.Model, UserMixin):
    '''
        Represents the users of the system.
        Each can have multiple vehivles ad bookings
    '''

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(16), nullable=False)
    vehicle_info = db.relationship('Vehicle', backref='owner', lazy=True)
    booking = db.relationship('Booking', backref='user', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"



# Vehicle table
class Vehicle(db.Model):
    '''
        Represents the vehicles associated with users.
        Each vehicle has a 'user_id' as a foreign key to 'User' table
    '''

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    make = db.Column(db.String(80), nullable=False)
    model = db.Column(db.String(80), nullable=False)
    year = db.Column(db.String(4), nullable=False)
    type = db.Column(db.String(20), nullable=False)
    color = db.Column(db.String(20), nullable=True)
    license_plate = db.Column(db.String(20), unique=True, nullable=False)

# Service table
class Service(db.Model):
    '''
        Represets The services offered.
        Each service can have multiple bookinngs
    '''

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    bookings = db.relationship('Booking', backref='service', lazy=True)

#Booking table
class Booking(db.Model):
    '''
        Represents orders made by users specific services.
        It includes foreign keys to both user and service tables
    '''

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    appointment_time = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(80), nullable=False)
    technician_bookings = db.relationship('TechnicianBooking', backref='booking', lazy=True)


#  Technician table
class Technician(db.Model):
    '''
        Represents Technicians who are assigned to bookings
    '''

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    status = db.Column(db.String(80), nullable=False)
    technician_bookings = db.relationship('TechnicianBooking', backref='technician', lazy=True)


# Admin table
class Admin(db.Model):
    '''
        Represents admin user with access to administratice privileges
    '''

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


# teck=hnician booking
class TechnicianBooking(db.Model):
    '''
        Represents the relationship between technicians and bookings,
        allowing for the assignment of technicians to specific boookings
    '''
    id = db.Column(db.Integer, primary_key=True)
    technician_id = db.Column(db.Integer, db.ForeignKey('technician.id'), nullable=False)
    booking_id = db.Column(db.Integer, db.ForeignKey('booking.id'), nullable=False)
