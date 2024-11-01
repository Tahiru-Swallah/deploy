from django.conf import settings
from twilio.rest import Client

def send_sms(user_code, phone_number, user):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    sms = client.messages.create(
        body = f'Hi {user}! your verification is {user_code}',
        from_ = '+12567436079',
        to= f'+233595467122'
    )

    print(sms.sid)