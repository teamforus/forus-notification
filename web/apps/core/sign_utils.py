import hashlib
import json

import requests
from django.conf import settings


class SignUtil():

    def __init__(self, password):
        self.password = password

    def create_hash(self, data):
        newArray = data.copy()
        newArray['password'] = self.password
        sortedArray = json.loads(json.dumps(newArray, sort_keys=True))
        hashString = ''
        for key in sortedArray:
            value = sortedArray[key]
            hashString += str(value)


        hashString = hashlib.sha256(hashString.encode('utf-8')).hexdigest()

        return hashString


