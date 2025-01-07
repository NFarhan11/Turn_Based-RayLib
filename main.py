import pyray as pr
from unit import Unit
from unit_index import UnitIndex
from battle import Battle
from settings import WINDOW_WIDTH, WINDOW_HEIGHT

class Game:
    def __init__(self):
        # window
        pr.init_window(WINDOW_WIDTH, WINDOW_HEIGHT, "RPG Game")
        pr.set_target_fps(60)
        
        # player units
        self.player_units = {
            0: Unit("captain"),
            1: Unit("female_wizard"),
            2: Unit("sword_maiden"),
            3: Unit("female_warrior"),
            4: Unit("scout"),
            5: Unit("myrmidon_monk")
        }

        #enemy units
        self.enemy_units = {
            0: Unit("goblin"),
            1: Unit("goblin"),
            2: Unit("goblin"),
        }

        # overlays
        self.unit_index = UnitIndex(self.player_units)
        self.index_open = False
        self.battle = Battle(self.player_units, self.enemy_units)

    def input(self):
        if not self.battle:
            if pr.is_key_pressed(pr.KEY_ENTER):  # toggle index menu
                self.index_open = not self.index_open

    def render(self):
        pr.clear_background(pr.BLACK)
        pr.draw_text("Hello World", 10, 10, 20, pr.DARKGRAY)
        
        
    def run(self):

        # game loop
        while not pr.window_should_close():
            dt = pr.get_frame_time()

            # update
            self.input()

            # start_draw
            pr.begin_drawing()
            
            # render
            self.render()

            # overlays
            if self.index_open:
                self.unit_index.update()
            if self.battle:
                self.battle.update(dt)

            # end_draw
            pr.end_drawing()
        pr.close_window()

if __name__ == "__main__":
    Game().run()