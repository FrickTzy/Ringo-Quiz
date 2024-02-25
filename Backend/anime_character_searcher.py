from requests import post
from random import shuffle, choice


class AnimeCharacterSearcher:
    __MAX_CHARACTER_RETRIEVED = 4
    __ERROR_MESSAGE = "Error fetching data."

    def get_list_of_random_characters(self, anime_title):
        anime_characters_json: dict = self.__retrieve_anime_characters_json(anime_title=anime_title)
        if (list_of_anime_characters := self.__extract_anime_characters(anime_characters_json)) == self.__ERROR_MESSAGE:
            return self.__ERROR_MESSAGE
        shuffle(list_of_anime_characters)
        return [self.__get_character_name(character=character) for character in
                list_of_anime_characters[0:self.__MAX_CHARACTER_RETRIEVED]]

    def get_random_character(self, anime_title):
        anime_characters_json: dict = self.__retrieve_anime_characters_json(anime_title=anime_title)
        if (list_of_anime_characters := self.__extract_anime_characters(anime_characters_json)) == self.__ERROR_MESSAGE:
            return self.__ERROR_MESSAGE
        chosen_character = choice(list_of_anime_characters)
        return self.__get_character_name(character=chosen_character)

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
    random_character = AnimeCharacterSearcher().get_random_character(anime_title=anime_name)
    print("Random character:", random_character)
