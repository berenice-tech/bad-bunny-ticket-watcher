import os
import requests

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

def envoyer_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message
    }

    response = requests.post(url, data=data)

    print("Réponse Telegram :")
    print(response.text)

if __name__ == "__main__":
    envoyer_message("🎟️ Bad Bunny Ticket Watcher connecté !")
