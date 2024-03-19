import spotipy

from spotipy.oauth2 import SpotifyOAuth


def get_track(spotify_client_id, spotify_client_secret):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=spotify_client_id,
        client_secret=spotify_client_secret,
        redirect_uri='https://t.me/spotifysharemusic_bot',
        scope='user-read-currently-playing'
    ))

    results = sp.current_user_playing_track()
    return f"{results['item']['artists'][0]['name']} - {results['item']['name']}"