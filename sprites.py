import pyray as pr


# Sprite class to manage individual sprites
class Sprite:
    def __init__(self, pos):
        self.width = 40
        self.height = 40
        self.rect = pr.Rectangle(pos[0], pos[1], self.width, self.height)

    def draw(self):
        pr.draw_rectangle_rec(self.rect, pr.RED)

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
        super().__init__(pos)
        self.index = index
        self.pos_index = pos_index
        self.team = team
        self.unit = unit

        # add sprite to specified groups
        for group in groups:
            group.add(self)

    def draw(self):
        # Draw the base sprite
        pr.draw_rectangle_rec(self.rect, pr.BLUE if self.team == "player" else pr.RED)

