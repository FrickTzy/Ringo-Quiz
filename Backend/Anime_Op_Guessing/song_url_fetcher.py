from youtubesearchpython import VideosSearch


def get_youtube_url(song_name):
    try:
        # Search for the song on YouTube
        videos_search = VideosSearch(song_name, limit=1)
        result = videos_search.result()

        # Extract the URL of the first video
        if 'result' in result and 'link' in result['result'][0]:
            youtube_url = result['result'][0]['link']
            return youtube_url
        else:
            print("No video found for the given song name.")
            return None
    except Exception as e:
        print("Error:", str(e))
        return None


# Example usage:
song_name = input("Enter the name of the song: ")
youtube_url = get_youtube_url(song_name)

if youtube_url:
    template = "naruto op 1"
    print("YouTube URL for the song:", youtube_url)