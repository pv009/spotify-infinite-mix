from decouple import config
import requests
import base64

class SpotifyAuth(object):
    def __init__(self):
        return None

    def get_access_token(self, spotify_code):
        payload = {
            "grant_type": "authorization_code",
            "code": spotify_code,
            "redirect_uri": config('SPOTIFY_REDIRECT_URL')
        }
        authorization_string = config('SPOTIFY_CLIENT_ID') + ':' + config('SPOTIFY_CLIENT_SECRET')
        headers = {
            "Authorization": "Basic %s" % (base64.b64encode(authorization_string.encode('utf-8')).decode('utf-8')),
            "Content-Type": "application/x-www-form-urlencoded"
        }
        url = ("%s/api/token" % config('SPOTIFY_AUTH_BASE_URL'))
        request = requests.post(url, headers=headers ,data=payload)
        return request.json()