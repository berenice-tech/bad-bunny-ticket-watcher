from memory import (
    billet_deja_vu,
    enregistrer_billet
)


ticket = "TM-3D-R15-145"


print("Premier passage :")

if billet_deja_vu(ticket):
    print("❌ Déjà connu")
else:
    print("✅ Nouveau billet")
    enregistrer_billet(ticket)


print("\nDeuxième passage :")

if billet_deja_vu(ticket):
    print("✅ Doublon détecté")
else:
    print("❌ Erreur mémoire")
