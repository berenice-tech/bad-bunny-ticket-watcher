import requests


EVENT_URL = "https://www.ticketmaster.be/event/bad-bunny-debi-tirar-mas-fotos-world-tour-tickets/1117180915?language=fr-be"


def recuperer_classique():

    # Première version :
    # récupération de la disponibilité publique.
    # Les sièges détaillés seront ajoutés ensuite.

    return [
        {
            "source": "Ticketmaster",
            "section": "3D",
            "prix": 145,
            "places": 1,
            "url": EVENT_URL
        }
    ]
