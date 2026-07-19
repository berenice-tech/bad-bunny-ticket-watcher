import os
import requests

from config import TICKETMASTER_EVENT_ID


API_KEY = os.environ.get("TICKETMASTER_API_KEY")


def recuperer_evenement():
    url = (
        "https://app.ticketmaster.com/"
        "discovery/v2/events/"
        f"{TICKETMASTER_EVENT_ID}.json"
    )

    params = {
        "apikey": API_KEY
    }

    response = requests.get(
        url,
        params=params,
        timeout=10
    )

    if response.status_code != 200:
        return {
            "erreur": response.status_code,
            "message": response.text
        }

    return response.json()


if __name__ == "__main__":
    evenement = recuperer_evenement()

    print("Nom :", evenement.get("name"))
    print("ID :", evenement.get("id"))

    print("\nInformations disponibles :")
    print(evenement.keys())
