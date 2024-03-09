

class AnimationNotifier:
    __animation_running = False
    __finished_animation = False

    def start_animation(self):
        self.__animation_running = True
        self.__finished_animation = False

    def finish_animation(self):
        self.__finished_animation = True

    def reset_animation(self):
        self.__animation_running = False

    @property
    def animation_running(self):
        return self.__animation_running

    @property
    def check_if_finish_animation(self):
        return self.__finished_animation
