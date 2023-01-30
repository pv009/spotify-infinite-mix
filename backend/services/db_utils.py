import os
import sqlite3

current_directory = os.path.dirname(__file__)
db = os.path.join(current_directory, '../data/song_data.sqlite')

def sqlite_entry(data):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    song_data = dict(data)
    cursor.execute("INSERT INTO song_data (acousticness, danceability, energy, instrumentalness, key, liveness, "
                   "loudness, mode, speechiness, tempo, valence, percent_listened) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (song_data["acousticness"], song_data["danceability"], song_data["energy"], song_data["instrumentalness"],
                   song_data["key"], song_data["liveness"], song_data["loudness"], song_data["mode"],
                   song_data["speechiness"], song_data["tempo"], song_data["valence"], song_data["percent_listened"]))
    conn.commit()
    conn.close()
