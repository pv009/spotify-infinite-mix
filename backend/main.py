import string

from fastapi import FastAPI, Header, Request
from fastapi.middleware.cors import CORSMiddleware

from services.train import TrainAlgo
from services.spotify_api import SpotifyApiConnect
from services.spotify_auth import SpotifyAuth

origins = [
    "http://localhost",
    "http://localhost:9000",
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
spotify_auth = SpotifyAuth()

@app.get("/")
def hello_world():
    return {"Hello": "World"}

@app.get('/spotify/access-token/')
def get_spotify_access_token(code):
    return spotify_auth.get_access_token(code)

@app.get('/spotify/refresh-token/')
def refresh_spotify_access_token(refresh_token):
    return spotify_auth.refresh_access_token(refresh_token)

@app.get('/spotify/random-song/')
def refresh_spotify_access_token(request: Request):
    spotify_api = SpotifyApiConnect(request.headers.get("spotify_access"))
    return spotify_api.get_random_songs()

@app.get('/spotify/meta-data/{id}')
def get_song_metadata(id, request: Request):
    spotify_api = SpotifyApiConnect(request.headers.get("spotify_access"))
    return spotify_api.get_song_metadata(song_id=id)

@app.post('/data/song-data/')
def save_song_data(data):
    print(data)
    train = TrainAlgo()
    train.save_listening_data(data)
    return data