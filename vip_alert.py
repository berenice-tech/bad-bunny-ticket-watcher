from vip_scoring import score_vip
from notifier import envoyer_message
from memory import billet_deja_vu


VIP_LINK = "https://www.ticketmaster.be/event/bad-bunny-debi-tirar-mas-fotos-world-tour-%7C-vip-packages-tickets/1339346645"


def verifier_vip(package, price):

    resultat = score_vip(package, price)

    ticket = {
        "source": "Ticketmaster VIP",
        "package": package,
        "price": price
    }

    if resultat["score"] == 0:
        return "Pas d'alerte"

    if billet_deja_vu(ticket):
        return "Déjà envoyé"

    message = f"""
{resultat['niveau']} VIP 👑

Bad Bunny Bruxelles

Package :
{package}

Prix :
{price} €

Source :
Ticketmaster VIP

Lien :
{VIP_LINK}
"""

    envoyer_message(message)

    return "Alerte envoyée"


if __name__ == "__main__":

    print(
        verifier_vip(
            "Early Entry Package",
            220
        )
    )
