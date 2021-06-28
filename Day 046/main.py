from bs4 import BeautifulSoup
import requests
from pprint import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date_entry = input(
    "Which year do you want to travel to? Type the date in YYYY-MM-DD format: "
)
year = date_entry.split('-')[0]

############# Scraping ##################

scrape_url = f"https://www.billboard.com/charts/hot-100/{date_entry}"

response = requests.get(scrape_url)
response.raise_for_status()

soup = BeautifulSoup(response.content, "html.parser")
tracks_elements = soup.find_all(
    name="span", class_="chart-element__information__song text--truncate color--primary"
)

tracks = [element.string for element in tracks_elements]

#pprint(tracks)

# #################### Spotify API ###########################

spotify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
    )
)

tracks_uris = []

for track in tracks:
    results = spotify.search(q=f"track: {track} year: {year}", type="track")
    try:
        tracks_uris.append(results["tracks"]["items"][0]["uri"])
    except:
        print(f"{track} track doesn't exist in Spotify!")

user_id = spotify.me()['id']
playlist_info = spotify.user_playlist_create(user=user_id, name=f"{date_entry} Billboard 100", public=False)
#pprint(playlist_info)
spotify.playlist_add_items(playlist_id=playlist_info['id'], items=tracks_uris)

