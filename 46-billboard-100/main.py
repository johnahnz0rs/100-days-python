import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth


load_dotenv()
ID = os.getenv("ID")
SECRET = os.getenv("SECRET")
SCOPE = "playlist-modify-private, playlist-read-private"



# # get list of songs based on user-input:date
travel_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:  ")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{travel_date}/")
response.raise_for_status()
page_html = BeautifulSoup(response.text, "html.parser")
track_tags = page_html.select("li.o-chart-results-list__item h3#title-of-a-story")
top_100_songs = [track.getText().replace("\n", "").replace("\t", "") for track in track_tags]
# print(f"top_100_songs ready: {top_100_songs[0]}")



# authenticate spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE, client_id=ID, client_secret=SECRET, redirect_uri="http://example.com"))
current_user = sp.me()
user_id = current_user["id"]
# print(f"user_id: {user_id}")



# search spotify for tracks/songs
track_uris = []
for t in top_100_songs:
    try:
        info = sp.search(t, type="track", limit=1)
    except:
        pass
    else:
        try:
            uri = info["tracks"]["items"][0]["uri"]
        except:
            pass
        else:
            track_uris.append(uri)
# print(track_uris)


# create a new playlist in spotify
new_playlist = sp.user_playlist_create(user=user_id, name=f"{travel_date} Billboard 100", public=False, description="The Billboard Hot 100 tracks on this date")
new_playlist_id = new_playlist["id"]

# add songs to spotify playlist
sp.playlist_add_items(playlist_id=new_playlist_id, items=track_uris)
