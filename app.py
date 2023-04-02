from flask import Flask, jsonify
from authorization.auth import get_spotify_obj
from authorization import top_songs

app = Flask(__name__)


@app.route("/user")
def user():
    user = top_songs.get_user()
    response = jsonify(user)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/top-tracks/<timeframe>")
def top_tracks(timeframe):
    tracks = top_songs.get_top_songs(20, timeframe)

    response = jsonify(tracks)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/make-playlist")
def make_playlist():
    playlist = top_songs.recommended_playlist(25, 'medium_term')
    response = jsonify(playlist)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
