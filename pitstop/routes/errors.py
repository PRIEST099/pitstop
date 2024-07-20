from flask import Blueprint, render_template

error = Blueprint('error', __name__)

@error.app_errorhandler(404)
def error_404(_):
    """
    Handles 404 errors (Page Not Found).
    - Renders a custom 404 error page when a page is not found.
    """
    return render_template('404.html', title='Page not found')