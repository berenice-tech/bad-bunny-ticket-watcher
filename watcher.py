from memory import billet_deja_vu
from alerts import creer_message
from notifier import envoyer_telegram


def traiter_ticket(ticket):

    if billet_deja_vu(ticket):
        return "Doublon ignoré"

    message = creer_message(
        niveau=ticket.get("niveau", "🟢 PRIORITÉ"),
        source=ticket.get("source", ""),
        section=ticket.get("section", ""),
        prix=ticket.get("prix", ""),
        places=ticket.get("places", 1),
        score=ticket.get("score", 0),
        url=ticket.get("url", "")
    )

    resultat = envoyer_telegram(message)

    return resultat
