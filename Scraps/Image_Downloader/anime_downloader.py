import requests
import shutil
import os
import cv2


def fetch_random_anime_image():
    try:
        # Fetch random anime image URL from Waifu.pics API
        response = requests.get("https://api.waifu.pics/sfw/neko")
        data = response.json()
        image_url = data['url']

        # Download the image
        response = requests.get(image_url, stream=True)
        if response.status_code == 200:
            # Save the image to a file
            with open("random_anime_image.jpg", 'wb') as f:
                response.raw.decode_content = True
                shutil.copyfileobj(response.raw, f)
            print("Random anime character image saved as 'random_anime_image.jpg'")

            # Fetch anime character name using Trace.moe API
            character_name = get_character_name("random_anime_image.jpg")
            if character_name:
                print("Name of the anime character:", character_name)
            else:
                print("Failed to fetch character name.")
        else:
            print("Failed to download image:", response.status_code)
    except Exception as e:
        print("Error:", e)


def get_character_name(image_path):
    try:
        # Upload image to Trace.moe API
        files = {'image': open(image_path, 'rb')}
        response = requests.post('https://api.trace.moe/search', files=files)
        if response.status_code == 200:
            data = response.json()
            if data['docs']:
                anime_title = data['docs'][0]['anime']
                character_name = data['docs'][0]['character']
                return f"{character_name} from {anime_title}"
            else:
                return None
        else:
            return None
    except Exception as e:
        print("Error fetching character name:", e)
        return None


if __name__ == "__main__":
    fetch_random_anime_image()