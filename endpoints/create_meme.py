import allure
import requests

from endpoints.endpoint import Endpoint


class CreateMeme(Endpoint):
    @allure.step('Создание нового мема')
    def create(self, body):
        self.response = requests.post(f'{self.url}/meme', json=body, headers=self.headers)
        if self.response.status_code != 200:
            print(f'Ошибка создания записи: статус {self.response.status_code}')
            print(f'Ответ: {self.response.text}')

            self.response.raise_for_status()

        self.response_json = self.response.json()
        print(f'Успешное создание мема с id ={self.response_json["id"]}')

