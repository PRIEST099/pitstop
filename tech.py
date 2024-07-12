#!/usr/bin/python3

from pitstop import db, create_app
from pitstop.models.models import Technician

app = create_app()

with app.app_context():
    t1 = Technician(name="ABC garage ltd", rating=4.5, status="available")
    t2 = Technician(name="Ahadi tech", rating=4.7, status="available")
    db.session.add(t1)
    db.session.add(t2)
    db.session.commit()
    print('technicians added successfully!')