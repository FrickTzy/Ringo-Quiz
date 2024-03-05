from Frontend.Settings import Colors
from .button import Button


class ButtonManager:
    __BUTTON_COLORS = [Colors.QUIZ_BLUE, Colors.QUIZ_CYAN, Colors.QUIZ_YELLOW, Colors.QUIZ_RED]
    __button_list = []

    def __init__(self, display, sfx_manager):
        self.__init_buttons(display=display, sfx_manager=sfx_manager)

    def __init_buttons(self, display, sfx_manager):
        for index, color in enumerate(self.__BUTTON_COLORS):
            self.__button_list.append(Button(color=color, index=index, display=display, sfx_manager=sfx_manager))

    def show_buttons(self, surface, choices: dict):
        for index, button in enumerate(self.__button_list):
            button.show_button(surface=surface, text=choices[index]["choice"])

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
