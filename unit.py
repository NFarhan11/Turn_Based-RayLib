from game_data import UNIT_DATA
from random import randint


class Unit:
    def __init__(self, name):
        # general
        self.name = name
        self.base_stats = UNIT_DATA[name]["stats"]
        self.talents = UNIT_DATA[name]["talents"]

        # variables
        self.current_stats = self.base_stats.copy()
        self.current_talent_stats = self.talents
        self.is_alive = True

        # temporary damage
        # random_damage = -(randint(0, 50))
        # self.modify_stat("HP", random_damage)

    def get_stat(self, stat, current=True):
        """Retrieve a specific stat, default to current."""
        if current:
            return self.current_stats[stat]
        return self.base_stats[stat]

    def get_stats(self, current=True):
        """Retrieve all stats, default to current."""
        stats_source = self.current_stats if current else self.base_stats
        return {key: stats_source[key] for key in stats_source}

    def get_talents(self):
        return self.current_talent_stats

    def modify_stat(self, stat, value):
        """Modify a current stat during battle."""
        if stat in self.current_stats:
            self.current_stats[stat] += value
            # HP cannot drop below 0
            if stat == "HP" and self.current_stats["HP"] < 0:
                self.current_stats["HP"] = 0
            # unit dies
            if self.current_stats["HP"] == 0:
                self.is_alive = False
