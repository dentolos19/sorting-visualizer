import random

import pygame

from algorithms import Algorithms
from colors import Colors
from drawing import Drawing


def generate_list(length, minimum_value=0, maximum_value=100):
    return [random.randint(minimum_value, maximum_value) for _ in range(length)]


def main():
    pygame.init()

    running = True
    sorting = False

    drawing = Drawing(800, 600)
    drawing.set_list(generate_list(100))

    sorting_algorithm = Algorithms.bubble_sort
    sorting_algorithm_generator = None

    clock = pygame.time.Clock()

    while running:
        clock.tick(60)

        drawing.window.fill(Colors.WHITE)

        if sorting:
            try:
                drawing.draw_list(next(sorting_algorithm_generator))
            except StopIteration:
                sorting = False
                sorting_algorithm_generator = None
        else:
            drawing.draw_list()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type != pygame.KEYDOWN:
                continue
            if event.key == pygame.K_r:
                drawing.set_list(generate_list(100))
                sorting = False
            elif event.key == pygame.K_SPACE:
                if not sorting:
                    sorting = True
                    sorting_algorithm_generator = sorting_algorithm(drawing.list)
                else:
                    sorting = False


    pygame.quit()


if __name__ == "__main__":
    main()