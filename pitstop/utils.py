from pitstop.extensions import mail
from flask_mail import Message
import phonenumbers
from phonenumbers import PhoneNumberFormat, parse, PhoneNumberType
import vonage
from pitstop.config import Config

def send_sms(text):
    client = vonage.Client(key=Config.VONAGE_KEY, secret=Config.VONAGE_SECRET)

    sms = vonage.Sms(client)

    try:
        responseData = sms.send_message(
            {
            "from": "Vonage APIs",
            "to": "250789108997",
            "text": text,
            }
            )

        if responseData["messages"][0]["status"] == "0":
            print("Message sent successfully.")
        else:
            print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
    except Exception as e:
        print(f'error: {e}')

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
    




def send_custom_email(subject, recipient, message):
    
    msg = Message(
        subject,
        sender='noreply@pitstop.rw',
        recipients=recipient,
        body=message
    )
    mail.send(msg)