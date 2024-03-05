import requests
import random


class RandomAnimeFetcher:
    __URL = "https://graphql.anilist.co"
    __MAX_PAGE_SCOPE = 3
    __ANIME_LIST = ["One Piece", "Bleach", "Unwanted Undead Adventurer",
                    "Eminence in Shadow", "Beastars", " Code Geass: Lelouch of the Rebellion", "Steins;Gate",
                    "Frieren", "Edens Zero", "Kimi ni Todoke",
                    "Hells Paradise", "The Ice Guy and His Cool Female Colleague", "Angel Next Door",
                    "Spy x Family", "Black Clover", "Tensura", "Chainsaw Man",
                    "Rising of the Shield Hero", "One Punch Man", "Death Note", "Assassination Classroom",
                    "Highschool of the Elite", "Violet Evergarden", "Hyouka", "Tsukimichi"]

    def __fetch_anime_data(self):
        page_number = random.randint(1, self.__MAX_PAGE_SCOPE)
        query, variables = self.__get_query_and_variables(page_number=page_number)
        try:
            response = requests.post(self.__URL, json={"query": query, "variables": variables})
            if response.status_code == 200:
                return response.json()["data"]["Page"]["media"]
            else:
                print("Failed to retrieve data. Status code:", response.status_code)
                return None
        except requests.exceptions.RequestException as e:
            print("Error:", e)
            return None

    @staticmethod
    def __get_query_and_variables(page_number):
        """
        Query is what determines the sorting, you can put a variable in it by adding $ to the name.
        And then adding it to the variable json.
        """
        return """
                query ($page: Int) {
                  Page(page: $page, perPage: 50) {
                    media(type: ANIME, sort: POPULARITY_DESC) {
                      title {
                        romaji
                      }
                    }
                  }
                }
                """, {"page": page_number}

    def get_random_anime_title(self):
        anime_data = self.__fetch_anime_data()
        if anime_data:
            anime_titles = [anime["title"]["romaji"] for anime in anime_data]
            return random.choice(anime_titles)
        else:
            return None

    def get_random_anime_from_list(self):
        return random.choice(self.__ANIME_LIST)


if __name__ == "__main__":
    anime_fetcher = RandomAnimeFetcher()
    random_anime_title = anime_fetcher.get_random_anime_title()
    if random_anime_title:
        print("Random Anime Title:", random_anime_title)