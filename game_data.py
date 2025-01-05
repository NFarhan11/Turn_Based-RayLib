UNIT_DATA = {
    "captain": {"stats": {"HP": 100, "ATK": 10, "DEF": 10, "RES": 1, "SPD": 5}, "talents": ["slash", "dodge"]},
    "female_wizard": {"stats": {"HP": 100, "ATK": 10, "DEF": 10, "RES": 1, "SPD": 5}, "talents": ["magic_beam", "dodge"]},
    "sword_maiden": {"stats": {"HP": 100, "ATK": 10, "DEF": 10, "RES": 1, "SPD": 5}, "talents": ["slash", "dodge"]},
    "female_warrior": {"stats": {"HP": 100, "ATK": 10, "DEF": 10, "RES": 1, "SPD": 5}, "talents": ["thrust", "dodge"]},
    "scout": {"stats": {"HP": 100, "ATK": 10, "DEF": 10, "RES": 1, "SPD": 5}, "talents": ["dash", "dodge"]},
    "myrmidon_monk": {"stats": {"HP": 100, "ATK": 10, "DEF": 10, "RES": 1, "SPD": 5}, "talents": ["punch", "dodge"]},
    "goblin": {"stats": {"HP": 100, "ATK": 10, "DEF": 10, "RES": 1, "SPD": 5}, "talents": ["slash", "dodge"]},
}

TALENT_DATA = {
    "dodge": {"type": "utility", "power": 10, "cost": 5, "target": "self"},
    "slash": {"type": "attack", "power": 10, "cost": 5, "target": "enemy"},
    "thrust": {"type": "attack", "power": 10, "cost": 5, "target": "enemy"},
    "punch": {"type": "attack", "power": 10, "cost": 5, "target": "enemy"},
    "magic_beam": {"type": "attack", "power": 10, "cost": 5, "target": "enemy"},
    "dash": {"type": "attack", "power": 10, "cost": 5, "target": "enemy"},
}