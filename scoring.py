from config import (
    MAX_PRICE_SINGLE,
    MAX_PRICE_TWO_TOTAL,
    SECTION_SCORES
)


def calculer_score(section, prix, nombre_places=1, source="Ticketmaster"):
    score = SECTION_SCORES.get(section, 5)

    # Ajustement prix
    if nombre_places == 1:
        if prix <= MAX_PRICE_SINGLE:
            score += 3
        else:
            score -= 3

    elif nombre_places == 2:
        if prix <= MAX_PRICE_TWO_TOTAL:
            score += 3
        else:
            score -= 3

    # Priorité aux sources officielles
    if source == "Ticketmaster":
        score += 2

    # Détermination de l'alerte
    if score >= 12:
        niveau = "🟢 PRIORITÉ"
    elif score >= 8:
        niveau = "🟡 INTÉRESSANT"
    elif source in ["Viagogo", "StubHub"]:
        niveau = "🔴 SECONDAIRE"
    else:
        niveau = "❌ IGNORER"

    return niveau, score


if __name__ == "__main__":
    test = calculer_score(
        section="3D",
        prix=145,
        nombre_places=1,
        source="Ticketmaster"
    )

    print(test)
