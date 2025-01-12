import pyray as pr
from sprites import UnitSprite, SpriteGroup, UnitNameSprite, UnitStatsSprite
from settings import BATTLE_POSITIONS
from utils import CommandUI
import heapq


class Battle:
    def __init__(self, player_units, enemy_units):
        # General battle setup
        self.units_data = {"player": player_units, "enemy": enemy_units}

        # Sprite groups
        self.battle_sprites = SpriteGroup()
        self.player_sprites = SpriteGroup()
        self.enemy_sprites = SpriteGroup()

        # Command UI
        self.cmd_ui = CommandUI((0, 500), (1200, 200), 30)

        # Turn-based system
        self.current_unit = None
        self.turn_in_progress = False
        self.priority_queue = []

    # Setup methods
    def setup(self):
        self.initialize_units()
        self.initialize_priority_queue()

    def initialize_units(self):
        """Initialize and position units on the battlefield."""
        for team, units in self.units_data.items():
            # Limit to max 6 units per side
            for index, unit in {k: v for k, v in units.items() if k <= 5}.items():
                self.create_unit(unit, index, index, team)

    def initialize_priority_queue(self):
        """Initialize the priority queue based on unit speed."""
        combined_units = [
            unit
            for unit_dict in self.units_data.values()
            for unit in unit_dict.values()
        ]
        self.priority_queue = [
            (-unit.get_stat("SPD"), index, unit)
            for index, unit in enumerate(combined_units)
            if unit.is_alive
        ]
        heapq.heapify(self.priority_queue)

    def create_unit(self, unit, index, pos_index, team):
        """Create a unit and its associated sprites."""
        pos = list(BATTLE_POSITIONS[team].values())[pos_index]
        groups = [
            self.battle_sprites,
            self.player_sprites if team == "player" else self.enemy_sprites,
        ]
        UnitSprite(pos, groups, unit, index, pos_index, team)
        UnitNameSprite(pos, unit, groups)
        UnitStatsSprite(pos, unit, team, groups)

    # Turn system
    def process_turn(self):
        """Process the current unit's turn."""
        if not self.turn_in_progress:
            # if queue is empty, repopulate it
            if not self.priority_queue:
                self.repopulate_queue()

            # process next unit turn
            if self.priority_queue:
                _, _, unit = heapq.heappop(self.priority_queue)
                if unit.is_alive:
                    self.current_unit = unit
                    self.turn_in_progress = True
                    print(f"{unit.name} takes turn")
                else:
                    self.process_turn()  # Skip dead units

    def repopulate_queue(self):
        """Repopulate the queue with alive units"""
        combined_units = [
            unit
            for unit_dict in self.units_data.values()
            for unit in unit_dict.values()
        ]
        self.priority_queue = [
            (-unit.get_stat("SPD"), index, unit)
            for index, unit in enumerate(combined_units)
            if unit.is_alive
        ]
        heapq.heapify(self.priority_queue)
        print("Repopulating queue...")

    def end_turn(self):
        """End the current unit's turn and move to the next."""
        if self.current_unit:
            print(f"{self.current_unit.name} finished its turn")
            self.current_unit = None
            self.turn_in_progress = False
            self.process_turn()

    def highlight_unit(self, unit):
        """Highlight the currently active unit."""
        for sprite in self.battle_sprites.sprites:
            if isinstance(sprite, UnitSprite) and sprite.unit == unit:
                sprite_pos = pr.Vector2(
                    sprite.rect.x + sprite.width / 2,
                    sprite.rect.y + sprite.rect.height / 2,
                )
                pr.draw_circle_v(sprite_pos, 10, pr.YELLOW)

    def input(self):
        if pr.is_key_pressed(pr.KEY_F):
            self.end_turn()

    # Game loop
    def update(self):
        """Update the game state."""
        self.process_turn()
        self.battle_sprites.update()
        self.input()

    def draw(self):
        """Draw the game elements."""
        pr.clear_background(pr.DARKGRAY)
        self.battle_sprites.draw()
        self.cmd_ui.draw(unit=self.current_unit)

        if self.current_unit:  # Hightlight current unit if there is one.
            self.highlight_unit(self.current_unit)
