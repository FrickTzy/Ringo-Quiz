from pygame import Surface, SRCALPHA
from .Buttons import ButtonManager


class BottomDiv:
    def __init__(self, display, answer_manager, sfx_manager, init_manager):
        self.__display = display
        self.__sfx_manager = sfx_manager
        self.__bottom_surface = Surface(display.get_window_size, SRCALPHA)
        self.__button_manager = ButtonManager(display=display, sfx_manager=sfx_manager)
        self.__answer_manager = answer_manager
        self.__event_handler = BottomDivEventHandler(init_manager=init_manager, button_manager=self.__button_manager)

    def show(self):
        self.__event_handler.check_for_events()
        self.__clear_surface()
        self.__button_manager.show_buttons(surface=self.__bottom_surface, choices=self.__answer_manager.choices)
        self.__display.window.blit(self.__bottom_surface, (0, 0))

    def __clear_surface(self):
        self.__bottom_surface.fill((0, 0, 0, 0))

    def __debug(self):
        print(f"{self.__answer_manager.choices}: {self.__answer_manager.anime_title}")

    def check_if_clicked_buttons(self):
        clicked, index = self.__button_manager.check_if_clicked()
        if not clicked:
            return False
        self.__sfx_manager.play_hit_sfx()
        return True

    def __print_if_correct_answer(self, index):
        print(self.__answer_manager.check_if_correct_answer(index=index))

    def update(self):
        self.__bottom_surface = Surface(self.__display.get_window_size, SRCALPHA)
        self.__button_manager.update()


class BottomDivEventHandler:
    __finished_init = False

    def __init__(self, init_manager, button_manager):
        self.__init_manager = init_manager
        self.__button_manager = button_manager

    def check_for_events(self):
        self.__check_for_animations()

    def __check_for_animations(self):
        if (finished_init := self.__init_manager.check_if_finished_init()) == self.__finished_init:
            return
        if not finished_init:
            self.__button_manager.set_animation_after_clicking()
        else:
            self.__button_manager.reset_animation()
        self.__finished_init = finished_init



