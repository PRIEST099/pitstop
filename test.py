#!/usr/bin/python3
from pitstop import create_app, db
from pitstop.models.models import User

app = create_app()

with app.app_context():
    existing_user = User.query.filter_by(username='ahadi').first()
    if existing_user:
        print('Test user already exists!')
    else:
        test_user = User(
            first_name = 'Ahadi',
            last_name = 'CYIZERE',
            username='ahadi',
            email='test@test.com',
            password='test'
        )
        db.session.add(test_user)
        db.session.commit()
        print('Test user added successfully!')
