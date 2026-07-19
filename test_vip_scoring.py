from vip_scoring import score_vip


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
