import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

auth_manager = SpotifyClientCredentials()


def getSongUrls(songArr):
    sp = spotipy.Spotify(auth_manager=auth_manager)
    urlArr = []
    if songArr == None:
        return "Error: No Genre Chosen"
    results = sp.tracks(songArr)
    tracks = results["tracks"]
    for track in tracks:
        url = track["preview_url"]
        if url == None:
            url = "No Preview Available At This Time"
        urlArr.append(url)
    return urlArr


def getSongTitles(songArr):
    sp = spotipy.Spotify(auth_manager=auth_manager)
    urlArr = []
    if songArr == None:
        return "Error: No Genre Chosen"
    results = sp.tracks(songArr)
    tracks = results["tracks"]
    for track in tracks:
        urlArr.append(track["name"])
    return urlArr
