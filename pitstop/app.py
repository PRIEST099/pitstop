from pitstop import create_app
from pitstop.routes import register_blueprints
from pitstop.models.models import User, Vehicle
from pitstop.config import Config

app = create_app()
register_blueprints(app)


