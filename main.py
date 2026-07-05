import random

import pygame

import algorithms
import colors

LIST_LENGTH = 200
ALGORITHMS = (
    (pygame.K_1, "Bubble Sort", algorithms.bubble_sort),
    (pygame.K_2, "Insertion Sort", algorithms.insertion_sort),
    (pygame.K_3, "Selection Sort", algorithms.selection_sort),
    (pygame.K_4, "Heap Sort", algorithms.heap_sort),
    (pygame.K_5, "Merge Sort", algorithms.merge_sort),
    (pygame.K_6, "Quick Sort", algorithms.quick_sort),
    (pygame.K_7, "Shell Sort", algorithms.shell_sort),
)


def generate_list(length, minimum_value=0, maximum_value=100):
    return [random.randint(minimum_value, maximum_value) for _ in range(length)]


def main():
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Sortinator")
    pygame.display.set_icon(pygame.image.load("icon.ico"))

    from drawing import Drawing

    running = True
    sorting = False

    drawing = Drawing(800, 600)
    drawing.set_list(generate_list(LIST_LENGTH))

    _, sorting_algorithm_name, sorting_algorithm = ALGORITHMS[0]
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
                drawing.draw_list(next(sorting_algorithm_generator))  # type: ignore
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
                if event.key == pygame.K_r:
                    drawing.set_list(generate_list(LIST_LENGTH))
                    sorting = False
                    sorting_algorithm_generator = None
                elif event.key == pygame.K_SPACE:
                    if not sorting:
                        sorting_algorithm_generator = sorting_algorithm(drawing.list)
                        sorting = True
                    else:
                        sorting = False
                elif not sorting:
                    for key, algorithm_name, algorithm in ALGORITHMS:
                        if event.key == key:
                            sorting_algorithm = algorithm
                            sorting_algorithm_name = algorithm_name
                            break

    pygame.quit()


if __name__ == "__main__":
    main()
