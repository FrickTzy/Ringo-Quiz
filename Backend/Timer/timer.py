from pygame import time


class TargetTimer:
    def __init__(self):
        self.__target_time: int | float = 0

    def update_target_second_time(self, target_time) -> None:
        self.__target_time += int(target_time)

    def update_target_ms_time(self, target_time) -> None:
        self.__target_time += target_time

    def set_target_second_time(self, target_time) -> None:
        self.__target_time = int(target_time)

    def set_target_ms_time(self, target_time) -> None:
        self.__target_time = target_time

    @staticmethod
    def ms_to_second(ms):
        return ms // 1000

    @property
    def current_second_time(self):
        return self.ms_to_second(time.get_ticks())

    def check_if_finish_timer(self):
        if self.current_second_time >= self.__target_time:
            return True
        return False

    @property
    def get_current_ms(self):
        return time.get_ticks()

    def check_if_finish_ms_timer(self):
        if self.get_current_ms >= self.__target_time:
            return True
        return False

    def debug(self):
        print(f"current time: {self.current_second_time} | target time: {self.__target_time}")


class PauseTimer:
    __started_pause = False

    def __init__(self):
        self.__ms_pause_start: int = 0
        self.__ms_pause_ended: int = 0
        self.__total_ms_spent_paused = 0

    def restart(self):
        self.__ms_pause_start = 0
        self.__ms_pause_ended = 0
        self.__total_ms_spent_paused = 0
        self.__started_pause = False

    @property
    def ms_spent_paused(self):
        if self.__started_pause:
            return self.__total_ms_spent_paused + (time.get_ticks() - self.__ms_pause_start)
        return self.__total_ms_spent_paused

    def start_pause(self):
        self.__ms_pause_start = time.get_ticks()
        self.__started_pause = True

    def end_pause(self):
        self.__ms_pause_ended = time.get_ticks()
        self.__total_ms_spent_paused += self.__ms_pause_ended - self.__ms_pause_start
        self.__started_pause = False


class DelayTimer:
    def __init__(self):
        self.__start_time: int | float = 0
        self.__started_timer = False
        self.__timer_finished: bool = False

    def check_delay_seconds(self, delay_seconds=0):
        if not self.__started_timer:
            self.__start_time = self.current_seconds
            self.__started_timer = True
        if self.__start_time + delay_seconds <= self.current_seconds:
            self.__timer_finished = True

    def check_delay_ms(self, delay_ms=0):
        if not self.__started_timer:
            self.__start_time = self.current_ms
            self.__started_timer = True
        if self.__start_time + delay_ms <= self.current_ms:
            self.__timer_finished = True

    def reset_timer(self):
        self.__started_timer = False
        self.__timer_finished = False

    @property
    def timer_finished(self):
        return self.__timer_finished

    @property
    def current_seconds(self):
        return self.ms_to_second(time.get_ticks())

    @property
    def current_ms(self):
        return time.get_ticks()

    @staticmethod
    def ms_to_second(ms):
        return ms // 1000


class IntervalTimer:
    def __init__(self, interval: int = 100):
        self.last_time: int = time.get_ticks()
        self.interval = interval

    def time_interval_finished(self) -> bool:
        current_time = time.get_ticks()
        if current_time - self.last_time >= self.interval:
            self.last_time = current_time
            return True
        return False

    def debug(self):
        print("Debugging: ")
        print(f"current time: {time.get_ticks()}")
        print(f"last time: {self.last_time}")
        print(f"interval: {self.interval}\n")

    def change_interval(self, interval):
        self.interval = interval


class ActivationTimer:
    def __init__(self, interval: int = 100):
        self.__last_time_taken: int = time.get_ticks()
        self.__interval = interval

    def activation_stopped(self, activated: bool) -> bool:
        """
        This function takes a bool and if that bool stays false for a certain time, it will return True.
        :param activated:
        :return:
        """
        current_time = time.get_ticks()
        if activated:
            self.__last_time_taken = current_time
        if current_time >= self.__last_time_taken + self.__interval:
            self.__last_time_taken = current_time
            return True
        return False

    def activation_started(self, activated: bool) -> bool:
        """
        This function takes a bool and if that bool stays true for a certain time, it will return True.
        :param activated:
        :return:
        """
        current_time = time.get_ticks()
        if not activated:
            self.__last_time_taken = current_time
        if current_time >= self.__last_time_taken + self.__interval:
            self.__last_time_taken = current_time
            return True
        return False

    def debug(self):
        print("Debugging: ")
        print(f"current time: {time.get_ticks()}")
        print(f"last time: {self.__last_time_taken}")
        print(f"interval: {self.__interval}\n")

    def change_interval(self, interval):
        self.__interval = interval
