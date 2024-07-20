from pitstop import db, create_app
from pitstop.models.models import Service
import uuid

# 📒 ist of sample services to be added just for testing the app
# im sure this will change in the near future
services = [
    'Oil Change', 'Tire Rotation', 'Brake Inspection', 'Transmission Repair', 'Battery Replacement',
    'Engine Diagnostics', 'Air Filter Replacement', 'AC Service', 'Alignment Check', 'Coolant Flush',
    'Spark Plug Replacement', 'Fuel System Cleaning', 'Exhaust System Repair', 'Suspension Repair',
    'Radiator Service', 'Timing Belt Replacement', 'Windshield Repair', 'Headlight Replacement', 
    'Wiper Blade Replacement', 'Clutch Repair', 'Shock and Strut Replacement', 'Muffler Repair',
    'Steering Repair', 'Starter Replacement', 'Alternator Replacement', 'Drive Belt Replacement', 
    'Power Steering Service', 'Differential Service', 'Transfer Case Service', 'Fuel Pump Replacement',
    'Axle Replacement', 'Wheel Balancing', 'Drivetrain Repair', 'Valve Adjustment', 'Emission Test', 
    'Throttle Body Service', 'Glow Plug Replacement', 'Turbocharger Service', 'EGR Valve Cleaning', 
    'Cylinder Head Repair', 'Diesel Particulate Filter Service', 'Car Wash', 'Interior Cleaning',
    'Exterior Detailing', 'Paint Touch-Up', 'Rust Proofing', 'Upholstery Repair', 'Leather Treatment',
    'Convertible Top Repair', 'Window Tinting'
]
app = create_app()
# Ensure database session is open
with app.app_context():
    for service_name in services:
        service = Service(
            id=uuid.uuid4().hex,
            name=service_name,
            price=300.00)
        db.session.add(service)

    # Commit the session
    db.session.commit()

print("50 services have been added to the database.")

