from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize the SQLAlchemy instance
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'e0ea551dbfa271000e46fbf8347a528d'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the db instance with the app
    db.init_app(app)

    with app.app_context():
        # Import models here to avoid circular import issues
        from pitstop.admin import models
        # Create all tables
        db.create_all()

    return app

# Create the app instance
app = create_app()