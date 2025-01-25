from game_data import TALENT_DATA

current_talent = None


def handle_talent(unit, name):
    for talent in TALENT_DATA:
        if name == talent:
            talent_manager = Talent(name, unit)
            talent_manager.execute_talent()


class Talent:
    def __init__(self, name, unit):
        self.name = name
        self.type = TALENT_DATA[self.name]["type"]
        self.power = TALENT_DATA[self.name]["power"]
        self.cost = TALENT_DATA[self.name]["cost"]
        self.target = TALENT_DATA[self.name]["target"]

        self.unit = unit
        print(f"This is {name}, belongs to {unit.name}")

    def test_dmg(self):
        dmg = self.power
        self.unit.modify_stat("HP", -dmg)

    def execute_talent(self):
        self.test_dmg()
