from colors import *
from config import *


class Text:
    def __init__(self, text, text_point, font_type, font_color, text_background_color, size):
        self.text = text
        self.text_point = text_point

        self.font_type = font_type
        self.font_color = font_color
        self.text_background_color = text_background_color
        self.size = size


def text_rendering(text, front_color, back_color, textRect_center, font):
    text = font.render(text, True, front_color, back_color)
    textRect = text.get_rect()
    textRect.center = textRect_center

    WIN.blit(text, textRect)