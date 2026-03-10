import requests

from endpoints.endpoint import Endpoint


class CreateMeme(Endpoint):

    def create_meme(self, body, headers=None):
        headers = headers
        url = f"{self.url}/meme"
        self.response = requests.post(url, json=body, headers=headers)
        try:
            self.json = self.response.json()
        except ValueError:
            self.json = {}
        if self.response.status_code == 401:
            raise Exception("Unauthorized! Token may be invalid or expired")

        return self.response
