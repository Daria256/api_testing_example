import requests

from endpoints.endpoint import Endpoint


class ReadMeme(Endpoint):
    def read_all_memes(self, headers=None):
        headers = headers or self.headers
        update_url = f"{self.url}/meme"
        session = requests.Session()
        self.response = session.get(update_url, headers=headers, allow_redirects=True)
        try:
            self.json = self.response.json()
        except ValueError:
            self.json = {"raw_text": self.response.text.strip()}

        return self.response
