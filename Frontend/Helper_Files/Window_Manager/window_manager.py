from pygame import QUIT


class WindowManager:
    __running = True

    @property
    def is_running(self):
        return self.__running

    def __quit(self):
        self.__running = False

    def check_if_quit(self, event):
        if event.type == QUIT:
            self.__quit()

