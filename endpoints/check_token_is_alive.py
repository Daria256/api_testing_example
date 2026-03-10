import requests

from endpoints.endpoint import Endpoint


class CheckToken(Endpoint):
    def check_token_is_alive(self, token, headers=None):
        headers = headers or self.headers
        update_url = f"{self.url}/authorize/{token}"
        self.response = requests.get(update_url, headers=headers)
        try:
            self.json = self.response.json()
        except ValueError:
            self.json = {"raw_text": self.response.text.strip()}

        return self.response
