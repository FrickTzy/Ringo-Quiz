from requests import post
from random import shuffle, choice
from .fetching_error import AnimeFetchingError


class AnimeCharacterFetcher:
    __MAX_CHARACTER_RETRIEVED = 4
    __ERROR_MESSAGE = "Error fetching data."
    __MAX_CHARACTER_RANGE = 15
    __character_chosen = []

    def get_list_of_random_characters(self, anime_title):
        list_of_anime_characters = self.__get_list_of_characters(anime_title=anime_title)
        return [self.__get_character_name(character=character) for character in
                list_of_anime_characters[0:self.__MAX_CHARACTER_RETRIEVED]]

    def __get_list_of_characters(self, anime_title, shuffle_list=True):
        anime_characters_json: dict = self.__retrieve_anime_characters_json(anime_title=anime_title)
        if (list_of_anime_characters := self.__extract_anime_characters(anime_characters_json)) == self.__ERROR_MESSAGE:
            return False
        if shuffle_list:
            shuffle(list_of_anime_characters)
        return list_of_anime_characters

    def get_random_character(self, anime_title):
        anime_characters_json: dict = self.__retrieve_anime_characters_json(anime_title=anime_title)
        if (list_of_anime_characters := self.__extract_anime_characters(anime_characters_json)) == self.__ERROR_MESSAGE:
            return self.__ERROR_MESSAGE
        chosen_character = choice(list_of_anime_characters)
        return self.__get_character_name(character=chosen_character)

    def get_random_character_for_quiz(self, anime_title) -> (str, list[str]):
        original_character_list = self.__get_list_of_characters(anime_title=anime_title, shuffle_list=False)
        if not original_character_list:
            raise AnimeFetchingError()
        chosen_character_list = []
        for character in original_character_list[:self.__MAX_CHARACTER_RANGE]:
            character_name = self.__get_character_name(character=character)
            if len(chosen_character_list) == self.__MAX_CHARACTER_RETRIEVED:
                break
            if character_name in self.__character_chosen:
                continue
            chosen_character_list.append(character_name)
        return self.__choose_random_character(chosen_character_list), chosen_character_list

    def __choose_random_character(self, character_list):
        chosen_character = choice(character_list)
        self.__character_chosen.append(chosen_character)
        return chosen_character

    @staticmethod
    def __get_character_name(character: dict):
        return character["name"]["full"]

    def __extract_anime_characters(self,  anime_characters_json):
        if anime_characters_json == self.__ERROR_MESSAGE:
            return self.__ERROR_MESSAGE
        try:
            list_of_anime_characters = anime_characters_json['data']['Page']['media'][0]['characters']['nodes']
            if not list_of_anime_characters:
                return self.__ERROR_MESSAGE
            return list_of_anime_characters
        except TypeError:
            return self.__ERROR_MESSAGE
        except IndexError:
            return self.__ERROR_MESSAGE

    def __retrieve_anime_characters_json(self, anime_title):
        try:
            # Search for anime by name
            query = '''
                 query ($search: String) {
                   Page {
                     media(search: $search, type: ANIME) {
                       characters {
                         nodes {
                           name {
                             full
                           }
                         }
                       }
                     }
                   }
                 }
                 '''
            variables = {'search': anime_title}
            response = post('https://graphql.anilist.co', json={'query': query, 'variables': variables})
            return response.json()

        except Exception:
            return self.__ERROR_MESSAGE


if __name__ == "__main__":
    anime_name = input("Enter the name of an anime: ")
    random_character = AnimeCharacterFetcher().get_random_character(anime_title=anime_name)
    print("Random character:", random_character)
