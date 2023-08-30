import pygame

from colors import Colors


class Drawing:
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

    def draw_list(self, color_blocks={}):
        for index, value in enumerate(self.list):
            x = self.blocks_start + (index * self.block_width)
            y = (self.height) - ((value) * self.block_height)
            width = self.block_width
            height = value * self.block_height
            color = Colors.BLACK
            if index in color_blocks:
                color = color_blocks[index]
            pygame.draw.rect(self.window, color, (x, y, width, height))