import os
from twilio.rest import Client
from dotenv import load_dotenv
import smtplib

load_dotenv()

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = "whatsapp:+14155238886"  # Twilio's Sandbox WhatsApp number
TWILIO_VERIFIED_WHATSAPP_NUMBER = f"whatsapp:{os.getenv('TWILIO_VERIFIED_WHATSAPP_NUMBER')}"
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")
SMTP_ADDRESS = os.getenv("SMTP_ADDRESS")


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

    def send_emails(self, emails, subject, message):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject: {subject}\n\n{message}"
                )
            
if __name__ == "__main__":
    print(TWILIO_SID)
    print(TWILIO_AUTH_TOKEN)