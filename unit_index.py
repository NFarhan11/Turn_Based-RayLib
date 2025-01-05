import pyray as pr
from settings import WINDOW_WIDTH, WINDOW_HEIGHT
from utils import draw_bar

class UnitIndex:
    def __init__(self, units):
        self.units = units

        # dimensions
        self.main_rect = pr.Rectangle(
            (WINDOW_WIDTH - WINDOW_WIDTH * 0.6) / 2,
            (WINDOW_HEIGHT - WINDOW_HEIGHT * 0.8) / 2,
            WINDOW_WIDTH * 0.6,
            WINDOW_HEIGHT * 0.8
        )

        # list
        self.visible_items = 6
        self.list_width = self.main_rect.width * 0.4
        self.item_height = self.main_rect.height / self.visible_items
        self.index = 0
        self.selected_index = None

    def input(self):
        if pr.is_key_pressed(pr.KEY_W):
            self.index -= 1
        if pr.is_key_pressed(pr.KEY_S):
            self.index += 1
        if pr.is_key_pressed(pr.KEY_F):
            if self.selected_index is not None:
                selected_unit = self.units[self.selected_index]
                current_unit = self.units[self.index]
                self.units[self.selected_index] = current_unit
                self.units[self.index] = selected_unit
                self.selected_index = None
            else:
                self.selected_index = self.index  # select current index
                

        self.index = self.index % len(self.units)

    def display_list(self):
        # handle vertical scrolling
        v_offset = 0 if self.index < self.visible_items else -self.item_height

        for index, unit in self.units.items():
            top = self.main_rect.y + index * self.item_height + v_offset
            item_rect = pr.Rectangle(self.main_rect.x, top, self.list_width, self.item_height)

            # draw items without spill over
            if pr.check_collision_recs(self.main_rect, item_rect):
                bg_color = pr.DARKGRAY if index != self.index else pr.GRAY
                txt_color = pr.WHITE if index != self.selected_index else pr.GOLD
                pr.draw_rectangle_rec(item_rect, bg_color)
                pr.draw_text(unit.name, int(item_rect.x + 10), int(item_rect.y + (item_rect.height / 2) - 10), 20, txt_color)

        # draw lines
        for i in range(min(self.visible_items, len(self.units))):
            left = self.main_rect.x
            right = self.main_rect.x + self.list_width
            y = self.main_rect.y + self.item_height * i
            pr.draw_line_v((left, y), (right, y), pr.WHITE)

        # shadow
        shadow_rect = pr.Rectangle(self.main_rect.x + self.list_width - 4, self.main_rect.y, 5, self.main_rect.height)
        pr.draw_rectangle_rec(shadow_rect, pr.Color(0,0,0, 128))

    def display_main(self):
        # main bg
        rect = pr.Rectangle(self.main_rect.x + self.list_width, self.main_rect.y, self.main_rect.width - self.list_width, self.main_rect.height)
        pr.draw_rectangle_rec(rect, pr.LIGHTGRAY)

        # upper rect
        upper_rect = pr.Rectangle(rect.x, rect.y, rect.width, rect.height * 0.3)
        pr.draw_rectangle_rec(upper_rect, pr.GRAY)

        # name
        unit = self.units[self.index]
        pr.draw_text(unit.name, int(upper_rect.x + 10), int(upper_rect.y + (upper_rect.height / 2) - 10), 20, pr.WHITE)

        # hp_bar
        hp_bar = pr.Rectangle(upper_rect.x + 10, upper_rect.y + upper_rect.height + 10, upper_rect.width *0.6, 20)
        draw_bar(hp_bar.x, hp_bar.y, hp_bar.width, hp_bar.height, unit.hp / unit.stats["HP"], pr.RED, pr.BLACK)
        pr.draw_text(f'HP: {unit.hp} / {unit.stats["HP"]}', int(hp_bar.x + 10), int(hp_bar.y + (hp_bar.height / 2 - 6)), 15, pr.WHITE) 

    def update(self):
        self.input()
        self.display_main()
        self.display_list()