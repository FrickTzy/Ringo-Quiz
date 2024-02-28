from pygame import display, image, mouse, cursors, FULLSCREEN, RESIZABLE as PYRES
from os import path
from Frontend.Settings import WIDTH, HEIGHT, FULL_SCREEN_VIEW, RESIZABLE, WINDOW_NAME


class Display:
    __LOGO_FILE = "Purps.png"
    __FULL_SCREEN_VIEW = FULL_SCREEN_VIEW
    __RESIZABLE = RESIZABLE

    def __init__(self):
        self.__width, self.__height = WIDTH, HEIGHT
        self.__window = self.__set_display()
        self.__check_full_screen()
        self.__set_title()

    def __set_display(self):
        return display.set_mode((self.__width, self.__height), PYRES if self.__RESIZABLE else None)

    def __set_logo(self):
        logo_image = image.load(path.join("Frontend\Mania_Window\Img", self.__LOGO_FILE)).convert_alpha()
        display.set_icon(logo_image)

    @staticmethod
    def show_cursor(show=True):
        mouse.set_visible(show)

    @staticmethod
    def __set_title():
        display.set_caption(WINDOW_NAME)

    def __check_full_screen(self, full_screen=False):
        if self.__FULL_SCREEN_VIEW or full_screen:
            self.__width, self.__height = 1600, 900
            self.__window = display.set_mode((self.__width, self.__height), FULLSCREEN)
            mouse.set_cursor(cursors.arrow)

    @property
    def get_window_size(self):
        return self.__width, self.__height

    @staticmethod
    def get_mouse_pos():
        return mouse.get_pos()

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @property
    def center(self) -> tuple[int, int]:
        return self.__width // 2, self.__height // 2

    @staticmethod
    def center_window_element(width, element_width):
        return width - element_width / 2

    def check_if_change_window_size(self) -> bool:
        width, height = self.__window.get_size()
        changed_window_size = width != self.__width or height != self.__height
        if changed_window_size:
            self.__width, self.__height = width, height
            return True
        else:
            return False

    @property
    def window(self):
        return self.__window
