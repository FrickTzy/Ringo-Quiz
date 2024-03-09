from pygame import Rect, draw
from Frontend.Settings import Colors
from .button_color_manager import ButtonColorManager
from .button_font import ButtonFont
from .button_animation import ButtonAnimation


class Button:
    __TEXT_COLOR = Colors.WHITE

    def __init__(self, color, display, index, sfx_manager):
        self.__color_manager = ButtonColorManager(initial_color=color)
        self.__index = index
        self.__display = display
        self.__correct_answer_manager = CorrectAnswerManager()
        self.__pos = ButtonPos(display=display, index=index)
        self.__font = ButtonFont(display=display, text_color=self.__TEXT_COLOR)
        self.__rect = Rect(self.__pos.button_x, self.__pos.button_y, self.__pos.button_width, self.__pos.button_height)
        self.__event_handler = ButtonEventHandler(sfx_manager, display=display)
        self.__correct_answer_manager = CorrectAnswerManager()
        self.__animation_manager = ButtonAnimation(button_pos=self.__pos, color_manager=self.__color_manager,
                                                   correct_answer_manager=self.__correct_answer_manager)

    def show_button(self, surface, text, finished_clicking):
        self.__animation_manager.check_for_animations(in_animation=finished_clicking)
        self.__draw_rect(surface=surface)
        self.__show_text(surface=surface, text=text)
        self.__event_handler.check_button_events(rect=self.__rect)

    def set_if_correct_answer(self, is_correct_answer):
        self.__correct_answer_manager.is_correct_answer = is_correct_answer

    def __draw_rect(self, surface):
        self.__update_rect()
        draw.rect(surface, self.__color_manager.current_color, self.__rect)

    def check_if_hover(self):
        return self.__event_handler.check_if_hover(rect=self.__rect)

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
        self.__update_rect()
        self.__font.update_font()

    def __update_rect(self):
        self.__rect.x, self.__rect.y = self.__pos.button_x, self.__pos.button_y
        self.__rect.width, self.__rect.height = self.__pos.button_width, self.__pos.button_height

    @property
    def finished_animation(self):
        return self.__animation_manager.finished_animation


class ButtonEventHandler:
    __hovered = False

    def __init__(self, sfx_manager, display):
        self.__sfx_manager = sfx_manager
        self.__display = display

    def check_button_events(self, rect):
        self.__check_if_hover_sfx(rect=rect)

    def check_if_hover(self, rect):
        if rect.collidepoint(self.__display.get_mouse_pos()):
            return True
        return False

    def __check_if_hover_sfx(self, rect):
        if not self.check_if_hover(rect=rect):
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
        self.__button_height = self.initial_button_height
        self.__button_y = self.initial_button_y

    @property
    def button_width(self):
        return self.__display.width // self.__BUTTON_WIDTH_RATIO

    @property
    def button_x(self):
        return (self.button_width + self.__button_margin) * self.__index + self.__button_margin

    @property
    def button_y(self):
        return self.__button_y

    @property
    def initial_button_y(self):
        return self.__display.height // self.__BUTTON_Y_RATIO

    @property
    def __button_margin(self):
        return self.__display.width // self.__BUTTON_X_MARGIN_RATIO

    @property
    def initial_button_height(self):
        return self.__display.height // self.__BUTTON_HEIGHT_RATIO

    @property
    def button_height(self):
        return self.__button_height

    def set_button_y(self, button_y):
        self.__button_y = button_y

    @property
    def correct_target_y(self):
        return self.initial_button_y - self.initial_button_y // 15

    @property
    def wrong_target_y(self):
        return self.initial_button_y + self.initial_button_y // 20

    @property
    def target_height(self):
        return self.initial_button_height + self.initial_button_y // 5

    def set_button_height(self, button_height):
        self.__button_height = button_height

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


class CorrectAnswerManager:
    is_correct_answer = False

