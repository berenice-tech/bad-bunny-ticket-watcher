import requests


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/126.0 Safari/537.36"
    )
}


TICKETSWAP_URL = "https://www.ticketswap.com/"


def recuperer_ticketswap():

    return [
        {
            "source": "TicketSwap",
            "section": "3D",
            "prix": 180,
            "places": 1,
            "url": "https://www.ticketswap.com/"
        }
    ]
