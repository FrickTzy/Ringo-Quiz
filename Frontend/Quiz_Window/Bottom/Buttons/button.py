from pygame import Rect, draw
from Frontend.Settings import Colors
from .button_font import ButtonFont


class Button:
    __TEXT_COLOR = Colors.WHITE

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
        rendered_text_list = self.__font.render_text(text=text, button_width=self.__pos.button_width)
        text_amount = len(rendered_text_list)
        for index, rendered_text in enumerate(rendered_text_list):
            text_size = rendered_text.get_size()
            surface.blit(rendered_text, self.__pos.get_text_pos(text_size=text_size, text_amount=text_amount,
                                                                current_index=index))

    def __simplified_show_text(self, surface, text):
        rendered_text_list = self.__font.render_text(text=text, button_width=self.__pos.button_width)
        for rendered_text in rendered_text_list:
            text_rect = rendered_text.get_rect(center=self.__rect.center)
            surface.blit(rendered_text, text_rect)

    def update_button(self):
        self.__rect = Rect(self.__pos.button_x, self.__pos.button_y, self.__pos.button_width, self.__pos.button_height)
        self.__font.update_font()


class ButtonEventHandler:
    __hovered = False

    def __init__(self, sfx_manager, display):
        self.__sfx_manager = sfx_manager
        self.__display = display

    def check_button_events(self, rect):
        self.__check_if_hover(rect=rect)

    def __check_if_hover(self, rect):
        if not rect.collidepoint(self.__display.get_mouse_pos()):
            self.__hovered = False
            return
        if not self.__hovered:
            self.__hovered = True
            self.__sfx_manager.play_hover_sfx()


class ButtonPos:
    __BUTTON_WIDTH_RATIO = 4.12
    __BUTTON_X_MARGIN_RATIO = 150
    __BUTTON_HEIGHT_RATIO = 2.0
    __BUTTON_Y_RATIO = 2.05
    __TEXT_PADDING_RATIO = 4

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

    def get_text_pos(self, text_size, text_amount, current_index):
        text_width, text_height = text_size
        return self.__get_text_x(text_width=text_width), self.__get_text_y(text_height=text_height,
                                                                           text_amount=text_amount,
                                                                           current_index=current_index)

    def __get_text_x(self, text_width):
        return self.button_x + (self.button_width - text_width) // 2

    def __get_text_y(self, text_height, text_amount, current_index):
        text_padding = self.__get_text_padding(text_height=text_height)
        total_text_height = (text_height * text_amount) + (text_padding * (text_amount - 1))
        starting_y = (self.button_height - total_text_height) // 2
        text_y = starting_y + (text_height * current_index) + (text_padding * current_index)
        return self.button_y + text_y

    def __get_text_padding(self, text_height):
        return text_height // self.__TEXT_PADDING_RATIO










