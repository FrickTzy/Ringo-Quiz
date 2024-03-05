from pygame import Surface, SRCALPHA
from .Buttons import ButtonManager


class BottomDiv:
    def __init__(self, display, answer_manager, sfx_manager):
        self.__display = display
        self.__sfx_manager = sfx_manager
        self.__bottom_surface = Surface(display.get_window_size, SRCALPHA)
        self.__button_manager = ButtonManager(display=display, sfx_manager=sfx_manager)
        self.__answer_manager = answer_manager

    def show(self):
        self.__button_manager.show_buttons(surface=self.__bottom_surface, choices=self.__answer_manager.choices)
        self.__display.window.blit(self.__bottom_surface, (0, 0))

    def __debug(self):
        print(f"{self.__answer_manager.choices}: {self.__answer_manager.anime_title}")

    def check_if_clicked_buttons(self):
        clicked, index = self.__button_manager.check_if_clicked()
        if not clicked:
            return False
        print(self.__answer_manager.check_if_correct_answer(index=index))
        self.__sfx_manager.play_hit_sfx()
        return True

    def update(self):
        self.__bottom_surface = Surface(self.__display.get_window_size, SRCALPHA)
        self.__button_manager.update()



