from pygame import transform
from .character_image_animation import CharacterImageAnimation


class CharacterImage:
    __ERROR_MESSAGE = "Haven't loaded image yet!"
    __original_image = None
    __used_image = None

    def __init__(self, display):
        self.__image_pos = CharacterImagePos(display=display)
        self.__size_manager = CharacterImageSizeManager(display=display)
        self.__animation_manager = CharacterImageAnimation(image_pos=self.__image_pos, image_size=self.__size_manager)

    def show(self, surface, finished_clicking, correct_index):
        self.__check_if_loaded_image()
        self.__animation_manager.check_for_animations(in_animation=finished_clicking, correct_index=correct_index)
        self.__check_if_update_image()
        surface.blit(self.__used_image, self.__image_pos.get_coord(image_width=self.__size_manager.width))

    def __check_if_update_image(self):
        if not self.__animation_manager.finished_animation:
            self.__update_image()

    def __check_if_loaded_image(self):
        if self.__used_image is None:
            raise Exception(self.__ERROR_MESSAGE)

    def set_image(self, image):
        self.__original_image = image

    def update(self):
        self.__size_manager.update_size()
        self.__update_image()

    def __update_image(self):
        self.__used_image = transform.scale(self.__original_image, self.__size_manager.get_size)


class CharacterImagePos:
    __X_RATIO, __Y_RATIO = 2, 39.5

    def __init__(self, display):
        self.__display = display

    def get_coord(self, image_width):
        return self.__x - (image_width // 2), self.__y

    @property
    def __x(self):
        return self.__display.width // self.__X_RATIO

    @property
    def __y(self):
        return self.__display.height // self.__Y_RATIO


class CharacterImageSizeManager:
    __WIDTH_RATIO, __HEIGHT_RATIO = 4.2, 2.30
    __REDUCING_RATIO = 30

    def __init__(self, display):
        self.__display = display
        self.__width = self.__initial_width
        self.__height = self.__initial_height

    @property
    def get_size(self):
        return self.__width, self.__height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    def set_size(self, width, height):
        self.__width, self.__height = width, height

    def update_size(self):
        self.__width, self.__height = self.__initial_width, self.__initial_height

    @property
    def initial_size(self):
        return self.__initial_width, self.__initial_height

    @property
    def __initial_width(self):
        return self.__display.width // self.__WIDTH_RATIO

    @property
    def __initial_height(self):
        return self.__display.height // self.__HEIGHT_RATIO

    @property
    def reducing_size(self):
        return self.__display.height // self.__REDUCING_RATIO
