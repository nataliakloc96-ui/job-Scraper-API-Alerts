import requests
import os

TELEGRAM_TOKEN = "8640982433:AAEleNJWJcfFAgL2M8rXh2BMWaCgvrHgUaU"
CHAT_ID = "8163340105"

def send_telegram(message: str):
    if not TELEGRAM_TOKEN or not CHAT_ID:
        return
    
        print("TELEGRAM TOKEN OR CHAT ID NOT SET")
        return

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

    response = requests.post(
        url,
        json = {
            "chat_id": CHAT_ID,
            "text": message
        }
    )
    print("TELEGRAM STATUS:", response.status_code)
    print("TELEGRAM RESPONSE:", response.text)