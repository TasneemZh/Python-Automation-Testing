import requests


class GetRequest:
    def __init__(self, base_url):
        self.base_url = base_url

    def read_get(self, route):
        response = requests.get(self.base_url + route)
        return response.status_code
