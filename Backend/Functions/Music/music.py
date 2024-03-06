import random
from Backend.Timer import TargetTimer
from pygame import mixer
from glob import glob
import os


class SongChecker:
    __SONG_FOLDER_PATH = "\\Backend\\Background Music"

    @classmethod
    def get_all_songs(cls):
        return glob("*.mp3", root_dir=cls.__get_path())

    @classmethod
    def __get_path(cls) -> str:
        return f"{os.getcwd()}{cls.__SONG_FOLDER_PATH}"


class Music:
    __SONG_FOLDER_PATH = "Backend/Background Music"
    __SONG_VOLUME = 0.8
    __current_song_index: int = 0
    __current_song = None

    def __init__(self):
        self.__target_timer = TargetTimer()
        self.__music_list = SongChecker.get_all_songs()
        self.__shuffle_music_list()
        self.__set_current_song()
        self.__play_current_song()

    def __set_current_song(self):
        self.__current_song = mixer.Sound(os.path.join(self.__SONG_FOLDER_PATH,
                                                       self.__music_list[self.__current_song_index]))
        self.__target_timer.update_target_second_time(target_time=self.__current_song.get_length())

    def __play_current_song(self):
        mixer.Channel(2).set_volume(self.__SONG_VOLUME)
        mixer.Channel(2).stop()
        mixer.Channel(2).play(self.__current_song)

    @property
    def __song_path(self):
        return os.path.join(self.__SONG_FOLDER_PATH, self.__music_list[self.__current_song_index])

    def __shuffle_music_list(self):
        random.shuffle(self.__music_list)

    def check_if_song_finished(self):
        if not self.__target_timer.check_if_finish_timer():
            return
        self.__current_song_index += 1
        self.__set_current_song()
        self.__play_current_song()
