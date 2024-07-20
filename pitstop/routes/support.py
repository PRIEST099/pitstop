from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_mail import Message
from flask_login import current_user
from pitstop.extensions import mail
from pitstop.config import Config
from pitstop.utils import send_sms

support = Blueprint('support', __name__)

@support.route('/support')
def support_route():
    """
    Renders the support page.
    - Displays the support page template.
    """

    return render_template('support.html')

@support.route('/support_response', methods=['GET', 'POST'])
def support_response():
    """
    Handles the support response process.
    - GET request: displays the support response form.
    - POST request: processes the form data and sends an email and SMS notification to the admin.
    """

    if request.method == 'POST':
        subject = request.form.get('subject')
        content = request.form.get('message')

        msg = Message(
            f'Pitsop user {current_user.username} has contacted you - regarding {subject}',
            sender='client@nonexistent.email', # ⚠️ This email does not exist
            recipients=[Config.TEST_EMAIL], # 🔐 I decided to make this email private in case some of you might want to mess with my inbox
            body=content)
        
        try:
            mail.send(msg)
            try:
                send_sms(Config.PHONE_NUMBER, 'someone just send an enquiry to the pitstop app') # 🔐 And again i have made my phone number private  due to obvious reasons
                print('\n\n\n\n\n\n\nmessage sent to sms')
            except Exception as e:
                print(f'\n\n\n\n\n\n\nmessage not sent: {e}')
        except Exception as e:
            flash('Failed to send message. Please try again later.', 'danger')
            return redirect(url_for('dashboard.dashboard_route'))

        return redirect(url_for('support.support_response'))

    return render_template('support_response.html', title='support | PITSTOP')
