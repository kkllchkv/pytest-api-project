import pytest

from api_client import ApiClient


@pytest.fixture()
def api_client():
    authed_users = {}

    def init_api_client(user):
        if user in authed_users:
            return authed_users[user]
        else:
            client = ApiClient(user)
            client.auth_user = user
            authed_users[user] = client

        return client

    return init_api_client


@pytest.fixture(scope='function')
def meme_id_setup(api_client):
    teardown_data = []

    def get_meme_id(user=None, cleanup=True):
        auth_user = 'test user for setup' if not user else user
        client = api_client(auth_user)
        create_client = client.create_meme_client
        delete_client = client.delete_meme_client
        body = create_client.test_body_constructor(text='test meme for setup')

        print(f'Создаем тестовый мем под тестовым юзером: {user}')
        create_client.create(body)
        meme_id = create_client.response_json['id']

        if cleanup:
            teardown_data.append((delete_client, meme_id))

        return meme_id

    yield get_meme_id

    for delete_client, meme_id in teardown_data:
        delete_client.delete(meme_id)