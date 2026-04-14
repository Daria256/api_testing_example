import requests

from endpoints.endpoint import Endpoint


class CreateToken(Endpoint):
    def create_token(self, authorize, body, headers=None):
        headers = headers or self.headers
        update_url = f"{self.url}/authorize"
        self.response = requests.post(update_url, json=body, headers=headers)
        self.json = self.response.json()
        return self.response

    def check_token_is_exist(self):
        if self.json and "token" in self.json:
            print(f"Token: {self.json['token']} is existing")
        else:
            print("Token is still pending")

    def check_user_is_correct(self, expected_name):
        assert self.json is not None, "JSON has not been received yet"
        if "user" in self.json:
            actual_name = self.json["user"]
            assert (
                actual_name == expected_name
            ), f" We are expecting {expected_name}, but we have received {actual_name}"
        else:
            assert "token" in self.json, "There is no token"

    def check_token_with_empty_name(self, name):
        body = {"name": name}
        self.create_token("authorize", body)
        assert (
            self.response.status_code == 400
        ), f"Expected 400, because we have sent empty value in name, but we received {self.response.status_code}"
