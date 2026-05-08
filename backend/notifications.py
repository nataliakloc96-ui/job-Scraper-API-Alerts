<<<<<<< HEAD
import requests
import os

TELEGRAM_TOKEN = "8640982433:AAEleNJWJcfFAgL2M8rXh2BMWaCgvrHgUaU"
CHAT_ID = "8163340105"

def send_telegram(message: str):

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

    response = requests.post(
        url,
        json = {
            "chat_id": CHAT_ID,
            "text": message
        }
    )
    print("TELEGRAM STATUS:", response.status_code)
=======
import requests
import os

TELEGRAM_TOKEN = "8640982433:AAEleNJWJcfFAgL2M8rXh2BMWaCgvrHgUaU"
CHAT_ID = "8163340105"

def send_telegram(message: str):

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

    response = requests.post(
        url,
        json = {
            "chat_id": CHAT_ID,
            "text": message
        }
    )
    print("TELEGRAM STATUS:", response.status_code)
>>>>>>> d23084533f23a819d73ec70629333fa77bfec141
    print("TELEGRAM RESPONSE:", response.text)