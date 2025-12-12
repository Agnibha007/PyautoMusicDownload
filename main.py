import os
import json
import subprocess
import time

# BASE PATH = folder where this script lives
BASE_FOLDER = os.path.dirname(os.path.abspath(__file__))


def extract_playlist_id(link):
    if "playlist/" in link:
        return link.split("playlist/")[1].split("?")[0].strip()
    return link.strip()


def fetch_metadata(playlist_url, playlist_id):
    metadata_file = os.path.join(BASE_FOLDER, f"{playlist_id}.spotdl")

    print("\nFetching playlist metadata…")

    subprocess.run([
        "spotdl",
        "save",
        playlist_url,
        "--save-file",
        metadata_file
    ], shell=True)

    time.sleep(1)

    if not os.path.exists(metadata_file):
        print("Metadata file not created.")
        exit()

    return metadata_file


def load_playlist(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    playlist_name = data[0]["list_name"]

    tracks = []
    for track in data:
        title = track["name"].lower()
        artist = track["artists"][0].lower()
        tracks.append({
            "raw": f"{title} {artist}",
            "title": track["name"],
            "artist": track["artists"][0],
        })

    return playlist_name, tracks


def get_local_tracks(folder):
    files = []
    for f in os.listdir(folder):
        if f.lower().endswith((".mp3", ".wav", ".m4a", ".flac")):
            files.append(os.path.splitext(f)[0].lower())
    return files


def download_song(title, artist, folder):
    print(f"\n⬇ Downloading: {title} – {artist}")

    subprocess.run([
        "spotdl",
        f"{title} {artist}",
        "--output",
        folder
    ], shell=True)


def sync_playlist(local, playlist, folder):
    missing = []

    for song in playlist:
        found = any(song["raw"] in l or l in song["raw"] for l in local)
        if not found:
            missing.append(song)

    print("\n=== Missing Songs ===")
    for s in missing:
        print(f" - {s['title']} – {s['artist']}")

    for s in missing:
        download_song(s["title"], s["artist"], folder)


if __name__ == "__main__":
    playlist_url = input("Paste Spotify playlist link: ").strip()
    playlist_id = extract_playlist_id(playlist_url)

    metadata_file = fetch_metadata(playlist_url, playlist_id)

    playlist_name, playlist_tracks = load_playlist(metadata_file)

    playlist_folder = os.path.join(BASE_FOLDER, playlist_name)

    if not os.path.exists(playlist_folder):
        print(f"\nCreating folder: {playlist_folder}")
        os.makedirs(playlist_folder)

    local_tracks = get_local_tracks(playlist_folder)

    sync_playlist(local_tracks, playlist_tracks, playlist_folder)

    print("\n=== PLAYLIST SYNC COMPLETE ===")
