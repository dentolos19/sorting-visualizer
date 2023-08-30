import pygame


class Visuals:
    PADDING = 50  # padding from one horizontal side of the window in pixels
    TOP_PADDING = 100  # padding from the top of the window in pixels

    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Sorting Visualizer")

    def set_list(self, list):
        self.list = list
        self.maximum_value = max(self.list)
        self.minimum_value = min(self.list)
        self.block_width = round((self.width - (self.PADDING * 2)) / len(self.list))
        self.block_height = round(
            (self.height - self.TOP_PADDING) / (self.maximum_value - self.minimum_value)
        )
        self.blocks_start = self.PADDING
        self.blocks_end = self.width - self.PADDING