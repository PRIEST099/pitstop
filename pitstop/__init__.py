from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from pitstop.config import Config
from pitstop.routes.routes import routes  # Import the blueprint from the correct file

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        db.create_all()
        # Create a new user insta

    app.register_blueprint(routes, url_prefix='/')  # Register the blueprint with a prefix

    return app
