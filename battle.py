import pyray as pr
from sprites import UnitSprite, SpriteGroup
from settings import BATTLE_POSITIONS


class Battle:
    def __init__(self, player_units, enemy_units):
        # general
        self.units_data = {"player": player_units, "enemy": enemy_units}

        # groups
        self.battle_sprites = SpriteGroup()
        self.player_sprites = SpriteGroup()
        self.enemy_sprites = SpriteGroup()

    def setup(self):
        for team, units in self.units_data.items():
            # limit to max 6 units per side
            for index, unit in {k: v for k, v in units.items() if k <= 5}.items():
                self.create_unit(unit, index, index, team)

    def create_unit(self, unit, index, pos_index, team):
        # get a unit's predefined position (x, y)
        pos = list(BATTLE_POSITIONS[team].values())[pos_index]
        #  assign groups for a unit
        groups = [
            self.battle_sprites,
            self.player_sprites if team == "player" else self.enemy_sprites,
        ]
        UnitSprite(pos, groups, unit, index, pos_index, team)

    def update(self, dt):
        pr.clear_background(pr.DARKGRAY)
        self.battle_sprites.draw()
