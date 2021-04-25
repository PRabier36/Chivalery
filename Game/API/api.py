import requests


class Api:
    def __init__(self):
        self.__api_url = "http://localhost:3001"

    def request(self, address, verb="GET", headers={}, payload={}):
        # print("api.payload :"+payload)
        return requests.request(verb, (self.__api_url + address), headers=headers, json=payload)

