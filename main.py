from watcher import traiter_ticket
from ticketmaster_vip_live import recuperer_vip
from datetime import datetime


def lancer_surveillance():

    print("🎟️ Bad Bunny Ticket Watcher démarré")
    print("Vérification :", datetime.now())

    tickets = recuperer_vip()

    for ticket in tickets:
        resultat = traiter_ticket(ticket)
        print(resultat)


if __name__ == "__main__":
    lancer_surveillance()
