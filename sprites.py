import pyray as pr
from utils import draw_bar


# Sprite class to manage individual sprites
class Sprite:
    def __init__(self, groups=None):
        # add sprite to specified groups
        for group in groups:
            group.add(self)

    def draw(self):
        pass

    def update(self):
        pass


# Group class to manage multiple sprites
class SpriteGroup:
    def __init__(self):
        self.sprites = []

    def add(self, sprite):
        self.sprites.append(sprite)

    def remove(self, sprite):
        self.sprites.remove(sprite)

    def update(self):
        for sprite in self.sprites:
            sprite.update()

    def draw(self):
        for sprite in self.sprites:
            sprite.draw()


# Battle sprites
class UnitSprite(Sprite):
    def __init__(self, pos, groups, unit, index, pos_index, team):
        super().__init__(groups)
        self.index = index
        self.pos_index = pos_index
        self.team = team
        self.unit = unit
        self.width = 40
        self.height = 40
        self.rect = pr.Rectangle(pos[0], pos[1], self.width, self.height)

    def draw(self):
        # Draw the base sprite
        pr.draw_rectangle_rec(self.rect, pr.BLUE if self.team == "player" else pr.RED)


# Unit name sprites
class UnitNameSprite(Sprite):
    def __init__(self, pos, unit, groups):
        super().__init__(groups)
        self.pos = pos
        self.unit = unit

    def draw(self):
        pr.draw_text(f"{self.unit.name}", self.pos[0], self.pos[1] + 45, 15, pr.WHITE)


# Unit stats sprite
class UnitStatsSprite(Sprite):
    def __init__(self, pos, unit, team, groups):
        super().__init__(groups)
        self.pos = pos
        self.unit = unit
        self.team = team

    def draw(self):
        # HP text
        pr.draw_text(
            f"{self.unit.hp}/{self.unit.get_stat('HP')}",
            self.pos[0] - 250 if self.team == "player" else self.pos[0] + 80,
            self.pos[1],
            20,
            pr.WHITE,
        )
        # HP bar
        draw_bar(
            self.pos[0] - 250 if self.team == "player" else self.pos[0] + 80,
            self.pos[1] + 25,
            200,
            10,
            self.unit.hp / self.unit.get_stat("HP"),
            pr.RED,
            pr.BLACK,
        )
