UNIT_DATA = {
    "captain": {
        "stats": {"HP": 80, "ATK": 18, "DEF": 10, "RES": 1, "SPD": 24},
        "talents": ["slash", "dodge"],
    },
    "female_wizard": {
        "stats": {"HP": 45, "ATK": 14, "DEF": 10, "RES": 10, "SPD": 10},
        "talents": ["magic_beam", "dodge"],
    },
    "sword_maiden": {
        "stats": {"HP": 50, "ATK": 10, "DEF": 0, "RES": 12, "SPD": 10},
        "talents": ["slash", "dodge"],
    },
    "female_warrior": {
        "stats": {"HP": 75, "ATK": 17, "DEF": 0, "RES": 1, "SPD": 25},
        "talents": ["thrust", "dodge"],
    },
    "scout": {
        "stats": {"HP": 100, "ATK": 15, "DEF": 5, "RES": 1, "SPD": 20},
        "talents": ["dash", "dodge"],
    },
    "myrmidon_monk": {
        "stats": {"HP": 100, "ATK": 20, "DEF": 10, "RES": 10, "SPD": 5},
        "talents": ["punch", "dispel", "dodge"],
    },
    "goblin": {
        "stats": {"HP": 20, "ATK": 5, "DEF": 5, "RES": 0, "SPD": 5},
        "talents": ["slash", "dodge"],
    },
}

TALENT_DATA = {
    "dodge": {
        "type": "utility",
        "power": 0,
        "cost": 5,
        "target": "self",
        "desc": "Chance to evade targeted talent.",
    },
    "slash": {
        "type": "physical",
        "power": 40,
        "cost": 10,
        "target": "enemy",
        "desc": "Cut an enemy with sharp edges.",
    },
    "thrust": {
        "type": "physical",
        "power": 35,
        "cost": 15,
        "target": "enemy",
        "desc": "Run through an enemy with lances.",
    },
    "punch": {
        "type": "physical",
        "power": 20,
        "cost": 20,
        "target": "enemy",
        "desc": "A normal punch.",
    },
    "magic_beam": {
        "type": "magic",
        "power": 60,
        "cost": 15,
        "target": "enemy",
        "desc": "A burst of mana unleashed in a beam.",
    },
    "dash": {
        "type": "physical",
        "power": 15,
        "cost": 10,
        "target": "enemy",
        "desc": "Trades low damage with agility.",
    },
    "dispel": {
        "type": "magic",
        "power": 30,
        "cost": 10,
        "target": "enemy_aoe",
        "desc": "Deals double damage to summons.",
    },
}
