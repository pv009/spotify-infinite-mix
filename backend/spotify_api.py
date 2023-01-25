
class SpotifyApiConnect(object):
    def __init__(self, access_token):
        self.access_token = access_token
        return None

    def get_random_song(self):
        characters = 'abcdefghijklmnopqrstuvwxyz'
