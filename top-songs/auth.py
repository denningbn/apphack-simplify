import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-top-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, 
                                               client_id='9b0951c26e85405697a1e52e99937b35',
                                               client_secret='b537e7f688ec45189a529da5ed5cdb61',
                                               redirect_uri='http://localhost:3000'))


#results = sp.current_user_saved_tracks()

results = sp.current_user_top_tracks(limit=20, offset=0, time_range='medium_term')


#for idx, item in enumerate(results['items']):
#    track = item['track']
#    print(idx, track['artists'][0]['name'], " - ", track['name'])
