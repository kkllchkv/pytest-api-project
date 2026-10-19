def test_delete_meme(api_client, meme_id_setup):
    user = 'Kirill'
    meme_id = meme_id_setup(user, cleanup=False)
    client = api_client(user)

    get_meme = client.get_meme_client
    delete_meme = api_client(user).delete_meme_client

    delete_meme.delete(meme_id=meme_id)

    delete_meme.assert_status_200()
    delete_meme.assert_response_not_null()

    get_meme.get_by_id(meme_id=meme_id)
    get_meme.assert_status_404()
