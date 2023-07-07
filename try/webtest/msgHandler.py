from django.conf import settings
from twilio.rest import Client

class messageHandler():
    phone_number = None
    otp = None
    def __init__(self, phone_number, otp) -> None:
        self.phone_number = phone_number
        self.otp = otp

    def send_otp_on_phone():
        client = Client(settings.ACCOUNT_SID, settings.AUTH_TOKEN)

        message = client.messages.create(
                              body='Hi there',
                              from_='+15017122661',
                              to='+15558675310'
                          )
        