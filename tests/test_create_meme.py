def test_create_meme(api_client):
    user = 'Kirill'
    client = api_client(user)
    get_meme = client.get_meme_client
    create_meme = client.create_meme_client
    delete_meme = client.delete_meme_client

    body = create_meme.test_body_constructor()
    create_meme.create(body=body)

    meme_id = create_meme.response_json['id']

    create_meme.assert_status_200()
    create_meme.assert_response_not_null()
    create_meme.assert_has_required_keys()
    create_meme.assert_all_params(body=body)

    get_meme.get_by_id(meme_id)

    get_meme.assert_status_200()
    get_meme.assert_all_params(body=body)

    delete_meme.delete(meme_id)