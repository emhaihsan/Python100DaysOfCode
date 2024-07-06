import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = "whatsapp:+14155238886"  # Twilio's Sandbox WhatsApp number
TWILIO_VERIFIED_WHATSAPP_NUMBER = f"whatsapp:{os.getenv('TWILIO_VERIFIED_WHATSAPP_NUMBER')}"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    
    def send_whatsapp(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_WHATSAPP_NUMBER,
            to=TWILIO_VERIFIED_WHATSAPP_NUMBER
        )
        print(f"Message sent: {message.sid}")

if __name__ == "__main__":
    print(TWILIO_SID)
    print(TWILIO_AUTH_TOKEN)