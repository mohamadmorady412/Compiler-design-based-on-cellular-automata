import pygame
import random
import time

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

square_size = 20
squares = {}

for x in range(0, width, square_size):
    for y in range(0, height, square_size):
        squares[(x, y)] = random.choice([True, False])

def draw_squares():
    for (x, y), alive in squares.items():
        color = WHITE if alive else BLACK
        pygame.draw.rect(screen, color, (x, y, square_size, square_size))

def update_squares():
    new_squares = {}
    for x in range(0, width, square_size):
        for y in range(0, height, square_size):
            neighbors = 0
            for nx in range(-square_size, square_size * 2, square_size):
                for ny in range(-square_size, square_size * 2, square_size):
                    if (nx, ny) != (0, 0) and squares.get((x + nx, y + ny)):
                        neighbors += 1

            if squares[(x, y)]:
                # If the square is alive and not next to two other squares, it dies after three seconds
                new_squares[(x, y)] = neighbors == 2 or time.time() - squares[(x, y)] < 3
            else:
                # If the square is dead and adjacent to three squares, it is fired
                new_squares[(x, y)] = neighbors == 3

    return new_squares

running = True
while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_squares()
    squares = update_squares()
    pygame.display.flip()
    clock.tick(10)

pygame.quit()
quit()