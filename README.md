# 🎵 Spotify Statistics 🎵

Discover your Spotify listening habits directly in your terminal! This Python script provides insights into:

- **Now Playing** cuurent track 
- **Top Songs, Artists, Albums, and Genres** over different time periods (last 4 weeks, last 6 months, all time)  

---

## 1) Prerequisites

Before you start, make sure you have:

- **Python 3.7 or higher**  
- Installed Python packages: `spotipy` and `colorama`  
- Have an active Spotify account


## 2) Get Your Spotify API Credentials
Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) and create a Spotify Developer Account
- Create a new application.
- Copy the Client ID and Client Secret.
- Set a Redirect URI (this must match the URI you’ll use in the script):

```python
CLIENT_ID = 'your_client_id_here'
CLIENT_SECRET = 'your_client_secret_here'
REDIRECT_URI = 'your_redirect_uri_here'
```

## 3) Run Code in Terminal

```python
python spotify_listening_stats.py
```
