from config import VIP_MAX_PRICE, VIP_PACKAGES_INTERESSANTS


def score_ticket(source, section, prix):
    """
    Analyse un package VIP selon :
    - le type de package
    - le budget
    """

    if package not in VIP_PACKAGES_INTERESSANTS:
        return {
            "niveau": "⚫ IGNORER",
            "score": 0,
            "raison": "Package VIP non surveillé"
        }

    if price <= VIP_MAX_PRICE:
        return {
            "niveau": "🟢 PRIORITÉ",
            "score": 15,
            "raison": "Dans le budget VIP"
        }

    elif price <= VIP_MAX_PRICE + 50:
        return {
            "niveau": "🟡 PROCHE",
            "score": 8,
            "raison": "Légèrement au-dessus du budget"
        }

    else:
        return {
            "niveau": "⚫ IGNORER",
            "score": 0,
            "raison": "Trop cher"
        }
