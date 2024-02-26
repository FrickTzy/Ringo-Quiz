from googlesearch import search
from bs4 import BeautifulSoup
import requests


def search_youtube(query):
    # Search for the query on Google and filter by YouTube results
    youtube_results = search(query + " site:youtube.com", tld="com", num=1, stop=1, pause=2)

    # Extract the URL of the first YouTube result
    for url in youtube_results:
        if "youtube.com" in url:
            return url

    return None

def get_anime_opening_title(anime_title):
    # Search for the anime opening on YouTube
    query = f"{anime_title} opening 1 title"
    youtube_url = search_youtube(query)

    if youtube_url:
        response = requests.get(youtube_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        video_title = soup.find("title").text
        return video_title.replace(" - YouTube", "")
    else:
        return None

if __name__ == "__main__":
    anime_title = input("Enter the name of the anime: ")
    opening_title = get_anime_opening_title(anime_title)
    if opening_title:
        print(f"The opening title of {anime_title} is: {opening_title}")
    else:
        print("No opening title found.")