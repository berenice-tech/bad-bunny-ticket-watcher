import requests


EVENT_URL = (
    "https://www.ticketmaster.be/"
    "artist/bad-bunny-tickets/979454"
    "?language=fr-be"
)


def verifier_ticketmaster():
    try:
        response = requests.get(
            EVENT_URL,
            timeout=10,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        if response.status_code == 200:
            return {
                "source": "Ticketmaster",
                "status": "accessible",
                "message": "Page événement accessible"
            }

        else:
            return {
                "source": "Ticketmaster",
                "status": "erreur",
                "code": response.status_code
            }

    except Exception as e:
        return {
            "source": "Ticketmaster",
            "status": "erreur",
            "message": str(e)
        }


if __name__ == "__main__":
    resultat = verifier_ticketmaster()
    print(resultat)
