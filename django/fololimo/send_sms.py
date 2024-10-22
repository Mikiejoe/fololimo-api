import africastalking
from .models import SubCounty, Client
from decouple import config

username = "sandbox"
api_key = config("AFRICAS_TALKING_API_KEY")
africastalking.initialize(username, api_key)
sms = africastalking.SMS


def send_sms(location, message):
    sub_county = SubCounty.objects.filter(sub_county=location).first()
    if sub_county:
        clients = Client.objects.filter(location=sub_county.sub_county)
        try:
            response = sms.send(message, [client.phone for client in clients], sender_id="FOLOLIMO")
            print(response)
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        return "Location not found"


