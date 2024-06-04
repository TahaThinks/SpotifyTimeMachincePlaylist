from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

base_url = "https://www.billboard.com/charts/hot-100/"
time = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
endpoint_url = f"{base_url}{time}/"
print(endpoint_url)

response = requests.get(endpoint_url)


soup = BeautifulSoup(response.text, 'html.parser')
print(f"{soup.title.text} of {time}")
songs_tags = soup.find_all("h3", class_="u-line-height-125")
songs = []
for song_name in songs_tags:
    songs.append(song_name.getText().strip())

print(songs)

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="YOUR_APP_CLIENT_ID",
                                                           client_secret="YOUR_APP_CLIENT_SECRET"))
