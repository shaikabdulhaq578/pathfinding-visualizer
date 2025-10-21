import pygame
import sys
from node import Node
from algorithms import a_star, dijkstra

pygame.init()

# --- Window setup ---
WIDTH = 600
ROWS = 30
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Pathfinding Visualizer")

# --- Colors ---
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
BLACK = (0, 0, 0)

# --- Draw Text (Instructions + Title) ---
def draw_text(win, width, current_algorithm=None):
    pygame.font.init()
    font = pygame.font.SysFont("arial", 18, bold=True)
    title_font = pygame.font.SysFont("arial", 24, bold=True)

    # Title
    title = title_font.render("Pathfinding Visualizer", True, BLACK)
    win.blit(title, (width // 2 - title.get_width() // 2, 5))

    # Controls
    controls = [
        "Left Click: Set Start, End, or Walls",
        "Right Click: Erase Node",
        "SPACE: Run A* Algorithm",
        "D: Run Dijkstra's Algorithm",
        "C: Clear Grid"
    ]

    for i, text in enumerate(controls):
        line = font.render(text, True, (50, 50, 50))
        win.blit(line, (10, 35 + i * 22))

    # Current Algorithm Display
    if current_algorithm:
        algo_text = font.render(f"Running: {current_algorithm}", True, (0, 100, 200))
        win.blit(algo_text, (width - algo_text.get_width() - 10, width - 30))

# --- Grid and Drawing Functions ---
def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)
    return grid

def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))

def draw(win, grid, rows, width, current_algorithm=None):
    win.fill(WHITE)
    for row in grid:
        for node in row:
            node.draw(win)
    draw_grid(win, rows, width)
    draw_text(win, width, current_algorithm)
    pygame.display.update()

def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos
    row = y // gap
    col = x // gap
    return row, col

# --- Main Game Loop ---
def main(win, width):
    grid = make_grid(ROWS, width)
    start = None
    end = None
    run = True
    current_algorithm = None

    while run:
        draw(win, grid, ROWS, width, current_algorithm)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            # --- Mouse Controls ---
            if pygame.mouse.get_pressed()[0]:  # Left click
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                node = grid[row][col]
                if not start and node != end:
                    start = node
                    start.make_start()
                elif not end and node != start:
                    end = node
                    end.make_end()
                elif node != end and node != start:
                    node.make_barrier()

            elif pygame.mouse.get_pressed()[2]:  # Right click
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                node = grid[row][col]
                node.reset()
                if node == start:
                    start = None
                elif node == end:
                    end = None

            # --- Keyboard Controls ---
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:  # Clear grid
                    start = None
                    end = None
                    current_algorithm = None
                    grid = make_grid(ROWS, width)

                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)
                    current_algorithm = "A* Algorithm"
                    a_star(lambda: draw(win, grid, ROWS, width, current_algorithm), grid, start, end)
                    current_algorithm = None  # reset after run

                if event.key == pygame.K_d and start and end:
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)
                    current_algorithm = "Dijkstra's Algorithm"
                    dijkstra(lambda: draw(win, grid, ROWS, width, current_algorithm), grid, start, end)
                    current_algorithm = None  # reset after run

main(WIN, WIDTH)
