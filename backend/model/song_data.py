from typing import Union
from pydantic import BaseModel

class SongData(BaseModel):
    acousticness: float
    analysis_url: str
    danceability: float
    duration_ms: float
    energy: float
    id: str
    instrumentalness: float
    key: float
    liveness: float
    loudness: float
    mode: float
    speechiness: float
    tempo: float
    time_signature: float
    track_href: str
    type: str
    uri: str
    valence: float
    percent_listened: Union[float, None] = None
