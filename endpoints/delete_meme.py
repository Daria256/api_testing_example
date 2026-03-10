import requests

from endpoints.endpoint import Endpoint


class DeleteMeme(Endpoint):

    def delete_meme(self, meme_id, headers=None):
        headers = headers or self.headers
        delete_url = f"{self.url}/meme/{meme_id}"
        self.response = requests.delete(delete_url, headers=headers)
        return self.response
