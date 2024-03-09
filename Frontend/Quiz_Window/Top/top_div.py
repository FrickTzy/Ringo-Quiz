from pygame import Surface, SRCALPHA, image as pyimage
from Backend import AnimeCharacterImageFetcher
from .Character_Image import CharacterImage


class TopDiv:
    def __init__(self, display, answer_manager, init_manager, animation_notifier):
        self.__display = display
        self.__top_surface = Surface(display.get_window_size, SRCALPHA)
        self.__answer_manager = answer_manager
        self.__image_manager = CharacterImage(display=display)
        self.__image_fetcher = AnimeCharacterImageFetcher()
        self.__init_manager = init_manager
        self.__animation_notifier = animation_notifier

    def show(self):
        self.__clear_surface()
        self.__image_manager.show(surface=self.__top_surface,
                                  finished_clicking=self.__animation_notifier.animation_running,
                                  correct_index=self.__answer_manager.get_correct_answer_index)
        self.__display.window.blit(self.__top_surface, (0, 0))

    def __clear_surface(self):
        self.__top_surface.fill((0, 0, 0, 0))

    def set_image(self, anime_title: str, character_name: str):
        image = self.__image_fetcher.retrieve_image(anime_title=anime_title, character_name=character_name)
        self.__image_manager.set_image(image=pyimage.load(image))

    def update(self):
        self.__top_surface = Surface(self.__display.get_window_size, SRCALPHA)
        self.__image_manager.update()

