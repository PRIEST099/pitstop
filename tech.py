#!/usr/bin/python3

from pitstop import db, create_app
from pitstop.models.models import Technician
from pitstop.utils import format_phone_number
import uuid

app = create_app()

# another testing technique to add a technician to the database
with app.app_context():
    t1 = Technician(id=uuid.uuid4().hex,
                    name="ABC garage ltd",
                    rating=4.5,
                    status="available",
                    phone=format_phone_number('789108997'),
                    email='cyizereahadi@gmail.com')
    db.session.add(t1)
    db.session.commit()
    print('technicians added successfully!')