import os
import requests
from twilio.rest import Client

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
client = Client(account_sid, auth_token)

parameters = {
    "lat" : 23.2599,
    "lon" : 77.4126,
    "appid" : os.environ.get("API_ID"),
    "cnt" : 4
}

response = requests.get(url = "https://api.openweathermap.org/data/2.5/forecast", params = parameters)
response.raise_for_status()
data = response.json()

condition_codes = []

for i in range (0, 4):
    condition_codes.append(data["list"][i]["weather"][0]["id"])

for code in condition_codes:
    if int(code) < 700:
        message = client.messages.create(
            messaging_service_sid = os.environ.get("MESSAGING_SERVICE_ID"),
            body = 'It is going to rain today, Bring an umbrella.',
            to = os.environ.get("TO_PHONE_NUMBER"),
            from_ = os.environ.get("TWILIO_PHONE_NUMBER")
    )
        print(message.status)
        break