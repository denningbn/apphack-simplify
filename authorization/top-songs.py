import spotipy
from spotipy.oauth2 import SpotifyOAuth
from auth import get_spotify_obj

scope = "user-read-email playlist-modify-public user-library-read user-library-modify"

sp = get_spotify_obj(scope)

def get_top_songs(limit, time_range):
    results = sp.current_user_top_tracks(limit=limit, offset=0, time_range=time_range)

    songDict = {}
    for idx, item in enumerate(results['items']):
        album = item['album']
        name = item['name']

        songdict[idx] = (album, " - ", name)
        #print (idx + 1, album['artists'][0]['name'], " - ",album['name'], " - ", name)
    return songDict

def get_top_artists():
    results = sp.current_user_top_artists(limit=20, offset=0, time_range='medium_term')

    artistsDict = {}

    for idx, item in enumerate(results['items']):
        popularity = item['popularity']
        genres = item['genres']
        name = item['name']
        artistDict[idx] = (name)

        #print(idx + 1, " - ", name)
    return artistDict



def get_featured_playlists():
    results = sp.featured_playlists(locale=None, country=None, timestamp=None, limit=20, offset=0)
    
    playlistDict = {}
    print(results['message'])
    for idx, item in enumerate(results['playlists']['items']):
        name = item['name']
        description = item['description']
        playlistDict[idx] = (name, " - ", description)

        print(idx + 1, " - ", name, " - ", description)

def make_playlist(name, is_public, is_collaborative, description ):
    sp.user_playlist_create(sp.me()['id'], name, public=is_public, collaborative=is_collaborative, description=description)

def get_user():
    return sp.me()

def add_to_playlist(playlist_id, items):
    sp.playlist_add_items(playlist_id, items, position=None)

def get_playlists():
    results = sp.current_user_playlists(limit=10)

    playlistDict = {}
    for idx, item in enumerate(results['items']):
        playlistDict[idx] = (item['Name'], " - ", item['id'])
        print(idx + 1, " - ", item['name'], " - ", item['id'])

def get_top_genres():
    results = sp.current_user_top_artists(limit=20, offset=0, time_range='medium_term')
    
    genres = []

    for genre in results:
        genres.append(genre)

def recommend_genres():
    seeds = recommendation_genre_seeds()
    recommendations

