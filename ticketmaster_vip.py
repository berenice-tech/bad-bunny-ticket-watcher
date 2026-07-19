import requests

from config import TICKETMASTER_VIP_EVENT_ID


VIP_URL = (
    "https://www.ticketmaster.be/event/"
    "bad-bunny-debi-tirar-mas-fotos-world-tour-%7C-vip-packages-tickets/"
    "1339346645?language=fr-be"
)


def verifier_vip():

    try:
        response = requests.get(
            VIP_URL,
            headers={
                "User-Agent": "Mozilla/5.0"
            },
            timeout=10
        )

        return {
            "status": response.status_code,
            "taille_page": len(response.text),
            "contient_bad_bunny": "Bad Bunny" in response.text,
            "contient_vip": "VIP" in response.text
        }

    except Exception as e:
        return {
            "erreur": str(e)
        }


if __name__ == "__main__":
    print(verifier_vip())
