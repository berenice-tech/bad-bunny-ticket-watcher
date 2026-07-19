import json
import os

MEMORY_FILE = "seen_tickets.json"


def charger_billets_vus():
    if not os.path.exists(MEMORY_FILE):
        return []

    with open(MEMORY_FILE, "r") as f:
        return json.load(f)


def billet_deja_vu(ticket_id):
    billets = charger_billets_vus()
    return ticket_id in billets


def enregistrer_billet(ticket_id):
    billets = charger_billets_vus()

    if ticket_id not in billets:
        billets.append(ticket_id)

        with open(MEMORY_FILE, "w") as f:
            json.dump(billets, f, indent=2)
