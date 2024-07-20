from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import current_user

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/dashboard')
def dashboard_route():
    """
    Handles the display of the dashboard page.
    - Checks if the user is authenticated.
    - If the user is not authenticated, redirects to the home page with a flash message.
    - If the user is authenticated, renders the dashboard page.
    """
    
    if not current_user.is_authenticated:
        flash('You must first log in to access the platform')
        return redirect(url_for('home.home_testing'))
    return render_template('dashboard.html', title="Portfolio project", user=current_user)
