from twilio.rest import Client
from flask import current_app

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