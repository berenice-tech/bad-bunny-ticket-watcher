import os
import requests

from alerts import creer_message


TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")


def envoyer_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": message
    }

    response = requests.post(url, data=data)

    return response.json()


if __name__ == "__main__":

    message = creer_message(
        niveau="🟢 PRIORITÉ",
        source="Ticketmaster",
        section="3D",
        prix=145,
        places=1,
        score=15
    )

    resultat = envoyer_telegram(message)

    print(resultat)
