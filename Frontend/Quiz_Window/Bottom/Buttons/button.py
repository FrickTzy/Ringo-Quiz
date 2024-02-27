from pygame import Rect, draw
from Frontend.Settings import Colors
from .button_font import ButtonFont


class Button:
    __TEXT_COLOR = Colors.BLACK

    def __init__(self, color, display, index):
        self.__color = color
        self.__index = index
        self.__display = display
        self.__pos = ButtonPos(display=display, index=index)
        self.__font = ButtonFont(display=display, text_color=self.__TEXT_COLOR)
        self.__rect = Rect(self.__pos.button_x, self.__pos.button_y, self.__pos.button_width, self.__pos.button_height)

    def show_button(self, surface, text):
        draw.rect(surface, self.__color, self.__rect)
        self.__show_text(surface=surface, text=text)

    def check_if_clicked(self):
        if self.__rect.collidepoint(self.__display.get_mouse_pos()):
            return True
        return False

    def __show_text(self, surface, text):
        rendered_text = self.__font.render_text(text=text)
        text_rect = rendered_text.get_rect(center=self.__rect.center)
        surface.blit(rendered_text, text_rect)

    def update_button(self):
        self.__rect = Rect(self.__pos.button_x, self.__pos.button_y, self.__pos.button_width, self.__pos.button_height)
        self.__font.update_font()


class ButtonPos:
    __BUTTON_WIDTH_RATIO = 4.12
    __BUTTON_X_MARGIN_RATIO = 150
    __BUTTON_HEIGHT_RATIO = 2.0
    __BUTTON_Y_RATIO = 2.1

    def __init__(self, display, index):
        self.__display = display
        self.__index = index

    @property
    def button_width(self):
        return self.__display.width // self.__BUTTON_WIDTH_RATIO

    @property
    def button_x(self):
        return (self.button_width + self.__button_margin) * self.__index + self.__button_margin

    @property
    def button_y(self):
        return self.__display.height // self.__BUTTON_Y_RATIO

    @property
    def __button_margin(self):
        return self.__display.width // self.__BUTTON_X_MARGIN_RATIO

    @property
    def button_height(self):
        return self.__display.height // self.__BUTTON_HEIGHT_RATIO







