import spotipy
from spotipy.oauth2 import SpotifyOAuth
from auth import get_spotify_obj

scope = "user-top-read"

sp = get_spotify_obj(scope)

def get_top_songs():
    results = sp.current_user_top_tracks(limit=20, offset=0, time_range='medium_term')

    for idx, item in enumerate(results['items']):
        album = item['album']
        name = item['name']
        print (idx + 1, album['artists'][0]['name'], " - ",album['name'], " - ", name)


def get_top_albums():
    results = sp.current_user_top_artists(limit=20, offset=0, time_range='medium_term')

    for idx, item in enumerate(results['items']):
        popularity = item['popularity']
        genres = item['genres']
        name = item['name']

        print(idx + 1, " - ", name)


