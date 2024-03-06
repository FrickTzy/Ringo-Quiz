from Frontend.Helper_Files import SmoothAnimation, TargetManager


class ButtonAnimation:
    __SPEED_PER_FRAME = 0.1
    __in_animation = False

    def __init__(self, button_pos):
        self.__button_pos = button_pos
        self.__target_manager = TargetManager()
        self.__animation_manager = SmoothAnimation(target_manager=self.__target_manager,
                                                   speed_per_frame=self.__SPEED_PER_FRAME)
        self.__animation_start_manager = AnimationStartManager()

    def check_for_animations(self, in_animation):
        if self.__correct_animation_condition(in_animation=in_animation):
            self.__animate_map_bar()

    def __correct_animation_condition(self, in_animation):
        if self.__animation_manager.finished_animation:
            self.__animation_start_manager.start_animation = False
        if not self.__in_animation == in_animation:
            self.__in_animation = in_animation
            self.__setup_animation(in_animation=in_animation)
        if self.__animation_start_manager.start_animation:
            return True
        return False

    def __setup_animation(self, in_animation):
        self.__animation_manager.reset()
        if in_animation:
            self.__target_manager.setup(current_value=self.__button_pos.button_y,
                                        target_value=self.__button_pos.target_y)
        else:
            self.__target_manager.setup(current_value=self.__button_pos.button_y,
                                        target_value=self.__button_pos.initial_button_y)
        self.__animation_start_manager.start_animation = True

    def __animate_map_bar(self):
        current_button_y = self.__animation_manager.get_current_value()
        current_button_height = self.__button_pos.initial_button_height + \
            self.__button_pos.initial_button_y - current_button_y
        self.__button_pos.set_button_y(button_y=current_button_y)
        self.__button_pos.set_button_height(button_height=current_button_height)


class AnimationStartManager:
    start_animation = False
