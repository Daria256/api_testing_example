class Endpoint:
    url = 'http://memesapi.course.qa-practice.com'
    response = None
    json = None
    headers = {'Content-type': 'application/json'}

    def __init__(self):
        self.response = None
        self.json = None

    def check_status_code_is_200(self):
        assert self.response.status_code == 200, "Status code is not 200"

    def check_status_code_is_400(self):
        assert self.response.status_code == 400, f"Expected 400, because we have sent without required fields in body, but we received {self.response.status_code}"

    def check_user_is_correct(self, expected_user):
        assert self.json["user"] == expected_user, "User is not correct"

    def check_text_is_correct(self, expected_text):
        assert self.json["text"] == expected_text, "Text is not correct"

    def check_url_is_correct(self, expected_url):
        assert self.json["url"] == expected_url, "Url is not correct"

    def check_tags_is_correct(self, expected_tags):
        assert self.json["tags"] == expected_tags, "Tags are not correct"
