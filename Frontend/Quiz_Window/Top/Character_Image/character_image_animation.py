from Frontend.Helper_Files import SmoothAnimation, TargetManager, EaseOutBackSmoothing


class CharacterImageAnimation:
    __SPEED_PER_FRAME = 0.03
    __in_animation = False
    __correct_index = 0

    def __init__(self, image_pos, image_size):
        self.__image_pos = image_pos
        self.__image_size = image_size
        self.__target_manager = TargetManager()
        self.__animation_manager = SmoothAnimation(target_manager=self.__target_manager,
                                                   speed_per_frame=self.__SPEED_PER_FRAME,
                                                   smoothing_method=EaseOutBackSmoothing())
        self.__animation_start_manager = AnimationStartManager()

    def check_for_animations(self, in_animation, correct_index):
        if self.__correct_animation_condition(in_animation=in_animation, correct_index=correct_index):
            self.__animate_image()

    def __correct_animation_condition(self, in_animation, correct_index):
        if self.__animation_manager.finished_animation:
            self.__animation_start_manager.animation_running = False
        if not self.__in_animation == in_animation:
            self.__in_animation = in_animation
            self.__setup_animation(in_animation=in_animation, correct_index=correct_index)
        if self.__animation_start_manager.animation_running:
            return True
        return False

    @property
    def finished_animation(self):
        return self.__animation_start_manager.finished_animation

    def __setup_animation(self, in_animation, correct_index):
        self.__animation_manager.reset()
        if in_animation:
            self.__in_animation_setup(correct_index=correct_index)
        else:
            self.__out_animation_setup()
        self.__animation_start_manager.animation_running = True

    def __in_animation_setup(self, correct_index):
        self.__correct_index = correct_index
        big_size_range = (0 < correct_index < 3)
        self.__target_manager.setup(current_value=0, target_value=self.__get_target_size(in_range=big_size_range))

    def __out_animation_setup(self):
        big_size_range = (0 < self.__correct_index < 3)
        self.__target_manager.setup(current_value=self.__get_target_size(in_range=big_size_range), target_value=0)

    def __get_target_size(self, in_range):
        return self.__image_size.reducing_size if in_range else -self.__image_size.reducing_size // 1.3

    def __animate_image(self):
        current_size_minus = self.__animation_manager.get_current_value()
        initial_width, initial_height = self.__image_size.initial_size
        current_width = initial_width - current_size_minus
        current_height = initial_height - current_size_minus
        self.__image_size.set_size(width=current_width, height=current_height)


class AnimationStartManager:
    animation_running = False

    @property
    def finished_animation(self):
        return not self.animation_running
