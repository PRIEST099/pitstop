from flask import Blueprint, render_template

support = Blueprint('support', __name__)

@support.route('/support')
def support_route():
    return render_template('support.html')
