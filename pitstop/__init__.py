from flask import Flask
from pitstop.config import Config
from pitstop.extensions import db, login_manager, mail

def create_app():
    """
    Factory function to create and configure the Flask application.
    Returns:
        app (Flask): Configured Flask application instance.
    """
    app = Flask(__name__)  # Create a Flask application instance
    app.config.from_object(Config)  # Load configuration from the Config object
    app.url_map.strict_slashes = False  # Disable strict slashes for URL routing

    # Initialize extensions with the application instance
    db.init_app(app)  # Initialize SQLAlchemy with the app
    login_manager.init_app(app)  # Initialize Flask-Login with the app
    mail.init_app(app)  # Initialize Flask-Mail with the app

    with app.app_context():
        db.create_all()  # Create database tables
    return app  # Return the configured app instance

