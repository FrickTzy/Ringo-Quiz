from pygame import font


class ButtonFont:
    __FONT_SIZE_RATIO = 30
    __TEXT_PADDING = 50

    def __init__(self, display, text_color):
        self.__display = display
        self.__text_color = text_color
        self.__font = font.SysFont("arialblack", 40)

    def render_text(self, text: str, button_width):
        text_list = self.__check_if_move_to_second_line(text=text, button_width=button_width)
        return [self.__font.render(text, True, self.__text_color) for text in text_list]

    def __check_if_move_to_second_line(self, text: str, button_width: int):
        if not self.__get_text_width(text=text) >= button_width - self.__TEXT_PADDING:
            return [text]
        if " " in text:
            return text.split()

    def __get_text_width(self, text):
        return self.__font.size(text)[0]

    def update_font(self):
        self.__font = font.SysFont("arialblack", self.__get_size)

    @property
    def __get_size(self):
        return self.__display.height // self.__FONT_SIZE_RATIO
