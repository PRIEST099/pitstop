from .auth import auth
from .home import home
from .services import services
from .vehicles import vehicles
from .dashboard import dashboard
from .support import support
from .api import api
from .test_user import test
from .errors import error

def register_blueprints(app):
    app.register_blueprint(auth)
    app.register_blueprint(home)
    app.register_blueprint(services)
    app.register_blueprint(vehicles)
    app.register_blueprint(dashboard)
    app.register_blueprint(support)
    app.register_blueprint(api)
    app.register_blueprint(test)
    app.register_blueprint(error)
