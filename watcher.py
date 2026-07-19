from memory import billet_deja_vu
from alerts import creer_message
from notifier import envoyer_telegram


def traiter_ticket(ticket):

    if billet_deja_vu(ticket):
        return "Doublon ignoré"

    message = creer_message(
        niveau="🟢 PRIORITÉ",
        source=ticket["source"],
        section=ticket.get("section", ""),
        prix=ticket["prix"],
        places=ticket.get("places", 1),
        score=15
    )

    resultat = envoyer_telegram(message)

    return resultat
