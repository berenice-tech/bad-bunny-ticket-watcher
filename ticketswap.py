import requests


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/126.0 Safari/537.36"
    )
}


TICKETSWAP_URL = (
    "https://www.ticketswap.com/concert-tickets/"
    "bad-bunny-brussels-stade-roi-baudouin-koning-boudewijnstadion-2026-07-22-TLrKbppcDpCXt8cEGjw1bC"
)


def recuperer_ticketswap():

    try:

        response = requests.get(
            TICKETSWAP_URL,
            headers=HEADERS,
            timeout=10
        )

        if response.status_code != 200:
            print("TicketSwap inaccessible :", response.status_code)
            return []


        contenu = response.text.lower()


        if "available" in contenu or "billet" in contenu or "ticket" in contenu:

            return [
                {
                    "source": "TicketSwap",
                    "section": "Disponible",
                    "prix": 0,
                    "places": 1,
                    "url": TICKETSWAP_URL
                }
            ]


    except Exception as e:

        print("Erreur TicketSwap :", e)


    return []
