import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import find_dotenv, load_dotenv


def authorization():
    load_dotenv(find_dotenv())
    auth_manager = SpotifyClientCredentials()
    return spotipy.Spotify(auth_manager=auth_manager)


def get_song_urls(song_arr):
    url_arr = []
    if song_arr is None:
        return "Error: No Genre Chosen"
    spotify = authorization()
    results = spotify.tracks(song_arr)
    tracks = results["tracks"]
    for track in tracks:
        url = track["preview_url"]
        if url is None:
            url = "No Preview Available At This Time"
        url_arr.append(url)
    return url_arr


def get_song_titles(song_arr):
    url_arr = []
    if song_arr is None:
        return "Error: No Genre Chosen"
    spotify = authorization()
    results = spotify.tracks(song_arr)
    tracks = results["tracks"]
    for track in tracks:
        url_arr.append(track["name"])
    return url_arr
