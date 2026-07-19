from config import VIP_MAX_PRICE


def score_vip(package, price):
    """
    Analyse un package VIP selon le budget.
    Retourne niveau d'alerte + score.
    """

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


if __name__ == "__main__":

    tests = [
        ("Ultimate VIP", 548.58),
        ("Early Entry", 258.58),
        ("VIP intéressant", 220),
    ]

    for package, price in tests:
        print(
            package,
            price,
            "→",
            score_vip(package, price)
        )
