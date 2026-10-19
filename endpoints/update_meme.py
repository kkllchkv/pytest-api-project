import allure
import requests

from endpoints.endpoint import Endpoint


class UpdateMeme(Endpoint):
    @allure.step('Обновление мема')
    def update(self, meme_id, body):
        self.response = requests.put(f'{self.url}/meme/{meme_id}', json=body, headers=self.headers)
        if self.response.status_code != 200:
            print(f'Ошибка обновления записи id={meme_id}: статус {self.response.status_code}')
            print(f'Тело запроса: {body}')
            print(f'Ответ: {self.response.text}')

            self.response.raise_for_status()

        self.response_json = self.response.json()
