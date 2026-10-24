import allure
import requests

from endpoints.endpoint import Endpoint


class CreateMeme(Endpoint):
    @allure.step('Создание нового мема')
    def create(self, body):
        self.response = requests.post(f'{self.url}/meme', json=body, headers=self.headers)

        match self.response.status_code:
            case 200:
                self.response_json = self.response.json()
                print(f'Успешное создание мема с id={self.response_json["id"]}')
            case 400:
                print(f'Ошибка валидации при создании записи: статус {self.response.status_code}')
                print(f'Ответ: {self.response.text}')
                return None
            case 401:
                print(f'Ошибка авторизации при создании записи: {self.response.status_code}')
                print(f'Ответ: {self.response.text}')
                return None
            case _:
                print(f'Ошибка создания записи со статусом {self.response.status_code}')
                print(f'Ответ: {self.response.text}')

                self.response.raise_for_status()

        return self.response_json['id']
