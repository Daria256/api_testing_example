import requests

from endpoints.endpoint import Endpoint


class UpdateMeme(Endpoint):

    def update_meme(self, meme_id, body, headers=None):
        headers = headers or self.headers
        update_url = f"{self.url}/meme/{meme_id}"
        self.response = requests.put(update_url, json=body, headers=headers)
        try:
            self.json = self.response.json()
        except ValueError:
            self.json = {}

        if self.response.status_code == 401:
            raise Exception("Unauthorized! Token may be invalid or expired")

        return self.response
