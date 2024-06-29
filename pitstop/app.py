from pitstop import app, db
from flask import jsonify
from pitstop.admin.models import User
from pitstop.client.forms.forms import OrderForm, LoginForm, RegisterForm, ContactForm
from flask import render_template

@app.route('/', methods=['GET', 'POST'])
def home():
    form = OrderForm()
    return render_template('homepage.html', title='Welcome - Pitstop', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Log in - Pitstop', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    return render_template('register.html', title='Join the Community', form=form)

@app.route('/support')
def contact():
    form = ContactForm()
    return render_template('contact.html', title='Support - Pitstop', form=form)

# Custom Error Handlers
@app.errorhandler(404)
def ErrorHandler(error):
    '''to be completed later'''

    return jsonify({None: 'None'}), 404

@app.errorhandler(500)
def internal_server_error(error):
    '''to be completed later'''

    return jsonify({None: 'None'}), 500

if __name__ == '__main__':
    app.run(debug=True)
