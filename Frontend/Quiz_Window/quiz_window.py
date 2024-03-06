from pygame import event as pyevent, MOUSEBUTTONDOWN
from threading import Thread
from Frontend.Helper_Files import Display, WindowManager, SFXManager
from Backend import AnswerManager
from .Bottom import BottomDiv
from .Top import TopDiv


class QuizWindow:
    def __init__(self, display: Display, window_manager: WindowManager, music):
        self.__display = display
        self.__music = music
        self.__window_manager = window_manager
        self.__init_manager = InitManager()
        self.__answer_manager = AnswerManager()
        self.__sfx_manager = SFXManager()
        self.__top_div = TopDiv(display=display, answer_manager=self.__answer_manager, init_manager=self.__init_manager)
        self.__bottom_div = BottomDiv(display=display, answer_manager=self.__answer_manager,
                                      sfx_manager=self.__sfx_manager, init_manager=self.__init_manager)
        self.__event_handler = QuizWindowEventHandler(window_manager=window_manager, bottom_div=self.__bottom_div,
                                                      top_div=self.__top_div, display=display,
                                                      init_manager=self.__init_manager)

    def run(self):
        self.__check_if_init()
        self.__event_handler.check_for_events()
        self.__music.check_if_song_finished()
        self.__show_div()

    def __show_div(self):
        if self.__init_manager.check_if_first_init():
            return
        self.__top_div.show()
        self.__bottom_div.show()

    def __check_if_init(self):
        if self.__init_manager.check_if_init():
            Thread(target=self.__init).start()

    def __init(self):
        self.__answer_manager.initialize()
        self.__top_div.set_image(anime_title=self.__answer_manager.anime_title,
                                 character_name=self.__answer_manager.chosen_character_name)
        self.__answer_manager.set_choices()
        self.__event_handler.update()
        self.__init_manager.finish_init()


class QuizWindowEventHandler:
    def __init__(self, window_manager: WindowManager, bottom_div: BottomDiv, top_div: TopDiv, display, init_manager):
        self.__window_manager = window_manager
        self.__bottom_div = bottom_div
        self.__display = display
        self.__top_div = top_div
        self.__init_manager = init_manager

    def check_for_events(self):
        self.__check_if_resize()
        for event in pyevent.get():
            self.__window_manager.check_if_quit(event=event)
            self.__check_if_clicked(event=event)

    def __check_if_resize(self):
        if self.__display.check_if_change_window_size():
            self.update()

    def __check_if_clicked(self, event):
        if not event.type == MOUSEBUTTONDOWN:
            return
        if not self.__bottom_div.check_if_clicked_buttons():
            return
        self.__init_manager.reset()

    def update(self):
        self.__top_div.update()
        self.__bottom_div.update()


class InitManager:
    __initialized = False
    __finished_init = False
    __first_init = True

    def reset(self):
        self.__finished_init = False
        self.__initialized = False

    def deep_reset(self):
        self.reset()
        self.__first_init = True

    def set_initialized(self):
        self.__initialized = True

    def check_if_init(self):
        if self.__initialized:
            return False
        self.__initialized = True
        return True

    def finish_init(self):
        self.__finished_init = True
        self.__first_init = False

    def check_if_finished_init(self):
        return self.__finished_init

    def check_if_first_init(self):
        return self.__first_init




