from flask import Flask
from pitstop import config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_class=config.Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    db.init_app(app)

    with app.app_context():
        from pitstop.admin import models
        db.create_all()

    return app

app = create_app()