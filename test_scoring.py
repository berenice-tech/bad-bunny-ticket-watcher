from scoring import calculer_score


tests = [
    {
        "section": "3D",
        "prix": 145,
        "places": 1,
        "source": "Ticketmaster"
    },
    {
        "section": "Golden",
        "prix": 170,
        "places": 1,
        "source": "Ticketmaster"
    },
    {
        "section": "3A",
        "prix": 190,
        "places": 2,
        "source": "TicketSwap"
    },
    {
        "section": "Catégorie 4",
        "prix": 250,
        "places": 1,
        "source": "StubHub"
    }
]


for billet in tests:
    resultat = calculer_score(
        section=billet["section"],
        prix=billet["prix"],
        nombre_places=billet["places"],
        source=billet["source"]
    )

    print(
        billet["source"],
        billet["section"],
        billet["prix"],
        "€ →",
        resultat
    )
