class ButtonColorManager:
    def __init__(self, initial_color):
        self.__initial_color = initial_color
        self.__current_color = initial_color

    @property
    def current_color(self):
        return self.__current_color

    def set_color(self, current_color_rgb: tuple):
        self.__current_color = current_color_rgb
