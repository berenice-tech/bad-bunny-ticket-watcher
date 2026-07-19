from watcher import traiter_ticket
from sources import recuperer_tous_les_tickets
from vip_scoring import score_vip
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
            "score": 15
        }

    ticket["score"] = analyse["score"]
    ticket["niveau"] = analyse["niveau"]

    print(ticket)
    print(analyse)

    if ticket["score"] > 0:

        resultat = traiter_ticket(ticket)

        print(resultat)
        
