from watcher import traiter_ticket
from sources import recuperer_tous_les_tickets
from vip_scoring import score_vip
from memory import billet_deja_vu, enregistrer_billet
from datetime import datetime


def lancer_surveillance():

    print("🎟️ Bad Bunny Ticket Watcher démarré")
    print("Vérification :", datetime.now())

    tickets = recuperer_tous_les_tickets()

    print("Billets trouvés :", len(tickets))

    for ticket in tickets:

        if ticket["source"] == "Ticketmaster VIP":

            analyse = score_vip(
                ticket["package"],
                ticket["prix"]
            )

        else:

            analyse = {
                "niveau": "🟢 PRIORITÉ",
                "score": 15,
                "raison": "Billet non VIP détecté"
            }

        ticket["score"] = analyse["score"]
        ticket["niveau"] = analyse["niveau"]

        print(ticket)
        print(analyse)

        ticket_id = (
            ticket["source"]
            + "-"
            + ticket.get("section", "")
            + "-"
            + str(ticket["prix"])
            + "-"
            + ticket.get("package", "")
        )

        if billet_deja_vu(ticket_id):

            print("⏭️ Déjà envoyé :", ticket_id)
            continue

        if ticket["score"] > 0:

            resultat = traiter_ticket(ticket)

            enregistrer_billet(ticket_id)

            print(resultat)


if __name__ == "__main__":

    lancer_surveillance()
