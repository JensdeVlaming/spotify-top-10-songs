# Spotify Top 10 Songs of Artist
Get top 10 songs of an artist and store it in a playlist with name 'Artist - Top 10 Songs'

# Usage

## Create application in Spotify dashboard

Copy ````client ID````, ```client Secret``` and set *Redirect URI in settings* of application to ```http://127.0.0.1:8080/```

## Use export (macOS) or set (Windows, Linux) to setup environment variables
```
MacOS
export SPOTIPY_CLIENT_ID=<client id> (without < and >)
export SPOTIPY_CLIENT_SECRET=<client secret> (without < and >)
export SPOTIPY_REDIRECT_URI=http://127.0.0.1:8080/ 
export SPOTIPY_USERNAME=<your spotify username> (without < and >)

Windows, Linux
set SPOTIPY_CLIENT_ID=<client id> (without < and >)
set SPOTIPY_CLIENT_SECRET=<client secret> (without < and >)
set SPOTIPY_REDIRECT_URI=http://127.0.0.1:8080/
set SPOTIPY_USERNAME=<your spotify username> (without < and >)
```

## Run python file
```
python3 run.py
```
