import requests


class Endpoint:
    url = "http://memesapi.course.qa-practice.com"
    response = None
    json = None
    headers = {"Content-type": "application/json"}

    def __init__(self):
        self.response = None
        self.json = None

    def check_status_code_is_200(self):
        assert self.response.status_code == 200, "Status code is not 200"

    def check_status_code_is_400(self):
        assert (
            self.response.status_code == 400
        ), f"Expected 400, because we have sent without required fields in body, but we received {self.response.status_code}"

    def check_user_is_correct(self, expected_user):
        assert self.json["user"] == expected_user, "User is not correct"

    def check_text_is_correct(self, expected_text):
        assert self.json["text"] == expected_text, "Text is not correct"

    def check_url_is_correct(self, expected_url):
        assert self.json["url"] == expected_url, "Url is not correct"

    def check_tags_is_correct(self, expected_tags):
        assert self.json["tags"] == expected_tags, "Tags are not correct"

    def check_info_is_correct(self, expected_info):
        assert self.json["info"] == expected_info, "Info is not correct"

    def check_id_is_correct(self, meme_id):
        assert str(self.json.get("id")) == str(
            meme_id
        ), f"Id is not correct: expected {meme_id}, got {self.json.get('id')}"

    def read_meme(self, meme_id, headers=None):
        headers = headers or self.headers
        update_url = f"{self.url}/meme/{meme_id}"
        self.response = requests.get(update_url, headers=headers, allow_redirects=True)
        try:
            self.json = self.response.json()
        except ValueError:
            self.json = {"raw_text": self.response.text.strip()}

        return self.response

    def check_status_code_is_404(self):
        assert (
            self.response.status_code == 404
        ), f"Expected 404, because we have sent invalid meme_id, but we received {self.response.status_code}"

    def check_status_code_is_401(self):
        assert (
            self.response.status_code == 401
        ), f"Expected 401, because we have sent empty token for unauthorized user, but we received {self.response.status_code}"
