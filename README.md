Built with ❤️ by Agnibha Mukherjee
# 🎵 Spotify Playlist Auto Sync
### Automatically mirror ANY Spotify playlist to your local system.
Created by **Agnibha Mukherjee**

---

## 🚀 What This Tool Does

This project allows you to **auto-sync your local music folder** with any Spotify playlist.

Just paste a playlist link — the script handles everything:

- Fetches playlist metadata (`spotdl save`)
- Reads track list automatically
- Detects or creates a local folder for the playlist
- Compares downloaded songs with the Spotify playlist
- **Downloads only the missing tracks**
- Saves them neatly inside the playlist-named folder
- Runs fully offline after metadata fetch

No Spotify API.  
No scraping.  
No manual work.  

---

## 🧠 How It Works (Simplified)

1. You paste a Spotify playlist link.  
2. Script extracts the playlist ID.  
3. The script runs:



spotdl save <playlist_url> --save-file <id>.spotdl


4. Playlist metadata is saved locally.  
5. The script creates a folder named after the playlist (if missing).  
6. It compares Spotify tracks with your local tracks.  
7. It automatically downloads missing songs via:



spotdl "<song name> <artist>" --output "<playlist_folder>"


8. You get a fully synced offline version of your playlist.

---

## 📂 Folder Structure

After syncing, your folder looks like this:



/project-directory
├── autosync.py
├── requirements.txt
├── <playlist_id>.spotdl # automatically generated
├── <Playlist Name>/ # all songs stored here
├── song1.mp3
├── song2.mp3
└── ...


The script works **relative to its own folder**, so the repo remains portable.

---

## 🔧 Requirements

Install dependencies:



pip install -r requirements.txt


Currently required:



spotdl>=4.4.0


Also ensure `ffmpeg` is installed on your system (required by spotdl):  
https://ffmpeg.org/download.html

---

## ▶️ Usage

Run:



python autosync.py


Then paste your playlist link, for example:



https://open.spotify.com/playlist/4PKHQkiYTUKThUJYhTGEZG


The script handles everything from there — metadata retrieval, folder creation, syncing, and downloading.

---

## 🖼 Example Output