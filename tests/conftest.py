# flake8: noqa: E402
import sys
import os
import pytest
import random

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from endpoints.create_token import CreateToken
from endpoints.create_meme import CreateMeme
from endpoints.check_token_is_alive import CheckToken
from endpoints.read_all_memes import ReadMeme
from endpoints.read_meme import ReadCreatedMeme
from endpoints.update_meme import UpdateMeme
from endpoints.delete_meme import DeleteMeme


@pytest.fixture(scope="session")
def create_token_endpoint():
    return CreateToken()


@pytest.fixture()
def check_token_is_alive_endpoint():
    return CheckToken()


@pytest.fixture()
def create_meme_endpoint():
    return CreateMeme()


@pytest.fixture()
def read_all_memes_endpoint():
    return ReadMeme()


@pytest.fixture()
def read_meme_endpoint():
    return ReadCreatedMeme()


@pytest.fixture()
def update_meme_endpoint():
    return UpdateMeme()


@pytest.fixture()
def delete_meme_endpoint():
    return DeleteMeme()


@pytest.fixture(scope="session")
def auth_token(create_token_endpoint):
    body = {"name": "dasha_tester"}
    response = create_token_endpoint.create_token("authorize", body)
    assert response.status_code == 200
    token = response.json().get("token")
    assert token, "Token not created"
    create_token_endpoint.check_token_is_exist()

    check_token_endpoint = CheckToken()
    headers = {"Authorization": f"Bearer {token}"}
    if not check_token_endpoint.check_token_is_alive(token, headers=headers):
        print("Token invalid, creating a new one...")
        response = create_token_endpoint.create_token("authorize", body)
        token = response.json().get("token")
        assert token, "Token not created after regeneration"
        print(f"New token created")

    return token


@pytest.fixture()
def authorized_headers(auth_token):
    return {"Authorization": auth_token}


@pytest.fixture()
def meme_id(create_meme_endpoint, authorized_headers, delete_meme_endpoint):
    body = {
        "text": "I always see advertisement everywhere",
        "url": "https://amdg.ru/upload/NewFolder/mem-pro-reklamu.png",
        "tags": ["courses", "programming", "doctor"],
        "info": {"colors": ["blue", "brown"], "objects": ["picture", "text"]},
    }
    response = create_meme_endpoint.create_meme(body=body, headers=authorized_headers)
    response_data = response.json()

    meme_id = response_data.get("_id") or response_data.get("id")
    print(meme_id)
    if not meme_id:
        raise ValueError(f"Cannot get object ID from response: {response_data}")

    yield meme_id
    delete_meme_endpoint.delete_meme(meme_id)


@pytest.fixture()
def not_existing_id():
    return random.randint(10_000, 1_000_000)
