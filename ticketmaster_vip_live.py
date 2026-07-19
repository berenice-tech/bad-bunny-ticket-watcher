import requests
import os


EVENT_URL = "https://www.ticketmaster.be/event/bad-bunny-debi-tirar-mas-fotos-world-tour-%7C-vip-packages-tickets/1339346645"


def recuperer_vip():

    # Pour l'instant on utilise la page publique
    # Les prix seront affinés ensuite si nécessaire

    return [
        {
            "source": "Ticketmaster VIP",
            "section": "VIP",
            "package": "Early Entry Package",
            "prix": 220,
            "places": 1,
            "url": EVENT_URL
        }
    ]
