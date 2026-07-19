def score_vip(package, prix):

    if package not in [
        "Early Entry Package",
        "Silver Premium Ticket Package",
        "Gold Premium Ticket Package"
    ]:
        return {
            "niveau": "⚫ IGNORER",
            "score": 0,
            "raison": "Package VIP non surveillé"
        }

    if prix <= 250:
        return {
            "niveau": "🟢 PRIORITÉ",
            "score": 15,
            "raison": "Dans le budget VIP"
        }

    if prix <= 260:
        return {
            "niveau": "🟡 PROCHE",
            "score": 8,
            "raison": "Légèrement au-dessus du budget"
        }

    return {
        "niveau": "⚫ IGNORER",
        "score": 0,
        "raison": "Trop cher"
    }
