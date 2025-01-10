import pyray as pr
from settings import WINDOW_WIDTH, WINDOW_HEIGHT, COLORS
from utils import draw_bar
from game_data import UNIT_DATA, TALENT_DATA


class UnitIndex:
    def __init__(self, units):
        self.units = units

        # dimensions
        self.main_rect = pr.Rectangle(
            (WINDOW_WIDTH - WINDOW_WIDTH * 0.6) / 2,
            (WINDOW_HEIGHT - WINDOW_HEIGHT * 0.8) / 2,
            WINDOW_WIDTH * 0.6,
            WINDOW_HEIGHT * 0.8,
        )

        # list
        self.visible_items = 6
        self.list_width = self.main_rect.width * 0.4
        self.item_height = self.main_rect.height / self.visible_items
        self.index = 0
        self.selected_index = None

        # max values
        self.max_stats = {}
        for unit in UNIT_DATA.values():
            # print (unit)
            for stat, value in unit["stats"].items():
                if stat not in self.max_stats:
                    self.max_stats[stat] = value
                else:
                    # keep the highest value
                    self.max_stats[stat] = (
                        value if value > self.max_stats[stat] else self.max_stats[stat]
                    )

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
                # select current index
                self.selected_index = self.index

        self.index = self.index % len(self.units)

    def display_list(self):
        # handle vertical scrolling
        v_offset = 0 if self.index < self.visible_items else -self.item_height

        for index, unit in self.units.items():
            top = self.main_rect.y + index * self.item_height + v_offset
            item_rect = pr.Rectangle(
                self.main_rect.x, top, self.list_width, self.item_height
            )

            # draw items without spill over
            if pr.check_collision_recs(self.main_rect, item_rect):
                bg_color = pr.DARKGRAY if index != self.index else pr.GRAY
                txt_color = pr.WHITE if index != self.selected_index else pr.GOLD
                pr.draw_rectangle_rec(item_rect, bg_color)
                pr.draw_text(
                    unit.name,
                    int(item_rect.x + 10),
                    int(item_rect.y + (item_rect.height / 2) - 10),
                    20,
                    txt_color,
                )

        # draw lines
        for i in range(1, min(self.visible_items, len(self.units))):
            left = self.main_rect.x
            right = self.main_rect.x + self.list_width
            y = self.main_rect.y + self.item_height * i
            pr.draw_line_v((left, y), (right, y), pr.WHITE)

        # shadow
        shadow_rect = pr.Rectangle(
            self.main_rect.x + self.list_width - 4,
            self.main_rect.y,
            5,
            self.main_rect.height,
        )
        pr.draw_rectangle_rec(shadow_rect, pr.Color(0, 0, 0, 128))

    def display_main(self):
        # main bg
        rect = pr.Rectangle(
            self.main_rect.x + self.list_width,
            self.main_rect.y,
            self.main_rect.width - self.list_width,
            self.main_rect.height,
        )
        pr.draw_rectangle_rec(rect, pr.DARKGRAY)

        # upper rect
        upper_rect = pr.Rectangle(rect.x, rect.y, rect.width, rect.height * 0.3)
        pr.draw_rectangle_rec(upper_rect, pr.GRAY)

        # name
        unit = self.units[self.index]
        pr.draw_text(
            unit.name,
            int(upper_rect.x + 10),
            int(upper_rect.y + (upper_rect.height / 2) - 10),
            20,
            pr.WHITE,
        )

        # hp_bar
        hp_bar = pr.Rectangle(
            upper_rect.x + 10,
            upper_rect.y + upper_rect.height + 10,
            upper_rect.width * 0.6,
            20,
        )
        draw_bar(
            hp_bar.x,
            hp_bar.y,
            hp_bar.width,
            hp_bar.height,
            unit.hp / unit.stats["HP"],
            pr.RED,
            pr.BLACK,
        )
        pr.draw_text(
            f"HP: {unit.hp} / {unit.stats['HP']}",
            int(hp_bar.x + 10),
            int(hp_bar.y + (hp_bar.height / 2 - 6)),
            15,
            pr.WHITE,
        )

        # info
        sides = {"left": hp_bar.x, "right": upper_rect.x + (upper_rect.width / 2)}
        info_height = (rect.y + rect.height) - (hp_bar.y + hp_bar.height) - 20
        stats_rect = pr.Rectangle(
            sides["left"], hp_bar.y + hp_bar.height + 60, hp_bar.width, info_height - 40
        )
        pr.draw_text(
            "STATS RANK:",
            int(sides["left"]),
            int(hp_bar.y + hp_bar.height + 25),
            20,
            pr.WHITE,
        )

        # stats
        base_stats = unit.get_stats()
        stat_height = stats_rect.height / len(base_stats)

        for item, (stat, value) in enumerate(base_stats.items()):
            # text
            pr.draw_text(
                f"{stat}: {value}",
                int(sides["left"]),
                int(stats_rect.y + stat_height * item + 5),
                18,
                pr.WHITE,
            )

            # stats_bar
            stats_bar = pr.Rectangle(
                sides["left"],
                int(stats_rect.y + stat_height * item + 25),
                stats_rect.width * 0.6,
                stat_height,
            )
            draw_bar(
                stats_bar.x,
                stats_bar.y,
                stats_bar.width,
                stats_bar.height * 0.1,
                (value / self.max_stats[stat]),
                pr.WHITE,
                pr.BLACK,
            )

        # talents
        pr.draw_text(
            "TALENTS:",
            int(sides["right"]),
            int(hp_bar.y + hp_bar.height + 25),
            20,
            pr.WHITE,
        )
        talent_rect = pr.Rectangle(
            sides["right"],
            hp_bar.y + hp_bar.height + 60,
            hp_bar.width * 0.8,
            info_height - 40,
        )
        unit_talents = unit.get_talents()
        talent_height = talent_rect.height / len(unit_talents)

        for item, talent in enumerate(unit_talents):
            talent_type = TALENT_DATA[talent]["type"]

            x = talent_rect.x + item % 2 * talent_rect.width / 2
            y = talent_rect.y + talent_height * int(item / 2)
            pr.draw_rectangle_v((x, y), (100, 21), COLORS[talent_type])
            pr.draw_text(talent, int(x), int(y), 18, pr.BLACK)

    def update(self):
        self.input()
        self.display_main()
        self.display_list()
