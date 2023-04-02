import spotipy
from spotipy.oauth2 import SpotifyOAuth
from authorization.auth import get_spotify_obj
# from auth import get_spotify_obj

scope = "user-read-email playlist-modify-public user-library-read user-library-modify"

sp = get_spotify_obj(scope)

def get_top_songs(limit, time_range):
    results = sp.current_user_top_tracks(limit=limit, offset=0, time_range=time_range)

    thisList = []

    for idx, item in enumerate(results['items']):
        name = item['name']
        song_id = item['id']
        artist = item['artists']
        artist_name = artist[0]
        artist_name = artist_name['name']
        songDict = {'name' : name, 'song_id' : song_id, 'artist_name' : artist_name}
        thisList.append(songDict)
    return thisList

def get_top_artists(limit, time_range):
    results = sp.current_user_top_artists(limit=limit, offset=0, time_range=time_range)

    artists = []

    for idx, item in enumerate(results['items']):
        popularity = item['popularity']
        genres = item['genres']
        name = item['name']
        artist_id = item['id']

        artist = {"artist_name" : name, "artist_popularity" : popularity, "artist_id" : artist_id}

        artists.append(artist)
    return artists



def get_featured_playlists(limit):
    results = sp.featured_playlists(locale=None, country=None, timestamp=None, limit=limit, offset=0)
    
    playlistDict = {}
    print(results['message'])
    for idx, item in enumerate(results['playlists']['items']):
        name = item['name']
        description = item['description']
        playlistDict[idx] = (name, " - ", description)

        print(idx + 1, " - ", name, " - ", description)

def make_playlist(name, is_public, is_collaborative, description ):
    return sp.user_playlist_create(sp.me()['id'], name, public=is_public, collaborative=is_collaborative, description=description)


def get_user():
    return sp.me()

def add_to_playlist(playlist_id, items):
    sp.playlist_add_items(playlist_id, items, position=None)

def get_playlists(limit):
    results = sp.current_user_playlists(limit=limit)

    playlistDict = {}
    for idx, item in enumerate(results['items']):
        playlistDict[item['Name']] = item['id']
        #print(idx + 1, " - ", item['name'], " - ", item['id'])

def recommendations_for_user(limit, time_range):
    #each of these calls to get functions return a dictionary
    #the dictionaries are keyed by name, and they return the id of the item
    #which the recommendations function needs


    artist_ids = []

    for artist_dict in get_top_artists(1,time_range):
        artist_ids.append(artist_dict["artist_id"])

    song_ids = []

    for song_dict in get_top_songs(1,time_range):
        song_ids.append(song_dict["song_id"])

    seeds = sp.recommendation_genre_seeds()

    return sp.recommendations(seed_artists = artist_ids,seed_genres = seeds, seed_tracks = song_ids, limit = limit, country = "US")

def recommended_playlist(limit, time_range):
    recc = recommendations_for_user(limit,time_range)

    new_playlist_id = make_playlist("Simplify Recommendations", True, False, "Your recommended songs! :D")['id']


    recc_song_ids = []
    for item in recc['tracks']:
        recc_song_ids.append(item['id'])

    add_to_playlist(new_playlist_id, recc_song_ids)
    return new_playlist_id