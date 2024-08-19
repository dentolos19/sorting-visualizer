import random

import algorithms
import colors
import pygame

LIST_LENGTH = 200


def generate_list(length, minimum_value=0, maximum_value=100):
    return [random.randint(minimum_value, maximum_value) for _ in range(length)]


def main():
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Sorting Visualizer")
    pygame.display.set_icon(pygame.image.load("public/icon.png"))

    from drawing import Drawing

    running = True
    sorting = False

    drawing = Drawing(800, 600)
    drawing.set_list(generate_list(LIST_LENGTH))

    sorting_algorithm = algorithms.bubble_sort
    sorting_algorithm_name = "Bubble Sort"
    sorting_algorithm_generator = None

    clock = pygame.time.Clock()

    while running:
        clock.tick(60)

        drawing.window.fill(colors.WHITE)
        drawing.draw_text(f"Current Algorithm: {sorting_algorithm_name}")

        if sorting:
            try:
                # draw the next step of the sorting algorithm
                # e.g. the green and red blocks which indicate the current comparison
                drawing.draw_list(next(sorting_algorithm_generator))
            except StopIteration:
                # if the sorting is done, stop sorting and reset the generator
                sorting = False
                sorting_algorithm_generator = None
        else:
            # if not sorting, simply draw the list
            drawing.draw_list()

        # update the display to show the overall changes
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                key = pygame.key.get_pressed()
                # modifier = pygame.key.get_mods()
                if key[pygame.K_r]:
                    drawing.set_list(generate_list(LIST_LENGTH))
                    sorting = False
                elif key[pygame.K_SPACE]:
                    if not sorting:
                        sorting_algorithm_generator = sorting_algorithm(drawing.list)
                        sorting = True
                    else:
                        sorting = False
                elif key[pygame.K_1] and not sorting:
                    sorting_algorithm = algorithms.bubble_sort
                    sorting_algorithm_name = "Bubble Sort"
                elif key[pygame.K_2] and not sorting:
                    sorting_algorithm = algorithms.insertion_sort
                    sorting_algorithm_name = "Insertion Sort"
                elif key[pygame.K_3] and not sorting:
                    sorting_algorithm = algorithms.selection_sort
                    sorting_algorithm_name = "Selection Sort"
                elif key[pygame.K_4] and not sorting:
                    sorting_algorithm = algorithms.heap_sort
                    sorting_algorithm_name = "Heap Sort"

    pygame.quit()


if __name__ == "__main__":
    main()