from .random_anime_fetcher import RandomAnimeFetcher
from .anime_character_fetcher import AnimeCharacterFetcher
from random import choice


class AnswerManager:
    __current_choices = {}
    __chosen_character_name = ""
    __anime_title = ""

    def __init__(self):
        self.__anime_fetcher = RandomAnimeFetcher()
        self.__character_name_fetcher = AnimeCharacterFetcher()

    def initialize(self):
        self.__current_choices.clear()
        anime_title = self.__anime_fetcher.get_random_anime_title()
        if not anime_title:
            return
        self.__anime_title = anime_title
        character_list = self.__character_name_fetcher.get_list_of_random_characters(anime_title=anime_title)
        chosen_character_name = self.__choose_random_character(character_list=character_list)
        self.__chosen_character_name = chosen_character_name
        self.__set_choices(character_list=character_list, chosen_character_name=chosen_character_name)

    def __set_choices(self, character_list, chosen_character_name):
        for index, character_name in enumerate(character_list):
            correct_answer = False
            if character_name == chosen_character_name:
                correct_answer = True
            self.__current_choices[index] = {"choice": character_name, "correct_answer": correct_answer}

    def check_if_correct_answer(self, index):
        if self.__current_choices[index]["correct_answer"]:
            return True
        return False

    @staticmethod
    def __choose_random_character(character_list):
        return choice(character_list)

    @property
    def choices(self):
        return self.__current_choices

    @property
    def anime_title(self):
        return self.__anime_title

    @property
    def chosen_character_name(self):
        return self.__chosen_character_name
