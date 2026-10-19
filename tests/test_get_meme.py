import allure
import pytest


def test_get_all_memes(api_client):
    user = 'Kirill'
    client = api_client(user)

    get_meme = client.get_meme_client
    get_meme.get_all()

    get_meme.assert_status_200()
    get_meme.assert_response_not_null()
    get_meme.assert_has_required_keys()


def test_get_meme_by_id(api_client, meme_id_setup):
    user = 'Kirill'
    client = api_client(user)
    meme_id = meme_id_setup(user)

    get_meme = client.get_meme_client
    get_meme.get_by_id(meme_id)

    get_meme.assert_status_200()
    get_meme.assert_response_not_null()
    get_meme.assert_has_required_keys()
