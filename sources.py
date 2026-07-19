from ticketmaster_vip import recuperer_vip
from ticketmaster_classique import recuperer_classique


def recuperer_tous_les_tickets():

    tickets = []

    tickets.extend(recuperer_vip())
    tickets.extend(recuperer_classique())

    return tickets
