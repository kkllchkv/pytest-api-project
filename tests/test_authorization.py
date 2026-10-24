def test_authorize(api_client_no_auth):
    auth_body = {'name': 'Kirill'}
    authorize = api_client_no_auth.authorization

    authorize.authorize(auth_body=auth_body)
    authorize.assert_status_200()
    authorize.assert_param(body=auth_body,body_param='name', response_param='user')


def test_get_token(api_client_no_auth):
    auth_body = {'name': 'Kirill'}
    authorize = api_client_no_auth.authorization

    token = authorize.authorize(auth_body=auth_body)
    authorize.get_token(token=token)

    authorize.assert_status_200()
    authorize.assert_response_not_null()


def test_authorize_wrong_user(api_client_no_auth):

    authorize = api_client_no_auth.authorization

    auth_body = {'name': 10}
    authorize.authorize(auth_body=auth_body)

    authorize.assert_status_400()
    authorize.assert_none_token()


def test_get_token_with_wrong_token(api_client_no_auth):
    authorize = api_client_no_auth.authorization
    auth_body = {'name': 'test_user'}

    authorize.authorize(auth_body=auth_body)
    authorize.get_token(token='123')

    authorize.assert_status_404()
    authorize.assert_response_not_null()
    authorize.assert_text_response('Not Found')
