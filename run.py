import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import os

scope = 'playlist-modify-public'
username = os.environ.get('SPOTIPY_USERNAME')

token = SpotifyOAuth(scope=scope, username=username)
spotifyObject = spotipy.Spotify(auth_manager = token)

artistInput = input('Input Artist Name: ') # Input artist name

search = spotifyObject.search(q='artist:' + artistInput, type='artist') # Search for artist

raw_artistURI = json.dumps(search['artists']['items'][0]['uri'],sort_keys=4, indent=4) # Raw data of artist URI
raw_aristNAME = json.dumps(search['artists']['items'][0]['name'], sort_keys=4, indent=4) # Raw data of artist name

artistURI = raw_artistURI.replace('"', '') # Clean data of artist URI
artistNAME = raw_aristNAME.replace('"', '') # Clean data of artist name

spotifyObject.user_playlist_create(user=username, public=True, name=artistNAME + ' - Top 10 Songs') # Create playlist with name of artist + - Top 10 Songs

results = spotifyObject.artist_top_tracks(artistURI) # Get top 10 songs of artist

list_of_songs = []

for track in results['tracks']:
    list_of_songs.append(track['uri']) # Store top 10 tracks of artist in list 

prePlaylist = spotifyObject.user_playlists(user=username)
playlist = prePlaylist['items'][0]['id']

spotifyObject.user_playlist_add_tracks(user=username, playlist_id=playlist, tracks=list_of_songs) # Add top 10 songs to created playlist
print('Succesfully created playlist with top 10 songs of', artistNAME)