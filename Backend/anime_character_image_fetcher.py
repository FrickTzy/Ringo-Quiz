import requests
from io import BytesIO


class AnimeCharacterImageFetcher:
    def retrieve_image(self, anime_title, character_name):
        if (json_data := self.__retrieve_json(anime_title=anime_title)) is None:
            return None
        characters = json_data['data']['Media']['characters']['edges']
        if not characters:
            return None
        filtered_character: dict = self.__filter_characters(character_name=character_name, characters=characters)
        if filtered_character:
            image_url = filtered_character['image']['large']
            return BytesIO(requests.get(image_url, stream=True).content)
        return None

    @staticmethod
    def __filter_characters(character_name, characters):
        matching_characters = [c['node'] for c in characters if c['node']['name']['full'] == character_name]
        if not matching_characters:
            return {}
        return matching_characters[0]

    @staticmethod
    def __retrieve_json(anime_title):
        try:
            query_anime = '''
                   query ($anime: String) {
                     Media(search: $anime, type: ANIME) {
                       characters {
                         edges {
                           node {
                             name {
                               full
                             }
                             image {
                               large
                             }
                           }
                         }
                       }
                     }
                   }
                   '''
            variables_anime = {'anime': anime_title}
            response_anime = requests.post('https://graphql.anilist.co',
                                           json={'query': query_anime, 'variables': variables_anime})
            return response_anime.json()

        except Exception as e:
            return None
