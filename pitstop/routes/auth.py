# Import necessary modules from Flask and other packages
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user
from pitstop.models.models import User
from pitstop.extensions import bcrypt, db
from pitstop.utils import format_phone_number, send_custom_email
import uuid

# Create a Blueprint for authentication-related routes
auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handles the user registration process. 
    - GET request: displays the registration form.
    - POST request: processes the form data to register a new user.
    """

    if current_user.is_authenticated:
        flash(f'You are already logged in as {current_user.username}')
        return redirect(url_for('dashboard.dashboard_route'))
    
    if request.method == 'POST':
        # Retrieves data from the request
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        phone = request.form.get('phone_number')

        # Hash user password
        user_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Creating a new user object
        new_user = User(
            id=uuid.uuid4().hex,
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            phone=format_phone_number(phone),
            password=user_password
        )

        # Add the new user to the database and commit the changes
        db.session.add(new_user)
        db.session.commit()

        # Notify the user and redirect to the login page
        flash('You can now login to access your account')
        return redirect(url_for('auth.login'))

    # Render the registration form template
    return render_template('register.html', title='Portfolio project')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handles the user login process.
    - GET request: processes login data and attempts authentication.
    - POST request: handles the actual login process.
    """

    if current_user.is_authenticated:
        flash(f'Already loggen in as {current_user.username}')
        return redirect(url_for('dashboard.dashboard_route'))
    

    if request.method == 'GET':
        # Redirects already logged-in users to the dashboard
        email = request.args.get('email')
        password = request.args.get('password')
        remember = request.args.get('remember')

        # Find the user by email
        user = User.query.filter_by(email=email).first()


        if user is None and email is not None:
            # checks if there is nouser in the database but they have entered the email on their end
            flash('No Account found for that Email! Consider Registering')
            return redirect(url_for('auth.login'))
        

        if user:
            if bcrypt.check_password_hash(user.password, password):
                # Log the user in and redirect to the dashboard
                login_user(user, remember=remember)
                flash(f'Logged in as {current_user.username}!')
                return redirect(url_for('dashboard.dashboard_route'))
            else:
                flash('incorect password')
                return redirect(url_for('auth.login'))
        
    # Rendering the login page Template
    return render_template('login.html', title="Portfolio project")

@auth.route('/logout')
def logout():
    """
    Logs out the current user and redirects to the home page.
    """
    logout_user()
    return redirect(url_for('home.home_testing'))



@auth.route('/login/forgot_password', methods=['GET', 'POST'])
def reset_request():
    """
    Handles password reset requests.
    - GET request: displays the password reset request form.
    - POST request: processes the form data and sends a password reset email if the email is associated with a user.
    """

    if request.method == 'POST':
        email = request.form.get('email')
        user = User.query.filter_by(email=email).first()
        if user is not None:
            token  = user.get_reset_token()
            message = f'''Hello {user.first_name},
To reset your password, follow the folowing link:
{url_for('auth.reset_password', token=token, _external=True)}

If you did not make this request, simply ignore this email and no changes will be made.
'''
            send_custom_email(
                subject='Password Reset Request',
                recipient=[user.email],
                message=message
            )
            flash('An Email has been sent with instructions to reset your password.')
            return redirect(url_for('auth.login'))
        else:
            flash('Email not found in our database', 'danger')
    return render_template('reset_request.html', title='Forgot password | PITSTOP')


@auth.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    """
    Handles the password reset process.
    - GET request: verifies the reset token and displays the password reset form.
    - POST request: processes the new password and updates it if valid.
    """

    user = User.verify_reset_token(token)

    if request.method == 'POST':
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if password != confirm_password:
            flash('Paswords must match')

        else:
            # Update the user's password and commit the changes
            user_password = bcrypt.generate_password_hash(password).decode('utf-8')
            user.password = user_password
            db.session.commit()
            flash('Your password has been updated, You are now able to log in')
            return redirect(url_for('auth.login'))

    if request.method == 'GET':
        if not user:
            flash('That is an Invalid or Expired token')
            return redirect(url_for('auth.reset_request'))
        
    # REndering the page template
    return render_template('reset_password.html', title='Reset password')

