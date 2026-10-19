import requests

from endpoints.endpoint import Endpoint


class Authorization(Endpoint):
    """методы авторизации"""
    def authorize(self, auth_body):
        self.response = requests.post(f'{self.url}/authorize', json=auth_body)
        if self.response.status_code != 200:
            print(f'Ошибка получения токена авторизации: {self.response.status_code}')
            print(f'Ответ: {self.response.text}')

            self.response.raise_for_status()

        self.response_json = self.response.json()

        return self.response_json['token']

    def get_token(self, token):
        # response содержит текст с типом Content-Type = text/html;
        # например, Token is alive. Username is Kirill.
        # преобразовывать в json нельзя
        self.response = requests.get(f'{self.url}/authorize/{token}')
        if self.response.status_code != 200:
            print(f'Ошибка получения токена авторизации: {self.response.status_code}')
            print(f'Ответ: {self.response.text}')

            self.response.raise_for_status()

        return self.response.text
