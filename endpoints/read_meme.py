import requests

from endpoints.endpoint import Endpoint


class ReadCreatedMeme(Endpoint):
    def check_meme_not_exist(self, meme_id, headers=None):
        headers = headers or self.headers
        response = requests.get(f"{self.url}/meme/{meme_id}", headers=headers)
        assert (
            response.status_code == 404
        ), f"Meme still exists after deletion, got {response.status_code}. Response: {response.text}"
