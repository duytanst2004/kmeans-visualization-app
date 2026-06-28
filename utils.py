import math
import pygame
from config import X, Y, BLACK
from button import TextButton


def distance(p1, p2):
    """Euclidean distance between two 2-D points."""
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)


def build_buttons(screen, font, K, error):
    """
    Create the sidebar button list and render the dynamic labels
    (K counter, error value).  Returns the list of TextButton objects
    in the same order the caller indexes them:
      0 → "+"
      1 → "-"
      2 → "Run"
      3 → "Random"
      4 → "Algorithm"
      5 → "Reset"
    """
    base_names = ["+", "Run", "Random", "", "Algorithm", "Reset"]
    buttons = []

    for i, name in enumerate(base_names):
        btn = TextButton(name, X, Y + i * 75, 120, 40)
        buttons.append(btn)

    # Shrink "+" button and inject "-" right after it
    buttons[0].width = 40
    btn_minus = TextButton("-", X + 80, Y, 40, 40)
    buttons.insert(1, btn_minus)          # index 1 = "-"

    # Render "K = N" next to the +/- buttons
    text_k = font.render("K = " + str(K), True, BLACK)
    screen.blit(text_k, (X + 80 * 2, Y))

    buttons[4].width, buttons[4].height = 0, 0
    text_error = font.render("Error = " + str(error), True, BLACK)
    screen.blit(text_error, (X, Y + 75 * 3))

    return buttons
    # Final order:  0=+  1=-  2=Run  3=Random  4=Error  5=Algorithm  6=Reset
