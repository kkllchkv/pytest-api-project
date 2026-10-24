def test_delete_meme(api_client, meme_id_setup):
    user = 'Kirill'
    meme_id = meme_id_setup(user, cleanup=False)
    client = api_client(user)

    get_meme = client.get_meme_client
    delete_meme = client.delete_meme_client

    delete_meme.delete(meme_id=meme_id)

    delete_meme.assert_status_200()
    delete_meme.assert_response_not_null()

    get_meme.get_by_id(meme_id=meme_id)
    get_meme.assert_status_404()

def test_delete_meme_not_auth(api_client_no_auth, meme_id_setup):
    user = 'Kirill'
    meme_id = meme_id_setup(user, cleanup=False)

    delete_meme = api_client_no_auth.delete_meme_client
    delete_meme.delete(meme_id=meme_id)

    delete_meme.assert_status_401()
    delete_meme.assert_response_not_null()
    delete_meme.assert_text_response('Unauthorized')

def test_delete_not_existing_meme(api_client):
    user = 'Kirill'
    meme_id = 9999999
    client = api_client(user)
    delete_meme = client.delete_meme_client

    delete_meme.delete(meme_id=meme_id)

    delete_meme.assert_status_404()
    delete_meme.assert_text_response('Not Found')

def test_delete_other_user_meme(api_client):
    user = 'Kirill'
    meme_id = 3
    client = api_client(user)
    delete_meme = client.delete_meme_client

    delete_meme.delete(meme_id=meme_id)

    delete_meme.assert_status_403()
    delete_meme.assert_text_response('Forbidden')
