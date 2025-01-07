import pyray as pr

class Battle:
    def __init__(self, player_units, enemy_units):
        self.units_data = {"player": player_units, "enemy": enemy_units}

    def setup(self):
        for team, units in self.units_data.items():
            # print(f"{team}, : {units}")
            for index, unit in {k:v for k, v in units.items() if k <= 5}.items():
                # print(f"{index}, {unit}")
                self.create_unit()

    def create_unit(self):
        pass

    def update(self, dt):
        pr.clear_background(pr.WHITE)
        self.setup()