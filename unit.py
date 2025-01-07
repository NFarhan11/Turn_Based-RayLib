from game_data import UNIT_DATA
from random import randint

class Unit:
    def __init__(self, name):
        self.name = name
        self.hp = UNIT_DATA[name]["stats"]["HP"]
        # self.atk = UNIT_DATA[name]["stats"]["ATK"]
        # self.defense = UNIT_DATA[name]["stats"]["DEF"]
        # self.resistance = UNIT_DATA[name]["stats"]["RES"]
        # self.speed = UNIT_DATA[name]["stats"]["SPD"]
        # self.talents = UNIT_DATA[name]["talents"]
        self.stats = UNIT_DATA[name]["stats"]
        self.talents = UNIT_DATA[name]["talents"]

        self.hp -= randint(0, 50)

    def get_stat(self, stat):
        return self.stats[stat]
    
    def get_stats(self):
        return {
            "HP": self.get_stat("HP"),
            "ATK": self.get_stat("ATK"),
            "DEF": self.get_stat("DEF"),
            "RES": self.get_stat("RES"),
            "SPD": self.get_stat("SPD")
            }
    
    def get_talents(self):
        return self.talents
    # def attack(self, target):
    #     damage = self.atk - target.defense
    #     target.hp -= damage
    #     print(f'{self.name} attacks {target.name} for {damage} damage')

    # def is_alive(self):
    #     return self.hp > 0

    # def __str__(self):
    #     return f'{self.name} has {self.hp} hp'