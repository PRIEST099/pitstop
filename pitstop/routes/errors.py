from flask import Blueprint, render_template

error = Blueprint('error', __name__)

@error.app_errorhandler(404)
def error_404(_):
    return render_template('404.html', title='Page not found')