import random

import pygame

import algorithms
import colors


def generate_list(length, minimum_value=0, maximum_value=100):
    return [random.randint(minimum_value, maximum_value) for _ in range(length)]


def main():
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Sorting Visualizer")
    pygame.display.set_icon(pygame.image.load("docs/icon.png"))

    from drawing import Drawing

    running = True
    sorting = False

    drawing = Drawing(800, 600)
    drawing.set_list(generate_list(100))

    sorting_algorithm = algorithms.bubble_sort
    sorting_algorithm_name = "Bubble Sort"

    clock = pygame.time.Clock()

    while running:
        clock.tick(60)

        drawing.window.fill(colors.WHITE)
        drawing.set_text(f"Current Algorithm: {sorting_algorithm_name}")

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
            if event.type == pygame.KEYDOWN:
                key = pygame.key.get_pressed()
                modifier = pygame.key.get_mods()
                if key[pygame.K_r]:
                    drawing.set_list(generate_list(100))
                    sorting = False
                elif key[pygame.K_SPACE]:
                    if not sorting:
                        sorting_algorithm_generator = sorting_algorithm(drawing.list)
                        sorting = True
                    else:
                        sorting = False
                elif modifier & pygame.KMOD_LCTRL and key[pygame.K_1] and not sorting:
                    sorting_algorithm = algorithms.bubble_sort
                    sorting_algorithm_name = "Bubble Sort"
                elif modifier & pygame.KMOD_LCTRL and key[pygame.K_2] and not sorting:
                    sorting_algorithm = algorithms.insertion_sort
                    sorting_algorithm_name = "Insertion Sort"
                elif modifier & pygame.KMOD_LCTRL and key[pygame.K_3] and not sorting:
                    sorting_algorithm = algorithms.selection_sort
                    sorting_algorithm_name = "Selection Sort"

    pygame.quit()


if __name__ == "__main__":
    main()