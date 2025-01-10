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
