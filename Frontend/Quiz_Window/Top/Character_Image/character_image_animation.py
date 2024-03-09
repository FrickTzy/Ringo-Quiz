from Frontend.Helper_Files import SmoothAnimation, TargetManager, EaseOutBackSmoothing


class CharacterImageAnimation:
    __SPEED_PER_FRAME = 0.03
    __in_animation = False

    def __init__(self, image_pos, image_size):
        self.__image_pos = image_pos
        self.__image_size = image_size
        self.__target_manager = TargetManager()
        self.__animation_manager = SmoothAnimation(target_manager=self.__target_manager,
                                                   speed_per_frame=self.__SPEED_PER_FRAME,
                                                   smoothing_method=EaseOutBackSmoothing())
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

    @property
    def finished_animation(self):
        return self.__animation_start_manager.finished_animation

    def __setup_animation(self, in_animation):
        self.__animation_manager.reset()
        if in_animation:
            self.__target_manager.setup(current_value=0,
                                        target_value=self.__image_size.reducing_size)
        else:
            self.__target_manager.setup(current_value=self.__image_size.reducing_size,
                                        target_value=0)
        self.__animation_start_manager.start_animation = True

    def __animate_map_bar(self):
        current_size_minus = self.__animation_manager.get_current_value()
        initial_width, initial_height = self.__image_size.initial_size
        current_width = initial_width - current_size_minus
        current_height = initial_height - current_size_minus
        self.__image_size.set_size(width=current_width, height=current_height)


class AnimationStartManager:
    start_animation = False

    @property
    def finished_animation(self):
        return not self.start_animation
