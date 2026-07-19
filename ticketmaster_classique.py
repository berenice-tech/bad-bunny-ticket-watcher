CLASSIQUE_URL = "https://www.ticketmaster.be/event/bad-bunny-debi-tirar-mas-fotos-world-tour-tickets/1117180915?language=fr-be"


SECTIONS_PRIORITAIRES = [
    "3D",
    "3C",
    "3A",
    "Golden"
]


def recuperer_classique():

    billets = []

    # Version initiale de connexion du flux classique
    # Les vraies disponibilités seront branchées ensuite

    billets.append(
        {
            "source": "Ticketmaster",
            "section": "3D",
            "prix": 145,
            "places": 1,
            "url": CLASSIQUE_URL
        }
    )

    return billets
