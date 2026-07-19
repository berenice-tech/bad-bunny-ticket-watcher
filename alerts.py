def creer_message(
    niveau,
    source,
    section,
    prix,
    places,
    score,
    url=""
):

    message = f"""
{niveau} — BAD BUNNY BRUXELLES

🎟 Source : {source}
📍 Section : {section}
💺 Places : {places}
💶 Prix : {prix} €

⭐ Score : {score}

🔗 Lien :
{url}

➡️ Vérifie rapidement !
"""

    return message.strip()
