from pygame import transform


class CharacterImage:
    __original_image = None
    __used_image = None

    def __init__(self, display):
        self.__image_pos = CharacterImagePos(display=display)
        self.__size_manager = CharacterImageSizeManager(display=display)

    def show(self, surface):
        if self.__used_image is None:
            raise Exception("You haven't loaded the image yet!")
        surface.blit(self.__used_image, self.__image_pos.get_coord(image_width=self.__size_manager.width))

    def set_image(self, image):
        self.__original_image = image

    def update(self):
        self.__used_image = transform.scale(self.__original_image, self.__size_manager.get_size)


class CharacterImagePos:
    __X_RATIO, __Y_RATIO = 2, 43

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
    __WIDTH_RATIO, __HEIGHT_RATIO = 2.8, 2.35

    def __init__(self, display):
        self.__display = display

    @property
    def get_size(self):
        return self.width, self.height

    @property
    def width(self):
        return self.__display.width // self.__WIDTH_RATIO

    @property
    def height(self):
        return self.__display.height // self.__HEIGHT_RATIO