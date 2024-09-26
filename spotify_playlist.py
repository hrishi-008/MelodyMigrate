import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import dotenv
import os

dotenv.load_dotenv()

def load_env_variables():
    return os.getenv('SPOTIPY_CLIENT_ID'), os.getenv('SPOTIPY_CLIENT_SECRET')

def load_playlist_data(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def authenticate_spotify(client_id, client_secret):
    return spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri="http://example.com",
            client_id=client_id,
            client_secret=client_secret,
            show_dialog=True,
            cache_path="token.txt"
        )
    )

def get_user_id(sp):
    return sp.current_user()["id"]

def search_songs(sp, song_names):
    song_uris = []
    for song in song_names:
        result = sp.search(q=f"track:{song}", type="track")
        try:
            uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
            print(f"Found URI for {song}: {uri}")
        except IndexError:
            print(f"{song} doesn't exist in Spotify. Skipped.")
    return song_uris

def create_playlist(sp, user_id, playlist_name):
    return sp.user_playlist_create(user=user_id, name=f"Playlist from {playlist_name}", public=False)

def add_songs_to_playlist(sp, playlist_id, song_uris):
    if song_uris:
        sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)
        print(f"Added {len(song_uris)} songs to the playlist.")
    else:
        print("No songs were added as none of them were found on Spotify.")

def main():
    SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET = load_env_variables()
    playlist_data = load_playlist_data('playlist_songs.json')
    song_names = playlist_data['songs']
    playlist_url = playlist_data['url']

    sp = authenticate_spotify(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)
    user_id = get_user_id(sp)
    print(f"Authenticated Spotify User ID: {user_id}")

    song_uris = search_songs(sp, song_names)
    playlist_name = input("Enter a name for the new playlist: ")
    playlist = create_playlist(sp, user_id, playlist_name)
    print(f"Created new playlist: {playlist['name']} (ID: {playlist['id']})")

    add_songs_to_playlist(sp, playlist["id"], song_uris)

if __name__ == "__main__":
    main()
