#!/usr/bin/python3

from pitstop import create_app, db
from pitstop.models.models import Vehicle, User
from pitstop.config import Config

app = create_app()

with app.app_context():
    user = User.query.filter_by(id=Config.DEFAULT_USER_ID).first()

    if not user:
        default_user = User(
            id=Config.DEFAULT_USER_ID,
            first_name='default',
            last_name='user',
            username='defaultusername',
            email='pistopdefaultuser@test.com',
            phone=1234567891011,
            password=Config.DEFAULT_USER_ID,
        )

        db.session.add(default_user)
        db.session.commit()

    vehicle = Vehicle.query.filter_by(id=Config.DEFAULT_VEHICLE_ID).first()

    if not vehicle:
        default_vehicle = Vehicle(
            id=Config.DEFAULT_VEHICLE_ID,
            user_id=Config.DEFAULT_USER_ID,
            make='default',
            model='vehicle',
            year=2024,
            type='default type',
            color='default to invisible',
            license_plate='ABCAHADIDEVELOPER'
        )
        db.session.add(default_vehicle)
        db.session.commit()
    print('setup complete')
    
