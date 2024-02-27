from pygame import Surface, SRCALPHA, image as pyimage
from Backend import AnimeCharacterImageFetcher
from .Character_Image import CharacterImage


class TopDiv:
    def __init__(self, display, answer_manager):
        self.__display = display
        self.__top_surface = Surface(display.get_window_size, SRCALPHA)
        self.__answer_manager = answer_manager
        self.__image_manager = CharacterImage(display=display)
        self.__image_fetcher = AnimeCharacterImageFetcher()

    def show(self):
        self.__image_manager.show(surface=self.__top_surface)
        self.__display.window.blit(self.__top_surface, (0, 0))

    def set_image(self, anime_title: str, character_name: str):
        image = self.__image_fetcher.retrieve_image(anime_title=anime_title, character_name=character_name)
        self.__image_manager.set_image(image=pyimage.load(image))

    def update(self):
        self.__top_surface = Surface(self.__display.get_window_size, SRCALPHA)
        self.__image_manager.update()

