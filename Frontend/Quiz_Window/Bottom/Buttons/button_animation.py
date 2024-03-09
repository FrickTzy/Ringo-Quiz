from Frontend.Helper_Files import SmoothAnimation, TargetManager, EaseOutBackSmoothing
from Frontend.Settings import Colors


class ButtonAnimation:
    __SPEED_PER_FRAME = 0.03
    __in_animation = False

    def __init__(self, button_pos, color_manager, correct_answer_manager):
        self.__button_pos = button_pos
        self.__correct_answer_manager = correct_answer_manager
        self.__color_animation_manager = ButtonColorAnimation(color_manager=color_manager)
        self.__target_manager = TargetManager()
        self.__animation_manager = SmoothAnimation(target_manager=self.__target_manager,
                                                   speed_per_frame=self.__SPEED_PER_FRAME,
                                                   smoothing_method=EaseOutBackSmoothing())
        self.__animation_start_manager = AnimationStartManager()

    def check_for_animations(self, in_animation):
        if self.__correct_animation_condition(in_animation=in_animation):
            self.__color_animation_manager.animate_button_color()
            self.__animate_button()

    def __correct_animation_condition(self, in_animation):
        if self.__animation_manager.finished_animation:
            self.__animation_start_manager.start_animation = False
        if not self.__in_animation == in_animation:
            is_correct_answer = self.__correct_answer_manager.is_correct_answer
            self.__in_animation = in_animation
            self.__setup_animation(in_animation=in_animation, is_correct_answer=is_correct_answer)
            self.__color_animation_manager.setup_animation(in_animation=in_animation,
                                                           is_correct_answer=is_correct_answer)
        if self.__animation_start_manager.start_animation:
            return True
        return False

    @property
    def finished_animation(self):
        return self.__animation_start_manager.finished_animation

    def __setup_animation(self, in_animation, is_correct_answer):
        target_y = self.__button_pos.correct_target_y if is_correct_answer else self.__button_pos.wrong_target_y
        self.__animation_manager.reset()
        if in_animation:
            self.__target_manager.setup(current_value=self.__button_pos.button_y,
                                        target_value=target_y)
        else:
            self.__target_manager.setup(current_value=self.__button_pos.button_y,
                                        target_value=self.__button_pos.initial_button_y)
        self.__animation_start_manager.start_animation = True

    def __animate_button(self):
        current_button_y = self.__animation_manager.get_current_value()
        current_button_height = self.__button_pos.initial_button_height + \
            self.__button_pos.initial_button_y - current_button_y
        self.__button_pos.set_button_y(button_y=current_button_y)
        self.__button_pos.set_button_height(button_height=current_button_height)


class ButtonColorAnimation:
    __CORRECT_COLOR = Colors.QUIZ_CORRECT_GREEN
    __WRONG_COLOR = Colors.QUIZ_WRONG_RED

    def __init__(self, color_manager):
        self.__color_manager_list = []
        self.__color_manager = color_manager
        self.__init_color_animation_manager_list()

    def __init_color_animation_manager_list(self):
        for color_value in self.__color_manager.current_color:
            self.__color_manager_list.append(RGBAnimationTemplate(initial_color_value=color_value))

    def setup_animation(self, in_animation, is_correct_answer):
        target_color = self.__CORRECT_COLOR if is_correct_answer else self.__WRONG_COLOR
        for index, color_manager in enumerate(self.__color_manager_list):
            target_color_value = target_color[index]
            color_manager.setup_animation(in_animation=in_animation, target_color_value=target_color_value)

    def animate_button_color(self):
        current_rgb = tuple(int(color_manager.get_current_color_value) for color_manager in self.__color_manager_list)
        self.__color_manager.set_color(current_color_rgb=current_rgb)


class RGBAnimationTemplate:
    __SPEED_PER_FRAME = 0.03
    __target_color_value = None

    def __init__(self, initial_color_value):
        self.__initial_color_value = initial_color_value
        self.__target_manager = TargetManager()
        self.__animation_manager = SmoothAnimation(target_manager=self.__target_manager,
                                                   speed_per_frame=self.__SPEED_PER_FRAME)

    def __set_target_color_value(self, target_color_value):
        self.__target_color_value = target_color_value

    def setup_animation(self, in_animation, target_color_value):
        self.__animation_manager.reset()
        self.__set_target_color_value(target_color_value=target_color_value)
        if in_animation:
            self.__target_manager.setup(current_value=self.__initial_color_value,
                                        target_value=self.__target_color_value)
        else:
            self.__target_manager.setup(current_value=self.__target_color_value,
                                        target_value=self.__initial_color_value)

    @property
    def get_current_color_value(self):
        return self.__animation_manager.get_current_value()


class AnimationStartManager:
    start_animation = False

    @property
    def finished_animation(self):
        return not self.start_animation
