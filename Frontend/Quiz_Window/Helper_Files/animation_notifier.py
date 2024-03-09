

class AnimationNotifier:
    __animation_running = False

    def start_animation(self):
        self.__animation_running = True

    def reset_animation(self):
        self.__animation_running = False

    @property
    def animation_running(self):
        return self.__animation_running
