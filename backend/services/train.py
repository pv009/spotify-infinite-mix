from decouple import config
import requests
import base64

from .db_utils import sqlite_entry


class TrainAlgo(object):
    def __init__(self):
        return None

    def save_listening_data(self, data):
        sqlite_entry(data)