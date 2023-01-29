import random
import string

import requests
from decouple import config


class SpotifyApiConnect(object):
    def __init__(self, access_token):
        self.headers = {
            "Authorization": 'Bearer %s ' % access_token
        }
        return None

    def get_random_songs(self, n_songs=1):
        random_char = random.choice(string.ascii_letters)
        search_strings = [random_char + '%', '%' + random_char + '%']
        random_search = random.choice(search_strings)
        random_offset = random.randrange(0, 1000)

        params = {
            "type": "track",
            "q": random_search,
            "offset": random_offset,
            "limit": n_songs
        }

        url = ("%s/search" % config('SPOTIFY_API_BASE_URL'))
        request = requests.get(url, headers=self.headers, params=params)
        self.put_song_in_queue_and_play(request.json()["tracks"]["items"][0]["id"])
        return request.json()

    def put_song_in_queue_and_play(self, song_id):
        url = ("%s/me/player/queue" % config('SPOTIFY_API_BASE_URL'))
        params = {
            "uri": "spotify:track:%s" % song_id,
        }
        requests.post(url, headers=self.headers, params=params)
        start_play_urls = ["%s/me/player/next" % config('SPOTIFY_API_BASE_URL'), "%s/me/player/play" % config('SPOTIFY_API_BASE_URL')]
        for url in start_play_urls:
            requests.post(url, headers=self.headers)

    def get_song_metadata(self, song_id):
        print(song_id)
        url = ("%s/audio-features/%s" % (config('SPOTIFY_API_BASE_URL'), song_id))
        request = requests.get(url, headers=self.headers)
        return request.json()