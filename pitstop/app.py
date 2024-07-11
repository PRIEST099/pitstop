from pitstop import create_app
from pitstop.routes import register_blueprints

app = create_app()
register_blueprints(app)

if __name__ == '__main__':
    app.run(debug=True)
