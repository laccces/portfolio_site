from flask import Flask, render_template
import requests
import base64
import json
import os

app = Flask(__name__)

# Spotify App Client ID and Client Secret
CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')

# Spotify API URLs
TOKEN_URL = 'https://accounts.spotify.com/api/token'
PLAYLIST_URL = 'https://api.spotify.com/v1/playlists/your_playlist_id'

@app.route('/')
def index():
    # Get access token from Spotify Web API
    auth_header = base64.b64encode(f'{CLIENT_ID}:{CLIENT_SECRET}'.encode('ascii')).decode('ascii')
    headers = {'Authorization': f'Basic {auth_header}'}
    data = {'grant_type': 'client_credentials'}
    response = requests.post(TOKEN_URL, headers=headers, data=data)
    access_token = response.json()['access_token']

    # Get playlist data from Spotify Web API
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(PLAYLIST_URL, headers=headers)
    playlist_data = response.json()

    # Get track URIs from playlist data
    track_uris = [track['track']['uri'] for track in playlist_data['tracks']['items']]

    # Render template with track URIs for embedded player
    return render_template('index.html', track_uris=track_uris)

if __name__ == '__main__':
    app.run()
