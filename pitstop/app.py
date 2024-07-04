from pitstop import app
from flask import render_template

@app.route('/')
def home_testing():
    return render_template('dashboard.html', title='Portfolio Project')

@app.route('/request')
def service_request():
    return render_template('service_request.html', title='Portfolio Project')

@app.route('/vehicles')
def vehicles():
    return render_template('vehicles.html', title='Portfolio Project')

@app.route('/services')
def services():
    return render_template('services.html', title='Portfolio Project')


if __name__ == '__main__':
    app.run(debug=True)
