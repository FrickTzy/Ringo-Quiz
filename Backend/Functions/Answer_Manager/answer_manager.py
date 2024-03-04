from Backend.Functions.Anime_Fetcher.random_anime_fetcher import RandomAnimeFetcher
from Backend.Functions.Anime_Fetcher.anime_character_fetcher import AnimeCharacterFetcher


class AnswerManager:
    __current_choices = {}
    __chosen_character_name = ""
    __anime_title = ""

    def __init__(self):
        self.__anime_fetcher = RandomAnimeFetcher()
        self.__character_name_fetcher = AnimeCharacterFetcher()

    def initialize(self):
        self.__current_choices.clear()
        anime_title = self.__anime_fetcher.get_random_anime_from_list()
        if not anime_title:
            return
        self.__anime_title = anime_title
        retrieved_character_tuple = self.__character_name_fetcher.get_random_character_for_quiz(anime_title=anime_title)
        chosen_character_name, character_list = retrieved_character_tuple
        self.__chosen_character_name = chosen_character_name
        self.__set_choices(character_list=character_list, chosen_character_name=chosen_character_name)

    def reset(self):
        self.__current_choices.clear()
        self.__chosen_character_name = self.__anime_title = ""

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

    @property
    def choices(self):
        return self.__current_choices

    @property
    def anime_title(self):
        return self.__anime_title

    @property
    def chosen_character_name(self):
        return self.__chosen_character_name
