import pygame

import colors


class Drawing:
    FONT = pygame.font.SysFont(None, 32)
    PADDING = 50  # padding from one horizontal side of the window in pixels
    TOP_PADDING = 100  # padding from the top of the window in pixels

    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((self.width, self.height))

    def set_list(self, list):
        self.list = list
        self.maximum_value = max(self.list)
        self.minimum_value = min(self.list)
        self.block_width = max((self.width - (self.PADDING * 2)) / len(self.list), 1)
        self.block_height = round(
            (self.height - self.TOP_PADDING) / (self.maximum_value - self.minimum_value)
        )
        self.blocks_start = self.PADDING
        self.blocks_end = self.width - self.PADDING

        # checks for any blocks that may go out of bounds, issue to be fixed
        # for index, _ in enumerate(self.list):
        #     x = self.blocks_start + (index * self.block_width)
        #     if (x > self.blocks_end):
        #         warnings.warn("There is block(s) that is out of bounds!")
        #         break

    def set_text(self, text):
        rendered_text = self.FONT.render(text, True, colors.BLACK)
        self.window.blit(
            rendered_text,
            ((self.width / 2) - (rendered_text.get_width() / 2), 20),
        )

    def draw_list(self, color_blocks={}):
        for index, value in enumerate(self.list):
            x = self.blocks_start + (index * self.block_width)
            y = (self.height) - ((value) * self.block_height)
            width = self.block_width
            height = value * self.block_height
            color = colors.BLACK
            if index in color_blocks:
                color = color_blocks[index]
            pygame.draw.rect(self.window, color, (x, y, width, height))