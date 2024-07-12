from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from pitstop.models.models import User
from pitstop.extensions import bcrypt, db

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        flash(f'You are already logged in as {current_user.username}')
        return redirect(url_for('dashboard.dashboard_route'))
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        user_password = bcrypt.generate_password_hash(password).decode('utf-8')

        new_user = User(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=user_password
        )
        db.session.add(new_user)
        db.session.commit()
        flash('You can now login to access your account')
        return redirect(url_for('auth.login'))

    return render_template('register.html', title='Portfolio project')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash(f'Already loggen in as {current_user.username}')
        return redirect(url_for('dashboard.dashboard_route'))
    if request.method == 'GET':
        email = request.args.get('email')
        password = request.args.get('password')
        user = User.query.filter_by(email=email).first()


        if user is None and email is not None:
            flash('No Account found for that Email! Consider Registering')
            return redirect(url_for('auth.login'))
        

        if user:
            if bcrypt.check_password_hash(user.password, password):
                login_user(user, remember=True)
                flash(f'Logged in as {current_user.username}!')
                return redirect(url_for('dashboard.dashboard_route'))
            else:
                flash('incorect password')
                return redirect(url_for('auth.login'))
        
        
    return render_template('login.html', title="Portfolio project")

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home.home_testing'))
