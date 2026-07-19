import requests
import os


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/126.0 Safari/537.36"
    )
}



API_KEY = os.environ.get("TICKETMASTER_API_KEY")

EVENT_ID = "Z698xZG2Z16v79kZ04"

CLASSIQUE_URL = (
    "https://www.ticketmaster.be/event/"
    "bad-bunny-debi-tirar-mas-fotos-world-tour-tickets/1117180915"
    "?language=fr-be"
)


def recuperer_classique():

    billets = []

    url = (
        f"https://app.ticketmaster.com/"
        f"discovery/v2/events/{EVENT_ID}"
    )

    params = {
        "apikey": API_KEY,
        "locale": "fr-be"
    }

    print(
        "Clé API présente :",
        bool(API_KEY)
    )

    response = requests.get(
        url,
        params=params,
        headers=HEADERS,
        timeout=10
    )
        

    if response.status_code != 200:

        print(
            "Erreur Ticketmaster API :",
            response.status_code
        )

        return billets


    evenement = response.json()


    # Vérifie si Ticketmaster indique une vente active

    dates = evenement.get("dates", {})

    statut = dates.get(
        "status",
        {}
    ).get(
        "code"
    )


    if statut != "onsale":

        return billets


    # L'API Discovery ne donne pas toujours les sièges/prix.
    # On renvoie donc seulement l'événement actif pour validation.

    billets.append(
        {
            "source": "Ticketmaster",
            "section": "Disponibilité détectée",
            "prix": "Voir Ticketmaster",
            "places": 1,
            "url": CLASSIQUE_URL
        }
    )


    return billets

if __name__ == "__main__":

    resultats = recuperer_classique()

    print("Résultat Ticketmaster classique :")
    print(resultats)
