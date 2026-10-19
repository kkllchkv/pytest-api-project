from datetime import datetime


class TokenManager:
    """
    класс руководит логикой использования токена
    при отсутствии токена - создает новый
    при наличии токена - проверяет его актуальность и актуализирует в случае необходимости
    возвращает хэдер авторизации с заполненным токеном
    """
    def __init__(self, auth_client, auth_user):
        self.auth_token = None
        self.auth_body = None
        self.auth_client = auth_client
        self.auth_user = auth_user
        self.token_timespan = None

    def get_auth_headers(self):
        self.auth_body = {'name': self.auth_user}

        if not self.auth_token:
            print('Получение новый токен')
            print(self.auth_body)
            self.auth_token = self.auth_client.authorize(self.auth_body)
            self.token_timespan = datetime.now()
            return {'Authorization': self.auth_token}

        elif self.auth_token and (datetime.now() - self.token_timespan).seconds > 300:
            print('С момента создания токена авторизации прошло > 5 минут. '
                  'Проверка актуальности')
            get_token_response = self.auth_client.get_token(self.auth_token)

            if "is alive" not in get_token_response:
                print('Обновление протухшего токена')
                self.auth_token = self.auth_client.authorize(self.auth_body)
                return {'Authorization': self.auth_token}

        return {'Authorization': self.auth_token}