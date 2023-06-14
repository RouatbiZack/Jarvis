import spacy
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import webbrowser
import time

nlp = spacy.load('en_core_web_sm')
CLIENT_ID = '82030908468a432591f88f355005b929'
CLIENT_SECRET = '71954609040e48ba9c6951c55d27a037'
PLAYLISTS = {
    'relaxed': '37i9dQZF1DWZeKCadgRdKQ',
    'energetic': '37i9dQZF1DXdxcBWuJkbcy',
    'working out': '37i9dQZF1DX76Wlfdnj7AP',
    'studying': '37i9dQZF1DX8NTLI2TtZa6',
    'sad': '37i9dQZF1DX7qK8ma5wgG1',
    'lonely': '37i9dQZF1DX8ymr6UES7vc',
    'in love': '37i9dQZF1DWZqd5JICZI0u',
    'happy': '37i9dQZF1DXdPec7aLTmlC',
    'confused': '37i9dQZF1DWTyiBJ6yEqeu',
    'adventurous': '37i9dQZF1DX1tyCD9QhIWF',
    'motivational': '37i9dQZF1DX7gIoKXt0gmx',
    'romantic': '37i9dQZF1DX1kznM9Kyjo6',
    'chill': '37i9dQZF1DWZeKCadgRdKQ',
    'party': '37i9dQZF1DX4FPkfQH6ZB0',
    'uplifting': '37i9dQZF1DWU0ScTcjJBdj'}



def get_user_preferences(user_input):
    doc = nlp(user_input)
    keywords = [token.text for token in doc if token.pos_ == 'ADJ' or token.pos_ == 'NOUN']
    mood = None
    for keyword in keywords:
        if keyword.lower() in PLAYLISTS:
            mood = keyword.lower()
            break
    return mood

def search_playlists(mood):
 try :
    client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    playlist_id = PLAYLISTS.get(mood)
    if playlist_id is not None:
        playlist = sp.playlist(playlist_id)
        return playlist['tracks']['items']
    else:
        return None
 except:
    print('unknow error')



def play_on_youtube(playlist):
  try:  
    if playlist:
        first_track = playlist[0]['track']
        query = f"{first_track['artists'][0]['name']} {first_track['name']} lyrics"
        url = f"https://www.youtube.com/results?search_query={query}"
        webbrowser.open_new_tab(url)
        time.sleep(5) # wait for page to load
        play_button = webbrowser.find_element_by_class_name('ytp-play-button')
        play_button.click()
    else:
        print("No playlist found.")
  except :
      print("unknown error")


