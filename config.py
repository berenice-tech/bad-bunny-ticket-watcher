# Configuration Bad Bunny Ticket Watcher

EVENT = {
    "artist": "Bad Bunny",
    "city": "Brussels",
    "date": "2026-07-22",
}

# Budget
MAX_PRICE_SINGLE = 150
MAX_PRICE_TWO_TOTAL = 200

# Nombre de billets
ALLOW_SINGLE_TICKET = True
ALLOW_TWO_TICKETS = True

# Sections prioritaires
SECTION_SCORES = {
    "3D": 10,
    "3C": 10,
    "3A": 9,
    "Golden": 10,
    "VIP": 10,
    "Catégorie 2": 8,
}

# Niveau d'alerte
ALERT_LEVELS = {
    "green": "Achat recommandé",
    "yellow": "Bonne opportunité",
    "red": "Surveillance secondaire",
}

# Identifiants Ticketmaster
TICKETMASTER_EVENT_ID = "Z698xZG2Z16v79kZ04"
TICKETMASTER_VIP_EVENT_ID = "Z698xZG2Z16vGyuk_A"

# Règle spéciale VIP
VIP_MAX_PRICE = 250

# Identifiants Ticketmaster
TICKETMASTER_EVENT_ID = "Z698xZG2Z16v79kZ04"
TICKETMASTER_VIP_EVENT_ID = "Z698xZG2Z16vGyuk_A"

# Règle spéciale VIP
VIP_MAX_PRICE = 250

# Packages VIP surveillés
VIP_PACKAGES_INTERESSANTS = [
    "Early Entry Package",
    "Silver Premium Ticket Package",
    "Gold Premium Ticket Package"
]

TICKETMASTER_URL = (
    "https://www.ticketmaster.be/"
    "event/bad-bunny-debi-tirar-mas-fotos-world-tour-tickets/1117180915"
)
