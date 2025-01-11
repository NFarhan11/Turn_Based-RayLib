import pyray as pr


def draw_bar(x, y, width, height, progress, bar_color, background_color):
    """
    Draws a progress bar on the screen.

    Parameters:
    x: The x-coordinate of the top-left corner of the progress bar.
    y: The y-coordinate of the top-left corner of the progress bar.
    width: The total width of the progress bar.
    height: The height of the progress bar.
    progress: The progress value (0.0 to 1.0).
    bar_color (pr.Color): The color of the progress bar.
    background_color (pr.Color): The color of the background of the progress bar.
    """
    # Draw the background of the progress bar
    pr.draw_rectangle_v(pr.Vector2(x, y), pr.Vector2(width, height), background_color)

    # Calculate the width of the filled part of the progress bar
    filled_width = int(width * progress)

    # Draw the filled part of the progress bar
    pr.draw_rectangle_v(pr.Vector2(x, y), pr.Vector2(filled_width, height), bar_color)


class CommandUI:
    def __init__(self, pos, size, font_size):
        self.x = pos[0]
        self.y = pos[1]
        self.width = size[0]
        self.height = size[1]
        self.font_size = font_size

    def draw(self):
        # Main rectangle
        ui_rect = pr.Rectangle(self.x, self.y, self.width, self.height)
        pr.draw_rectangle_rounded(ui_rect, 0.1, 2, pr.GRAY)

        # Draw left GUI (Unit)
        self.draw_left_ui(ui_rect)
        self.draw_right_ui(ui_rect)

    def draw_left_ui(self, ui_rect):
        # Unit GUI (centered on the left half)
        padding = 10
        unit_width = (ui_rect.width / 2) - padding * 2
        unit_height = ui_rect.height - padding * 2
        unit_rect = pr.Rectangle(
            ui_rect.x + padding, ui_rect.y + padding, unit_width, unit_height
        )
        pr.draw_rectangle_rec(unit_rect, pr.RED)

        # Unit name
        unit_name_rec = pr.Rectangle(
            unit_rect.x + padding, unit_rect.y + padding, 150, 50
        )
        pr.draw_rectangle_rec(unit_name_rec, pr.GREEN)

        # Unit command
        unit_cmd_rec = pr.Rectangle(
            unit_rect.x + padding, unit_rect.y + padding + 60, 250, 100
        )
        pr.draw_rectangle_rec(unit_cmd_rec, pr.DARKBLUE)

        # Talent desc
        unit_talent_rec = pr.Rectangle(
            unit_rect.x + padding + 260, unit_rect.y + padding + 60, 300, 100
        )
        pr.draw_rectangle_rec(unit_talent_rec, pr.DARKPURPLE)

        # Innate Talent
        unit_innate_rec = pr.Rectangle(
            unit_rect.x + padding + 160, unit_rect.y + padding, 200, 50
        )
        pr.draw_rectangle_rec(unit_innate_rec, pr.DARKGREEN)

    def draw_right_ui(self, ui_rect):
        padding = 10
        # Middle of the main rectangle
        midx = ui_rect.x + ui_rect.width / 2
        # Right
        width = (ui_rect.width / 2) - padding * 2
        height = ui_rect.height - padding * 2
        right_rect = pr.Rectangle(
            midx + padding,
            ui_rect.y + padding,
            width,
            height,
        )
        pr.draw_rectangle_rec(right_rect, pr.BLUE)

        # Divide the right half into Action Order and Prompt sections
        section_height = (height - padding) / 2

        # Action Order section
        action_rect = pr.Rectangle(
            right_rect.x,
            right_rect.y,
            right_rect.width,
            section_height,
        )
        pr.draw_rectangle_rec(action_rect, pr.RED)

        # Prompt section
        prompt_rect = pr.Rectangle(
            right_rect.x,
            right_rect.y + section_height + padding,
            right_rect.width,
            section_height,
        )
        pr.draw_rectangle_rec(prompt_rect, pr.GREEN)
