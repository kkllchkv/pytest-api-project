import requests

from endpoints.endpoint import Endpoint


class Authorization(Endpoint):
    """методы авторизации"""
    def authorize(self, auth_body):
        self.response = requests.post(f'{self.url}/authorize', json=auth_body)

        match self.response.status_code:
            case 200:
                print(f'Успешное создание токена авторизации')
                self.response_json = self.response.json()
                self.auth_token = self.response_json['token']
            case 400:
                print(f'Ошибка валидации при создании токена авторизации: {self.response.status_code}')
                print(f'Ответ: {self.response.text}')
                return None
            case _:
                print(f'Ошибка авторизации')
                print(f'Ответ: {self.response.text}')
                self.response.raise_for_status()

        return self.response_json['token']

    def get_token(self, token):
        # response содержит текст с типом Content-Type = text/html;
        # например, Token is alive. Username is Kirill.
        # преобразовывать в json нельзя
        self.response = requests.get(f'{self.url}/authorize/{token}')

        match self.response.status_code:
            case 200:
                print(f'Успешное получение токена авторизации')
                self.auth_token = self.response_json['token']
            case 404:
                print(f'Ошибка получения токена авторизации - заданного токена не существует: {self.response.status_code}')
                print(f'Ответ: {self.response.text}')
            case _:
                print(f'Ошибка получения токена авторизации: {self.response.status_code}')
                print(f'Ответ: {self.response.text}')

                self.response.raise_for_status()

        return self.response.text

    def assert_none_token(self):
        assert self.auth_token is None