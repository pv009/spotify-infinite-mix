import os
import sqlite3

current_directory = os.path.dirname(__file__)
db = os.path.join(current_directory, 'data/song_data.sqlite')

def sqlite_entry(json_object):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO song_data (acousticness, danceability, energy, instrumentalness, key, liveness, "
                   "loudness, mode, speechiness, tempo, valence, percent_listened) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   json_object["acousticness"], json_object["danceability"], json_object["energy"], json_object["instrumentalness"],
                   json_object["key"], json_object["liveness"], json_object["loudness"], json_object["mode"],
                   json_object["speechiness"], json_object["tempo"], json_object["valence"], json_object["percent_listened"])
    conn.commit()
    conn.close()
