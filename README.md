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
├── main.py
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



python main.py


Then paste your playlist link, for example:



https://open.spotify.com/playlist/4PKHQkiYTUKThUJYhTGEZG


The script handles everything from there — metadata retrieval, folder creation, syncing, and downloading.

---

## 🖼 Example Output
Fetching playlist metadata…

Creating folder: /SpotifySync/Bengali Songs

=== Missing Songs ===

Ei Meghla Dine Ekla – Hemanta Mukherjee

Ami Dur Hote Tomarei Dekhechhi – Hemant Kumar

⬇ Downloading: Ei Meghla Dine Ekla – Hemanta Mukherjee
⬇ Downloading: Ami Dur Hote Tomarei Dekhechhi – Hemant Kumar

=== PLAYLIST SYNC COMPLETE ===


---

## ✨ Features

- ✔ Fully automated syncing  
- ✔ Local folder auto-detection  
- ✔ Automatic metadata fetching  
- ✔ Only downloads missing songs  
- ✔ Clean project structure  
- ✔ No hardcoded paths  
- ✔ GitHub-friendly  
- ✔ Perfect for public use  

---

## 📘 FAQ

### **Does this use Spotify’s API?**  
No. It uses `spotdl`, which handles metadata extraction independently.

### **Is downloading songs legal?**  
Downloading copyrighted content without rights may violate terms.  
This tool is for personal backup/educational use.

---

## 👨‍💻 Author

**Agnibha Mukherjee**  
Student • Developer • Automation Enthusiast  

If you found this useful, consider ⭐ starring the repository!

---

## 📝 License

This project is open-source under the MIT License.