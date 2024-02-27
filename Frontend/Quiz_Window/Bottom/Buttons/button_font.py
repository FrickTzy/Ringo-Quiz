from pygame import font


class ButtonFont:
    __FONT_SIZE_RATIO = 30

    def __init__(self, display, text_color):
        self.__display = display
        self.__text_color = text_color
        self.__font = font.SysFont("arialblack", 40)

    def render_text(self, text):
        return self.__font.render(text, True, self.__text_color)

    def update_font(self):
        self.__font = font.SysFont("arialblack", self.__get_size)

    @property
    def __get_size(self):
        return self.__display.height // self.__FONT_SIZE_RATIO
