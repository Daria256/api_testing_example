import pytest

TEST_DATA = [
    {"text": "I always see advertisement everywhere", "url": "https://amdg.ru/upload/NewFolder/mem-pro-reklamu.png",
     "tags": ["courses", "programming", "doctor"],
     "info": {"colors": ["blue", "brown"],
              "objects": ["picture", "text"]}
     }
]

TEST_CREATE_MEME_INVALID_DATA = [
    {"text": "I always see advertisement everywhere", "url": "https://amdg.ru/upload/NewFolder/mem-pro-reklamu.png",
     "info": {"colors": ["blue", "brown"],
              "objects": ["picture", "text"]}
     },
    {"text": "I always see advertisement everywhere", "url": "https://amdg.ru/upload/NewFolder/mem-pro-reklamu.png",
     "tags": None,
     "info": {"colors": ["blue", "brown"],
              "objects": ["picture", "text"]}
     },
    {"url": "https://amdg.ru/upload/NewFolder/mem-pro-reklamu.png",
     "tags": ["courses", "programming", "doctor"],
     "info": {"colors": ["blue", "brown"],
              "objects": ["picture", "text"]}
     },
    {"text": "I always see advertisement everywhere",
     "info": {"colors": ["blue", "brown"],
              "objects": ["picture", "text"]}
     },
    {"text": None,
     "url": "https://amdg.ru/upload/NewFolder/mem-pro-reklamu.png",
     "tags": ["courses", "programming", "doctor"]
     }
]

TEST_UPDATE_MEME_INVALID_DATA = [
    {
        "url": "https://amdg.ru/upload/NewFolder/mem-pro-reklamu.png",
        "tags": ["new tag1", "new tag2", "new tag3"],
        "info": {"colors": ["white", "black"],
                 "objects": ["smile", "joke"]}

    },
    {"text": "I always see advertisement everywhere- updated",
     "tags": ["new tag1", "new tag2", "new tag3"],
     "info": {"colors": ["white", "black"],
              "objects": ["smile", "joke"]}

     },
    {"text": "I always see advertisement everywhere- updated",
     "url": "https://amdg.ru/upload/NewFolder/mem-pro-reklamu.png",
     "info": {"colors": ["white", "black"],
              "objects": ["smile", "joke"]}

     }

]


@pytest.mark.parametrize("name", ["dasha_tester"])
def test_create_token(create_token_endpoint, name):
    body = {"name": name}
    create_token_endpoint.create_token("authorize", body)
    create_token_endpoint.check_status_code_is_200()
    create_token_endpoint.check_user_is_correct(body["name"])
    create_token_endpoint.print_token()


@pytest.mark.parametrize("name", [""])
def test_create_token_with_invalid_name(create_token_endpoint, name):
    body = {"name": ""}
    create_token_endpoint.check_token_with_empty_name(body["name"])


def test_check_token_is_alive(check_token_is_alive_endpoint, auth_token):
    check_token_is_alive_endpoint.check_token_is_alive(auth_token)
    check_token_is_alive_endpoint.check_status_code_is_200()


def test_read_all_memes(read_all_memes_endpoint, authorized_headers):
    read_all_memes_endpoint.read_all_memes(headers=authorized_headers)
    read_all_memes_endpoint.check_status_code_is_200()



@pytest.mark.parametrize("data", TEST_DATA)
def test_create_meme(create_meme_endpoint, data, authorized_headers):
    create_meme_endpoint.create_meme(body=data, headers=authorized_headers)
    create_meme_endpoint.check_status_code_is_200()
    create_meme_endpoint.check_text_is_correct(data["text"])
    create_meme_endpoint.check_url_is_correct(data["url"])
    create_meme_endpoint.check_tags_is_correct(data["tags"])


@pytest.mark.parametrize("data", TEST_CREATE_MEME_INVALID_DATA)
def test_create_meme_without_required_fields(create_meme_endpoint, data, authorized_headers):
    create_meme_endpoint.create_meme(body=data, headers=authorized_headers)
    create_meme_endpoint.check_status_code_is_400()


def test_read_created_meme(read_created_meme_endpoint, meme_id, authorized_headers):
    read_created_meme_endpoint.read_created_meme(meme_id, headers=authorized_headers)
    read_created_meme_endpoint.check_status_code_is_200()


def test_update_meme(update_meme_endpoint, meme_id, authorized_headers):
    body = {
        "id": meme_id,
        "text": "I always see advertisement everywhere- updated",
        "url": "https://amdg.ru/upload/NewFolder/mem-pro-reklamu.png",
        "tags": ["new tag1", "new tag2", "new tag3"],
        "info": {"colors": ["white", "black"],
                 "objects": ["smile", "joke"]}
    }

    update_meme_endpoint.update_meme(meme_id, body=body, headers=authorized_headers)
    update_meme_endpoint.check_status_code_is_200()


@pytest.mark.parametrize("data", TEST_UPDATE_MEME_INVALID_DATA)
def test_update_meme_without_required_fields(update_meme_endpoint, meme_id, data, authorized_headers):
    update_meme_endpoint.update_meme(meme_id, body=data, headers=authorized_headers)
    update_meme_endpoint.check_status_code_is_400()


def test_delete_meme(delete_meme_endpoint, read_created_meme_endpoint, meme_id, authorized_headers):
    delete_meme_endpoint.delete_meme(meme_id, headers=authorized_headers)
    delete_meme_endpoint.check_status_code_is_200()
    read_created_meme_endpoint.check_meme_not_exist(meme_id, headers=authorized_headers)
