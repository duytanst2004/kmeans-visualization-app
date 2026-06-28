import pygame

from config import (
    SCREEN_WIDTH, SCREEN_HEIGHT,
    BACKGROUND, BLACK, WHITE, BACKGROUND_PANEL,
    COLORS, PANEL,
    FONT_SIZE, FONT_SIZE_MOUSE,
)
from utils import build_buttons
from kmeans_handler import (
    random_clusters, run_step, run_sklearn, calc_error,
)

# Pygame init
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("KMeans Visualisation")
clock  = pygame.time.Clock()
font        = pygame.font.SysFont("sans", FONT_SIZE)
font_mouse  = pygame.font.SysFont("sans", FONT_SIZE_MOUSE)

# State
K        = 0
error    = 0
points   = []
clusters = []
labels   = []

running  = True

# Helpers
def inside_panel(x, y):
    px, py, pw, ph = PANEL
    return px < x < px + pw and py < y < py + ph

# Main loop
while running:
    clock.tick(60)
    screen.fill(BACKGROUND)

    # --- Draw background panel ---
    pygame.draw.rect(screen, BLACK, (50, 50, 700, 500))
    pygame.draw.rect(screen, BACKGROUND_PANEL, PANEL)

    # --- Build & draw sidebar buttons ---
    buttons = build_buttons(screen, font, K, error)
    for btn in buttons:
        btn.draw(screen, font)

    # --- Mouse-position tooltip ---
    mx, my = pygame.mouse.get_pos()
    if inside_panel(mx, my):
        tip = font_mouse.render(
            "({}, {})".format(mx - PANEL[0], my - PANEL[1]), True, BLACK
        )
        screen.blit(tip, (mx + 10, my - 5))

    # --- Events ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Add a point inside the drawing panel
            if inside_panel(mx, my):
                labels = []
                points.append([mx - PANEL[0], my - PANEL[1]])

            # Button "+"  → increase K
            if buttons[0].is_hovered() and K < len(COLORS):
                K += 1

            # Button "-"  → decrease K
            if buttons[1].is_hovered() and K > 0:
                K -= 1

            # Button "Run"  → one E/M step
            if buttons[2].is_hovered() and clusters:
                clusters, labels = run_step(points, clusters, K)

            # Button "Random"  → initialise random cluster centres
            if buttons[3].is_hovered():
                clusters = random_clusters(K, PANEL)
                labels   = []
                error    = 0

            # Button "Algorithm"  → run scikit-learn KMeans
            if buttons[5].is_hovered():
                try:
                    clusters, labels = run_sklearn(points, K)
                except Exception as exc:
                    print("KMeans error:", exc)

            # Button "Reset"  → clear everything
            if buttons[6].is_hovered():
                K        = 0
                error    = 0
                points   = []
                clusters = []
                labels   = []

    # --- Draw cluster centres ---
    for i, c in enumerate(clusters):
        pygame.draw.circle(
            screen, COLORS[i],
            (int(c[0]) + PANEL[0], int(c[1]) + PANEL[1]), 6
        )

    # --- Draw data points ---
    for i, p in enumerate(points):
        pos = (p[0] + PANEL[0], p[1] + PANEL[1])
        if labels:
            pygame.draw.circle(screen, COLORS[labels[i]], pos, 4)
        else:
            pygame.draw.circle(screen, BLACK, pos, 4)
            pygame.draw.circle(screen, WHITE, pos, 3)

    # --- Update error metric ---
    if clusters and labels:
        error = calc_error(points, clusters, labels)

    pygame.display.flip()

pygame.quit()
