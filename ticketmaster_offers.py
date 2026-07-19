import os
import requests

from config import TICKETMASTER_EVENT_ID


API_KEY = os.environ.get("TICKETMASTER_API_KEY")


def recuperer_offres():
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

    data = response.json()

    result = {
        "nom": data.get("name"),
        "url": data.get("url"),
        "priceRanges": data.get("priceRanges"),
        "ticketing": data.get("ticketing"),
    }

    return result


if __name__ == "__main__":
    print(recuperer_offres())
