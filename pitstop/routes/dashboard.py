from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import current_user

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/dashboard')
def dashboard_route():
    if not current_user.is_authenticated:
        flash('You must first log in to access the platform')
        return redirect(url_for('home.home_testing'))
    return render_template('dashboard.html', title="Portfolio project", user=current_user)
