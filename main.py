from watcher import traiter_ticket
from ticketmaster_vip import recuperer_vip
from ticketmaster_classique import recuperer_classique
from vip_scoring import score_ticket as score_vip
from scoring import score_ticket as score_classique
from datetime import datetime


def lancer_surveillance():

    print("🎟️ Bad Bunny Ticket Watcher démarré")
    print("Vérification :", datetime.now())

    tickets = []

    tickets.extend(recuperer_vip())
    tickets.extend(recuperer_classique())

    print("Billets trouvés :", len(tickets))

    for ticket in tickets:

        if ticket["source"] == "Ticketmaster VIP":
            
            analyse = score_vip(
                ticket["source"],
                ticket["section"],
                ticket["prix"]
            )

        else:

            analyse = score_ticket(
                ticket["source"],
                ticket["section"],
                ticket["prix"]
            )

        ticket["score"] = analyse["score"]
        ticket["niveau"] = analyse["niveau"]

        print(ticket)
        print(analyse)

        if ticket["score"] > 0:

            resultat = traiter_ticket(ticket)

            print(resultat)


if __name__ == "__main__":
    lancer_surveillance()
