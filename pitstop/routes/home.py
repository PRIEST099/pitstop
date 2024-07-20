from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import current_user

home = Blueprint('home', __name__)

@home.route('/')
def home_testing():
    """
    Handles the home page route.
    - Checks if the user is authenticated.
    - If the user is authenticated, redirects to the dashboard with a flash message.
    - If the user is not authenticated, renders the home page.
    """
    
    if current_user.is_authenticated:
        flash(f'You are already logged in as {current_user.username}')
        return redirect(url_for('dashboard.dashboard_route'))
    return render_template('home.html', title='Portfolio Project')
