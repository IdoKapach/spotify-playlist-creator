import spotipy
from spotipy.oauth2 import SpotifyOAuth
from song_list_creator import SongListCreator
from url_list_creator import UrlListCreator
from os import environ

client_ID = environ["spotifyClientId"]
client_secret = environ["spotifyClientSecret"]
redirect_URI = "http://example.com/idopython10@gmail.com"

scope = "playlist-modify-private"

# connecting to the spotify account
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
                                                scope=scope,
                                                redirect_uri=redirect_URI,
                                                client_id=client_ID,
                                                client_secret=client_secret,
                                                show_dialog=True,
                                                cache_path="token.txt",
                                                username="ido"))
user_id = sp.current_user()["id"]
date = input("Enter the date in the format YYYY-MM-DD: ")

# creating the song list:
print("creating list...")
song_list_creator = SongListCreator(date)
song_list_creator.create_list()
url_list_creator = UrlListCreator(sp)
url_list_creator.create_list()

# creating the playlist from the url-list
print("creating playlist...")
response = sp.user_playlist_create(user=sp.current_user()["id"], name=f"best songs at {date}", public=False)
playlist_id = response["id"]
print(playlist_id)

with open("url-list.txt") as file:
    url_list = file.readlines()
    url_list = [url.strip() for url in url_list]

sp.playlist_add_items(playlist_id=playlist_id, items=url_list[:5])