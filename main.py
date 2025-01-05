import pyray as pr
from unit import Unit
from unit_index import UnitIndex
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
            5: Unit("myrmidon_monk"),
            6: Unit("goblin"),
        }

        # overlays
        self.unit_index = UnitIndex(self.player_units)
        self.index_open = False

    def input(self):
        if pr.is_key_pressed(pr.KEY_ENTER):
            print("toggle index")
            self.index_open = not self.index_open

    def render(self):
        pr.begin_drawing()
        pr.clear_background(pr.BLACK)
        pr.draw_text("Hello World", 10, 10, 20, pr.DARKGRAY)
        pr.end_drawing()
        
    def run(self):

        # game loop
        while not pr.window_should_close():

            # update
            self.input()
            
            # render
            self.render()

            # overlays
            if self.index_open:
                self.unit_index.update()

        pr.close_window()

if __name__ == "__main__":
    Game().run()