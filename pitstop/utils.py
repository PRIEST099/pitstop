from twilio.rest import Client
from flask import current_app, url_for
from pitstop.extensions import mail
from flask_mail import Message
import phonenumbers
from phonenumbers import PhoneNumberFormat, parse, PhoneNumberType

def send_sms(to, message):
    account_sid = current_app.config['TWILIO_ACCOUNT_SID']
    auth_token = current_app.config['TWILIO_AUTH_TOKEN']
    twilio_phone_number = current_app.config['TWILIO_PHONE_NUMBER']

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=message,
        from_=twilio_phone_number,
        to=to
    )
    return message.sid

def format_phone_number(phone_number):
    try:
        # Parse the phone number
        parsed_number = parse(phone_number, "RW")

        # Check if the number is valid and of the correct type for Rwanda
        if phonenumbers.is_valid_number(parsed_number) and phonenumbers.number_type(parsed_number) == PhoneNumberType.MOBILE:
            # Format the phone number to international format for Rwanda
            formatted_number = phonenumbers.format_number(parsed_number, PhoneNumberFormat.INTERNATIONAL)
            return formatted_number
        else:
            return f"Invalid or not a mobile number in Rwanda: {phone_number}"
    except phonenumbers.phonenumberutil.NumberParseException as e:
        print(f"Error parsing phone number: {e}")
        return None
    

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message(
        'Password Reset Request',
        sender='noreply@pitstop.com',
        recipients=[user.email]
    )
    msg.body = f'''Hello {user.first_name},
To reset your password, follow the folowing link:
{url_for('auth.reset_password', token=token, _external=True)}

If you did not make this request, simply ignore this email and no changes will be made
'''
    mail.send(msg)