from flask import Flask, jsonify
from authorization.auth import get_spotify_obj
from authorization import top_songs

app = Flask(__name__)


@app.route("/user")
def user():
    user = top_songs.get_user()
    print(user)
    # sp_obj = get_spotify_obj(scope)
    # test_response = {'number': 17}
    # return test_response
    # results = sp_obj.current_user_saved_tracks()
    response = jsonify(user)
    # response = jsonify({'some': 'data'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/top-tracks")
def top_tracks():
    tracks = top_songs.get_top_songs(20, 'medium_term')

    response = jsonify(tracks)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# results = sp_obj.current_user_saved_tracks()

# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " - ", track['name'])
# print('hello world')
# return "<p>Hello, World!</p>"
