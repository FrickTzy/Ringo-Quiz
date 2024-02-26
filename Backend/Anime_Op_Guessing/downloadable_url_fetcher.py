from pytube import YouTube


def get_mp3_url(youtube_url):
    try:
        # Create a YouTube object
        yt = YouTube(youtube_url)

        # Get the audio streams
        audio_streams = yt.streams.filter(only_audio=True)

        # Get the highest quality audio stream
        highest_quality_audio = audio_streams.get_audio_only()

        # Get the URL of the audio stream
        mp3_url = highest_quality_audio.url

        return mp3_url

    except Exception as e:
        print("Error:", e)
        return None

# Example usage
youtube_url = input("Enter the YouTube URL: ")
mp3_url = get_mp3_url(youtube_url)

if mp3_url:
    print("MP3 URL:", mp3_url)
else:
    print("Failed to retrieve MP3 URL.")