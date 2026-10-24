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

def test_get_all_memes_unauthorized(api_client_no_auth):
    get_meme = api_client_no_auth.get_meme_client
    get_meme.get_all()

    get_meme.assert_status_401()
    get_meme.assert_response_not_null()
    get_meme.assert_text_response('Unauthorized')

def test_get_meme_by_id(api_client, meme_id_setup):
    user = 'Kirill'
    client = api_client(user)
    meme_id = meme_id_setup(user)

    get_meme = client.get_meme_client
    get_meme.get_by_id(meme_id)

    get_meme.assert_status_200()
    get_meme.assert_response_not_null()
    get_meme.assert_has_required_keys()
    get_meme.assert_meme_id(meme_id=meme_id)

def test_get_meme_by_wrong_id(api_client):
    user = 'Kirill'
    client = api_client(user)
    meme_id = 999999999

    get_meme = client.get_meme_client
    get_meme.get_by_id(meme_id)

    get_meme.assert_status_404()
    get_meme.assert_response_not_null()
    get_meme.assert_text_response('Not Found')

def test_get_meme_unauthorized(api_client_no_auth, meme_id_setup):
    user = 'Kirill'
    meme_id = meme_id_setup(user)

    get_meme = api_client_no_auth.get_meme_client
    get_meme.get_by_id(meme_id)

    get_meme.assert_status_401()
    get_meme.assert_response_not_null()
    get_meme.assert_text_response('Unauthorized')