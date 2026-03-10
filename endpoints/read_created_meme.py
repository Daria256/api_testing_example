import requests

from endpoints.endpoint import Endpoint


class ReadCreatedMeme(Endpoint):
    def read_created_meme(self, meme_id, headers=None):
        headers = headers or self.headers
        update_url = f"{self.url}/meme/{meme_id}"
        session = requests.Session()
        self.response = session.get(update_url, headers=headers, allow_redirects=True)
        try:
            self.json = self.response.json()
        except ValueError:
            self.json = {"raw_text": self.response.text.strip()}

        return self.response

    def check_meme_not_exist(self, meme_id, headers=None):
        headers = headers or self.headers
        response = requests.get(f"{self.url}/meme/{meme_id}", headers=headers)
        assert response.status_code == 404, \
            f"Meme still exists after deletion, got {response.status_code}. Response: {response.text}"
