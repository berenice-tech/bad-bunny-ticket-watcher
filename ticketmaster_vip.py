import requests

VIP_URL = "https://www.ticketmaster.be/event/bad-bunny-debi-tirar-mas-fotos-world-tour-%7C-vip-packages-tickets/1339346645?language=fr-be"


PACKAGES_SURVEILLES = [
    "Early Entry Package",
    "Silver Premium Ticket Package",
    "Gold Premium Ticket Package"
]


PRIX_CONNUS = {
    "Early Entry Package": 258.58,
    "Silver Premium Ticket Package": 298.58,
    "Gold Premium Ticket Package": 353.58
}


def recuperer_vip():

    billets = []

    for package in PACKAGES_SURVEILLES:

        billets.append(
            {
                "source": "Ticketmaster VIP",
                "section": "VIP",
                "package": package,
                "prix": PRIX_CONNUS[package],
                "places": 1,
                "url": VIP_URL
            }
        )

    return billets
