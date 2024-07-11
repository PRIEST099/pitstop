from flask import Flask
from pitstop.config import Config
from pitstop.extensions import db, login_manager

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.url_map.strict_slashes = False

    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        db.create_all()
    return app
