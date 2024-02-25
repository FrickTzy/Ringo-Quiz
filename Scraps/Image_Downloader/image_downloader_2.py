import os
import requests
import random
import shutil
from Backend.anime_character_searcher import AnimeCharacterSearcher


def download_character_image(anime_name, character_name):
    try:
        # Create directory for the anime if it doesn't exist
        anime_directory = anime_name.replace(" ", "_")
        if not os.path.exists(anime_directory):
            os.makedirs(anime_directory)

        # Search for anime by name
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
        variables_anime = {'anime': anime_name}
        response_anime = requests.post('https://graphql.anilist.co', json={'query': query_anime, 'variables': variables_anime})
        data_anime = response_anime.json()

        if 'errors' in data_anime:
            return None

        characters = data_anime['data']['Media']['characters']['edges']
        if not characters:
            return None

        # Find the character with the exact name match
        matching_characters = [c['node'] for c in characters if c['node']['name']['full'] == character_name]
        if not matching_characters:
            return None

        character = random.choice(matching_characters)
        image_url = character['image']['large']

        # Download the image
        response_image = requests.get(image_url, stream=True)
        if response_image.status_code == 200:
            # Save the image to a file
            image_filename = f"{character_name}.jpg"
            image_path = os.path.join(anime_directory, image_filename)
            with open(image_path, 'wb') as f:
                response_image.raw.decode_content = True
                shutil.copyfileobj(response_image.raw, f)
            return image_path
        else:
            return None

    except Exception as e:
        print("Error:", e)
        return None


if __name__ == "__main__":
    anime_name = input("Enter the name of an anime: ").title()
    character_name = AnimeCharacterSearcher().get_random_character(anime_title=anime_name)
    image_file = download_character_image(anime_name, character_name)
    if image_file:
        print(f"Image of {character_name} downloaded as {image_file}")
    else:
        print("Failed to download image.")