from flask import Flask, render_template, request, redirect
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
app = Flask(__name__)


@app.route('/', methods=['POST','GET'])
def hello_world():
    if request.method == 'POST':
        singer = request.form['id']
        print(singer)
        sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="8f8107cc227845b2a1d232b967cc0965",
                                                                   client_secret="53f5bf50da1e42bc8e0b89db4152a80d"))

        album = []
        results = sp.search(q=singer, limit=50)
        # print(results)
        for idx, track in enumerate(results['tracks']['items']):
            album.append(track['name'])
        return render_template('indexspotify.html',album=album)

    return render_template('indexspotify.html')


if __name__ == "__main__":
    app.run(host="localhost", port=5001, debug=True)