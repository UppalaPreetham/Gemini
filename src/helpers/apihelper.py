import requests, json
from src.helpers.loghelper import Logger;

"""
Class for helping with rest api
"""


class ApiHelper:
    logger = None

    def __init__(self):
        self.logger = Logger

    def getDetails(self, url):
        response = requests.get(url)
        return response.json()


