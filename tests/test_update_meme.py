def test_update_meme(api_client, meme_id_setup):
    user = 'Kirill'
    meme_id = meme_id_setup(user)
    client = api_client(user)
    get_meme = client.get_meme_client
    update_meme = client.update_meme_client

    # параметр id является обязательным для update метода
    body = update_meme.test_body_constructor(
        id=meme_id,text="test update method", tags=["QA", "test update"]
    )
    update_meme.update(body=body, meme_id=meme_id)

    update_meme.assert_status_200()
    update_meme.assert_response_not_null()
    update_meme.assert_has_required_keys()
    update_meme.assert_all_params(body=body, need_id=True)

    get_meme.get_by_id(meme_id)
    get_meme.assert_status_200()
    get_meme.assert_all_params(body=body, need_id=True)


def test_update_meme_not_auth(api_client_no_auth, meme_id_setup):
    user = 'Kirill'
    meme_id = meme_id_setup(user)

    update_meme = api_client_no_auth.update_meme_client

    # параметр id является обязательным для update метода
    body = update_meme.test_body_constructor()
    update_meme.update(body=body, meme_id=meme_id)

    update_meme.assert_status_401()
    update_meme.assert_response_not_null()
    update_meme.assert_text_response('Unauthorized')

def test_update_other_user_meme(api_client, meme_id_setup):
    user = 'Kirill'
    client = api_client(user)
    update_meme = client.update_meme_client

    body = update_meme.test_body_constructor()
    update_meme.update(body=body, meme_id=1)

    update_meme.assert_status_403()
    update_meme.assert_response_not_null()
    update_meme.assert_text_response('Forbidden')