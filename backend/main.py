from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from spotify_auth import SpotifyAuth

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

@app.get('/spotify-access-token/')
def get_spotify_access_token(code):
    return spotify_auth.get_access_token(code)