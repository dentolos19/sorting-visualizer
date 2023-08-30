import random

import pygame
from algorithms import Algorithms
from colors import Colors
from visuals import Visuals

pygame.init()


def generate_list(length, minimum_value=0, maximum_value=100):
    return [random.randint(minimum_value, maximum_value) for _ in range(length)]


def draw_list(view: Visuals, color_blocks={}):
    for index, value in enumerate(view.list):
        x = view.blocks_start + (index * view.block_width)
        y = (view.height) - ((value) * view.block_height)
        width = view.block_width
        height = value * view.block_height
        color = Colors.BLACK
        if index in color_blocks:
            color = color_blocks[index]
        pygame.draw.rect(view.window, color, (x, y, width, height))


def main():
    running = True
    sorting = False
    clock = pygame.time.Clock()
    drawing = Visuals(800, 600)
    drawing.set_list(generate_list(100))

    sorting_algorithm = Algorithms.bubble_sort
    sorting_algorithm_generator = None

    while running:
        clock.tick(60)

        drawing.window.fill(Colors.WHITE)

        if sorting:
            try:
                color = next(sorting_algorithm_generator)
                draw_list(drawing, color)
            except StopIteration:
                sorting = False
                sorting_algorithm_generator = None
        else:
            draw_list(drawing)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type != pygame.KEYDOWN:
                continue
            if event.key == pygame.K_r:
                drawing.set_list(generate_list(100))
                sorting = False
            elif event.key == pygame.K_SPACE and not sorting:
                sorting = True
                sorting_algorithm_generator = sorting_algorithm(drawing.list)

    pygame.quit()


if __name__ == "__main__":
    main()