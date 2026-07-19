import os
import requests


API_KEY = os.environ.get("TICKETMASTER_API_KEY")


def rechercher_bad_bunny():
    url = "https://app.ticketmaster.com/discovery/v2/events.json"

    params = {
        "apikey": API_KEY,
        "keyword": "Bad Bunny",
        "city": "Brussels",
        "countryCode": "BE",
        "size": 5
    }

    response = requests.get(url, params=params, timeout=10)

    if response.status_code != 200:
        return {
            "erreur": response.status_code,
            "message": response.text
        }

    data = response.json()

    evenements = []

    for event in data.get("_embedded", {}).get("events", []):
        evenements.append({
            "nom": event.get("name"),
            "date": event.get("dates", {})
            .get("start", {})
            .get("localDate"),
            "id": event.get("id")
        })

    return evenements


if __name__ == "__main__":
    resultat = rechercher_bad_bunny()
    print(resultat)
