import pyray as pr
from game_data import TALENT_DATA


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
        self.selected_command_index = 0  # Track selected command

    def draw(self, unit=None):
        # Main rectangle
        ui_rect = pr.Rectangle(self.x, self.y, self.width, self.height)
        pr.draw_rectangle_rounded(ui_rect, 0.1, 2, pr.GRAY)

        # Draw left GUI (Unit)
        self.draw_left_ui(ui_rect, unit)
        # self.draw_right_ui(ui_rect)
        self.handle_input(unit)

    def handle_input(self, unit):
        """Handles input for selecting a command and scrolling the talent list."""
        if pr.is_key_pressed(pr.KEY_S):
            self.selected_command_index = (self.selected_command_index + 1) % len(
                unit.talents
            )
        elif pr.is_key_pressed(pr.KEY_W):
            self.selected_command_index = (self.selected_command_index - 1) % len(
                unit.talents
            )

    def draw_left_ui(self, ui_rect, unit):
        # Unit GUI (centered on the left half)
        padding = 10
        unit_width = (ui_rect.width / 2) - padding * 2
        unit_height = ui_rect.height - padding * 2
        unit_rect = pr.Rectangle(
            ui_rect.x + padding, ui_rect.y + padding, unit_width, unit_height
        )
        pr.draw_rectangle_rec(unit_rect, pr.WHITE)

        # Unit name
        unit_name_rec = pr.Rectangle(
            unit_rect.x + padding, unit_rect.y + padding, 150, 50
        )
        pr.draw_rectangle_rec(unit_name_rec, pr.ORANGE)
        if unit:
            pr.draw_text(
                unit.name,
                int(unit_name_rec.x + padding * 1.5),
                int(unit_name_rec.y + padding * 1.5),
                18,
                pr.BLACK,
            )

        # Unit command (list of talents)
        unit_cmd_rec = pr.Rectangle(
            unit_rect.x + padding, unit_rect.y + padding + 60, 250, 100
        )
        pr.draw_rectangle_rec(unit_cmd_rec, pr.ORANGE)
        if unit:
            # Reset selected_command_index if out of range
            if self.selected_command_index >= len(unit.talents):
                self.selected_command_index = 0

            talent_x = int(unit_cmd_rec.x + padding)
            talent_y = int(unit_cmd_rec.y + padding)

            # Draw & highlight talents
            for index, talent in enumerate(unit.talents):
                color = pr.YELLOW if index == self.selected_command_index else pr.BLACK
                pr.draw_text(talent, talent_x, talent_y, 16, color)
                talent_y += 20

        # Talent desc
        unit_talent_rec = pr.Rectangle(
            unit_rect.x + padding + 260, unit_rect.y + padding + 60, 300, 100
        )
        pr.draw_rectangle_rec(unit_talent_rec, pr.ORANGE)

        if unit and unit.talents:
            selected_talent = unit.talents[self.selected_command_index]
            if selected_talent in TALENT_DATA:
                talent_info = TALENT_DATA[selected_talent]

                # Prepare description lines for the 2x2 grid
                desc_lines = [
                    f"TYPE: {talent_info['type'].capitalize()}",
                    f"POWER: {talent_info['power']}",
                    f"COST: {talent_info['cost']}",
                    f"TARGET: {talent_info['target']}",
                ]

                # Draw the 2x2 grid
                grid_spacing_x = 130  # Horizontal spacing between grid items
                grid_spacing_y = 20  # Vertical spacing between grid items
                start_x = int(unit_talent_rec.x + padding)
                start_y = int(unit_talent_rec.y + padding)

                for i, line in enumerate(desc_lines):
                    grid_x = (
                        start_x + (i % 2) * grid_spacing_x
                    )  # Alternate between two columns
                    grid_y = (
                        start_y + (i // 2) * grid_spacing_y
                    )  # Move to the next row every two items
                    pr.draw_text(line, grid_x, grid_y, 16, pr.BLACK)

                # Wrap the talent's additional description
                talent_description = talent_info.get("desc", "No description available")
                max_line_width = 50  # Adjust maximum characters per line
                wrapped_desc_lines = [
                    talent_description[i : i + max_line_width]
                    for i in range(0, len(talent_description), max_line_width)
                ]

                # Draw the talent description below the grid
                desc_start_y = (
                    start_y + 2 * grid_spacing_y + 20
                )  # Offset below the grid
                for i, line in enumerate(wrapped_desc_lines):
                    pr.draw_text(
                        line,
                        start_x,  # Align with the left side of the grid
                        desc_start_y + i * grid_spacing_y,
                        16,
                        pr.DARKGRAY,
                    )
        # Innate Talent
        unit_innate_rec = pr.Rectangle(
            unit_rect.x + padding + 160, unit_rect.y + padding, 200, 50
        )
        pr.draw_rectangle_rec(unit_innate_rec, pr.ORANGE)

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
