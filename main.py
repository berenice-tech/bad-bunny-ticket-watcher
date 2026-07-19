from watcher import traiter_ticket
from datetime import datetime


def lancer_surveillance():

    print("🎟️ Bad Bunny Ticket Watcher démarré")
    print("Vérification :", datetime.now())

    # TEST TEMPORAIRE
    # sera remplacé par Ticketmaster / TicketSwap

    tickets = [
        {
            "source": "Ticketmaster VIP",
            "section": "VIP",
            "prix": 220,
            "places": 1,
            "url": "https://www.ticketmaster.be/"
        }
    ]

    for ticket in tickets:
        resultat = traiter_ticket(ticket)
        print(resultat)


if __name__ == "__main__":
    lancer_surveillance()
