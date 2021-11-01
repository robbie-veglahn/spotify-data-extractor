import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time
import os
from dotenv import load_dotenv


# @ROB TO DO: turn this into OOP, create a Track Class that contains features
load_dotenv(".env")

CLIENT_ID = os.environ.get('ID')
CLIENT_SECRET = os.environ.get('SECRET')
client_credentials_manager = SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def getPlaylistTracks(user_id, playlist_id):
    """
    getTracks takes in a playlist_id and a user_id, and returns an array full..
    of all relevant track ids on that playlist
    """
    playlist = sp.user_playlist(user_id, playlist_id)
    ids = []
    for item in playlist['tracks']['items']:
        track = item['track']
        ids.append(track['id'])
    return ids

def getTrackFeatures(track_id):
    features = sp.audio_features(track_id)
    meta_data = sp.track(track_id)

    # fetch features
    acousticness = features[0]['acousticness']
    danceability = features[0]['danceability']
    liveness = features[0]['liveness']
    loudness = features[0]['loudness']
    energy = features[0]['energy']
    instrumentalness = features[0]['instrumentalness']
    speechiness = features[0]['speechiness']
    tempo = features[0]['tempo']
    time_signature = features[0]['time_signature']

    # fetch meta_data
    name = meta_data['name']
    album = meta_data['album']['name']
    artist = meta_data['album']['artists'][0]['name']
    release_date = meta_data['album']['release_date']
    length = meta_data['duration_ms']
    popularity = meta_data['popularity']

    track = [name, album, artist, release_date, length, popularity, danceability, acousticness, danceability, energy, instrumentalness, liveness, loudness, speechiness, tempo, time_signature]
    return track

def getPlaylistDataSet(user_id, playlist_id):
    # loop over track ids 
    ids = getPlaylistTracks(user_id, playlist_id)
    tracks = []
    for i in range(len(ids)):
        time.sleep(.5)
        track = getTrackFeatures(ids[i])
        tracks.append(track)
    # create dataset
    df = pd.DataFrame(tracks, columns = ['name', 'album', 'artist', 'release_date', 'length', 'popularity', 'danceability', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'time_signature'])
    df.to_csv("spotify.csv", sep = ',')
    return df