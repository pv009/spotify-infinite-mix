from fastapi import FastAPI
from starlette.responses import RedirectResponse

from spotify_auth import SpotifyAuth

app = FastAPI()
spotify_auth = SpotifyAuth()

@app.get("/")
def hello_world():
    return {"Hello": "World"}

@app.get('/spotify-access-token')
def get_spotify_access_token():
    return spotify_auth.get_access_token()