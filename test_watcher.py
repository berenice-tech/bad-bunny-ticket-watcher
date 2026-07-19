from watcher import traiter_ticket


ticket_test = {
    "source": "Test",
    "section": "3D",
    "prix": 145,
    "places": 1,
    "url": "https://ticketmaster.be/test"
}


resultat = traiter_ticket(ticket_test)

print(resultat)
