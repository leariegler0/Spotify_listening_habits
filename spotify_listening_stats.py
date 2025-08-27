import spotipy
from spotipy.oauth2 import SpotifyOAuth
from colorama import Style

def colorize(text, color):
    colors = {
        'black': '\033[30m',
        'deepblue': '\033[34m',
        'steelblue': '\033[38;5;75m'
    }
    return f"{colors.get(color, '')}{text}{Style.RESET_ALL}"

LABELS = {
    'short_term': 'short term',
    'medium_term': 'mid term',
    'long_term': 'long term',
}

def print_top(sp, time_range, description):
    print(colorize(f"\n{LABELS.get(time_range, time_range)} ({description})", 'black'))

    # Top Songs
    top_songs = sp.current_user_top_tracks(limit=10, time_range=time_range)
    print(colorize("\nTop 10 Songs:", 'black'))
    for idx, song in enumerate(top_songs['items'], 1):
        artists = ', '.join([artist['name'] for artist in song['artists']])
        print(f"{idx}. {colorize(song['name'], 'deepblue')} - {colorize(artists, 'steelblue')}")

    # Top Artists
    top_artists = sp.current_user_top_artists(limit=10, time_range=time_range)
    print(colorize("\nTop 10 Artists:", 'black'))
    for idx, artist in enumerate(top_artists['items'], 1):
        print(f"{idx}. {colorize(artist['name'], 'deepblue')}")

    # Top Albums (from top tracks)
    albums = {}
    for track in top_songs['items']:
        album_name = track['album']['name']
        artists = ', '.join([artist['name'] for artist in track['album']['artists']])
        albums[album_name] = artists
    print(colorize("\nTop 10 Albums (from top tracks):", 'black'))
    for idx, (album_name, artists) in enumerate(list(albums.items())[:10], 1):
        print(f"{idx}. {colorize(album_name, 'deepblue')} - {colorize(artists, 'steelblue')}")

    # Top Genres (up to 10)
    genres = []
    for artist in top_artists['items']:
        genres.extend(artist['genres'])
    genre_count = {}
    for g in genres:
        genre_count[g] = genre_count.get(g, 0) + 1
    sorted_genres = sorted(genre_count.items(), key=lambda x: x[1], reverse=True)[:10]
    print(colorize("\nTop Genres (up to 10):", 'black'))
    for idx, (genre, count) in enumerate(sorted_genres, 1):
        print(f"{idx}. {colorize(genre, 'deepblue')} - {colorize(str(count), 'steelblue')}")


def get_spotify_stats():
    CLIENT_ID = 'Insert your Client ID'
    CLIENT_SECRET = 'Insert your Client Secret'
    REDIRECT_URI = 'http://127.0.0.1:8888/callback'
    SCOPE = 'user-read-playback-state user-top-read'

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=SCOPE
    ))

    # --- Now Playing ---
    now_playing = sp.current_playback()
    if now_playing and now_playing['is_playing']:
        track_name = now_playing['item']['name']
        artists = ', '.join([artist['name'] for artist in now_playing['item']['artists']])
        print(f"\nNow Playing: {colorize(track_name, 'deepblue')} - {colorize(artists, 'steelblue')}")

    print_top(sp, 'short_term', 'last 4 weeks')
    print_top(sp, 'medium_term', 'last 6 months')
    print_top(sp, 'long_term', 'last years')


if __name__ == "__main__":
    get_spotify_stats()
