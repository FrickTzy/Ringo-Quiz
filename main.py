import pygame
from Backend.Functions import Music
from Frontend.Helper_Files import WindowManager, Display
from Frontend.Quiz_Window import QuizWindow
from Frontend.Settings import Colors, FPS


class Main:
    __CLOCK = pygame.time.Clock()
    __FILL_COLOR = Colors.QUIZ_DARK_PURPLE

    def __init__(self):
        self.__init_pygame()
        self.__window_manager = WindowManager()
        self.__music = Music()
        self.__display = Display()
        self.__quiz_window = QuizWindow(display=self.__display, window_manager=self.__window_manager,
                                        music=self.__music)

    @staticmethod
    def __init_pygame():
        pygame.init()

    def run(self):
        while self.__window_manager.is_running:
            self.__update_frame()
            self.__quiz_window.run()
        pygame.quit()

    def __update_frame(self):
        self.__CLOCK.tick(FPS)
        pygame.display.update()
        self.__display.window.fill(self.__FILL_COLOR)


if __name__ == "__main__":
    Main().run()

