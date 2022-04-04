import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)


def getSongUrls(songArr):
    urlArr = []
    results = sp.tracks(songArr)
    tracks = results["tracks"]
    for track in tracks:
        urlArr.append(track["preview_url"])
    return urlArr
