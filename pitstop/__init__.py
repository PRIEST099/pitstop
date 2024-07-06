from flask import Flask
from pitstop.config import Config
from pitstop.extensions import db, login_manager
from pitstop.routes.routes import routes
from pitstop.routes.api.network import api

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(routes, url_prefix='/')
    app.register_blueprint(api, url_prefix='/')

    return app
