from decouple import config
import requests
import base64

class SpotifyAuth(object):
    def __init__(self):
        self.authorization_string = config('SPOTIFY_CLIENT_ID') + ':' + config('SPOTIFY_CLIENT_SECRET')
        self.headers = headers = {
            "Authorization": "Basic %s" % (base64.b64encode(self.authorization_string.encode('utf-8')).decode('utf-8')),
            "Content-Type": "application/x-www-form-urlencoded"
        }
        return None

    def get_access_token(self, spotify_code):
        payload = {
            "grant_type": "authorization_code",
            "code": spotify_code,
            "redirect_uri": config('SPOTIFY_REDIRECT_URL')
        }

        url = ("%s/api/token" % config('SPOTIFY_AUTH_BASE_URL'))
        request = requests.post(url, headers=self.headers ,data=payload)
        return request.json()

    def refresh_access_token(self, refresh_token):
        payload = {
            "grant_type": "refresh_token",
            "refresh_token": refresh_token
        }
        url = ("%s/api/token" % config('SPOTIFY_AUTH_BASE_URL'))
        print(url)
        request = requests.post(url, headers=self.headers, data=payload)
        return request.json()