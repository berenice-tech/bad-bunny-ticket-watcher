from watcher import traiter_ticket
from ticketmaster_vip_live import recuperer_vip
from datetime import datetime


def lancer_surveillance():

    print("🎟️ Bad Bunny Ticket Watcher démarré")
    print("Vérification :", datetime.now())

    tickets = recuperer_vip()



for ticket in tickets:

    analyse = scorer_vip(
        ticket["package"],
        ticket["prix"]
    )

    ticket["score"] = analyse["score"]
    ticket["niveau"] = analyse["niveau"]

    if ticket["score"] > 0:
        resultat = traiter_ticket(ticket)
        print(resultat)

if __name__ == "__main__":
    lancer_surveillance()
