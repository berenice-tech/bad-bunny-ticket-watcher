from vip_scoring import score_vip


tests = [
    ("Ultimate Bad Bunny VIP Lounge Experience", 548.58),
    ("Early Entry Package", 258.58),
    ("Early Entry Package", 220),
    ("Package inconnu", 100),
]


for package, price in tests:
    print(
        package,
        price,
        "→",
        score_vip(package, price)
    )
