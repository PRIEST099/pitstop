from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import current_user

home = Blueprint('home', __name__)

@home.route('/')
def home_testing():
    if current_user.is_authenticated:
        flash(f'You are already logged in as {current_user.username}')
        return redirect(url_for('dashboard.dashboard_route'))
    return render_template('home.html', title='Portfolio Project')
