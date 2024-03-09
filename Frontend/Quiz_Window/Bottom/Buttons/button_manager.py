from Frontend.Settings import Colors
from .button import Button


class ButtonManager:
    __BUTTON_COLORS = [Colors.QUIZ_BLUE, Colors.QUIZ_CYAN, Colors.QUIZ_YELLOW, Colors.QUIZ_RED]

    def __init__(self, display, sfx_manager, animation_notifier):
        self.__button_list = []
        self.__animation_notifier = animation_notifier
        self.__init_buttons(display=display, sfx_manager=sfx_manager)

    def __init_buttons(self, display, sfx_manager):
        for index, color in enumerate(self.__BUTTON_COLORS):
            self.__button_list.append(Button(color=color, index=index, display=display, sfx_manager=sfx_manager))

    def show_buttons(self, surface, choices: dict):
        for index, button in enumerate(self.__button_list):
            button.show_button(surface=surface, text=choices[index]["choice"],
                               finished_clicking=self.__animation_notifier.animation_running)

    def set_correct_answers(self, correct_index):
        for index, button in enumerate(self.__button_list):
            is_correct_answer = False
            if index == correct_index:
                is_correct_answer = True
            button.set_if_correct_answer(is_correct_answer=is_correct_answer)

    def check_if_clicked(self):
        clicked, index_clicked = False, None
        for index, button in enumerate(self.__button_list):
            if not button.check_if_hover():
                continue
            clicked, index_clicked = True, index
        return clicked, index_clicked

    def update(self):
        for button in self.__button_list:
            button.update_button()
