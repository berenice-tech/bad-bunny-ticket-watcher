import requests
from bs4 import BeautifulSoup


VIP_URL = "https://www.ticketmaster.be/event/bad-bunny-debi-tirar-mas-fotos-world-tour-%7C-vip-packages-tickets/1339346645?language=fr-be"


PACKAGES_SURVEILLES = [
    "Early Entry Package",
    "Silver Premium Ticket Package",
    "Gold Premium Ticket Package"
]


def recuperer_vip():

    response = requests.get(
        VIP_URL,
        headers={
            "User-Agent": "Mozilla/5.0"
        },
        timeout=10
    )

    if response.status_code != 200:
        return []

    page = response.text

    billets = []

    for package in PACKAGES_SURVEILLES:

        if package in page:

            billets.append(
                {
                    "source": "Ticketmaster VIP",
                    "section": "VIP",
                    "package": package,
                    "prix": None,
                    "places": 1,
                    "url": VIP_URL
                }
            )

    return billets
