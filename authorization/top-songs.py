import spotipy
from spotipy.oauth2 import SpotifyOAuth
from auth import get_spotify_obj

scope = "user-top-read"

sp = get_spotify_obj(scope)

def get_top_songs(limit, time_range):
    results = sp.current_user_top_tracks(limit=limit, offset=0, time_range=time_range)

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

def get_featured_playlists():
    results = sp.featured_playlists(locale=None, country=None, timestamp=None, limit=20, offset=0)
    
    print(results['message'])
    for idx, item in enumerate(results['playlists']['items']):
        name = item['name']
        description = item['description']
        print(idx + 1, " - ", name, " - ", description)

get_top_songs(20, 'medium_term')