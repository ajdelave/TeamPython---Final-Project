import os
import sys
import json
import spotipy
import spotipy.util as util
from json.decoder import JSONDecodeError
import spotify_info
import sqlite3


# Import Spotify API info from spotify_info.py
username = spotify_info.username
scope = 'user-top-read'
client_id = spotify_info.client_id
client_secret = spotify_info.client_secret
redirect_uri = spotify_info.redirect_uri
token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

# Create Spotify Object
spotify_object = spotipy.Spotify(auth=token)

# Create database and add table "Spotify_Song_Info"
conn = sqlite3.connect('sql_data.sqlite')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS Spotify_Song_Info (id INTEGER PRIMARY KEY, track_title TEXT UNIQUE, artist TEXT, track_number INTEGER, release_year INTEGER, popularity INTEGER)''')

print('')
print('Connecting to Spotify API and Creating Database...')
print('')

# These three functions make requests to Spotify's API to get a user's song preference over the past:
    # week
    # six months
    # entire account lifetime

# New favorite songs will be added to the database if the function is called every day.

def get_data_short_term():
    # Only the top 50 songs are grabbed for the week
    user_top_tracks = spotify_object.current_user_top_tracks(limit=50,offset=0,time_range='short_term')
    for x in user_top_tracks['items']:
        track_title = x['name']
        artist = x['artists'][0]['name']
        track_number = x['track_number']
        full_release_date = x['album']['release_date']
        release_year = full_release_date[:4]
        popularity = x['popularity']

        # No repeat entries will be added
        cur.execute('INSERT OR IGNORE INTO Spotify_Song_Info (track_title, artist, track_number, release_year, popularity) VALUES (?, ?, ?, ?, ?)', (track_title, artist, track_number, release_year, popularity))
    conn.commit()

def get_data_medium_term():
    # Only the top 20 songs are grabbed for the last 6 months
    user_top_tracks = spotify_object.current_user_top_tracks(limit=50,offset=0,time_range='medium_term')
    for x in user_top_tracks['items']:
        track_title = x['name']
        artist = x['artists'][0]['name']
        track_number = x['track_number']
        full_release_date = x['album']['release_date']
        release_year = full_release_date[:4]
        popularity = x['popularity']

        # No repeat entries will be added
        cur.execute('INSERT OR IGNORE INTO Spotify_Song_Info (track_title, artist, track_number, release_year, popularity) VALUES (?, ?, ?, ?, ?)', (track_title, artist, track_number, release_year, popularity))
    conn.commit()

def get_data_long_term():
    # Only the top 20 songs are grabbed for account's lifetime
    user_top_tracks = spotify_object.current_user_top_tracks(limit=50,offset=0,time_range='long_term')
    for x in user_top_tracks['items']:
        track_title = x['name']
        artist = x['artists'][0]['name']
        track_number = x['track_number']
        full_release_date = x['album']['release_date']
        release_year = full_release_date[:4]
        popularity = x['popularity']

        # No repeat entries will be added
        cur.execute('INSERT OR IGNORE INTO Spotify_Song_Info (track_title, artist, track_number, release_year, popularity) VALUES (?, ?, ?, ?, ?)', (track_title, artist, track_number, release_year, popularity))
    conn.commit()

# Call the functions
get_data_short_term()
get_data_medium_term()
get_data_long_term()

# Inform user that the this program has ended
print('Connection Ended')