import requests
from bs4 import BeautifulSoup
from datetime import datetime
from dateutil import parser
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import dotenv_values
config = dotenv_values(".env") 

SPOTIPY_CLIENT_ID = config["SPOTIPY_CLIENT_ID"]
SPOTIPY_CLIENT_SECRET = config["SPOTIPY_CLIENT_SECRET"]
SPOTIPY_REDIRECT_URI = config["SPOTIPY_REDIRECT_URI"]
SPOTIFY_DISPLAY_NAME = config["SPOTIFY_DISPLAY_NAME"]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,  # e.g. "https://example.com"
        scope="playlist-modify-private",
        username=SPOTIFY_DISPLAY_NAME,
    )
)

user_id = sp.current_user()["id"]
try:
    date = input("Type in year in yyyy-mm-dd format: ")
    date = datetime.strptime(date, "%Y-%m-%d").date()
except ValueError:
    print("Error: Invalid date format. Please enter a date in the format yyyy-mm-dd.")
    exit()

url = f"https://www.billboard.com/charts/hot-100/{date}"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
songs = soup.select("li ul li h3")
songs = [song.text.strip() for song in songs]
artist = [artist.text.strip() for artist in soup.select("li ul li span") if len(artist.text.strip()) >= 3]

song_uris = []

for i in range(len(songs)):
    song_name = songs[i]
    query = f"track:{song_name} year:{date.year}"
    
    try:
        results = sp.search(q=query, type='track', limit=1)
        song_uri = results['tracks']['items'][0]['uri']
        song_uris.append(song_uri)
    except (IndexError, KeyError) as e:
        print(f"Could not find URI for {song_name} with year filter: {e}")
        # Retry with just the song name
        try:
            query = f"track:{song_name}"
            results = sp.search(q=query, type='track', limit=1)
            song_uri = results['tracks']['items'][0]['uri']
            song_uris.append(song_uri)
        except (IndexError, KeyError) as e:
            print(f"Could not find URI for {song_name} without year filter: {e}")
        except Exception as e:
            print(f"An unexpected error occurred for {song_name} on second try: {e}")
    except Exception as e:
        print(f"An unexpected error occurred for {song_name} on first try: {e}")


playlist = sp.user_playlist_create(
    user=user_id,
    name=f"100 Billboard at {str(date)}",
    public=False,
    collaborative=False,
    description=f'This is 100 Billboard at {str(date)}'
)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)