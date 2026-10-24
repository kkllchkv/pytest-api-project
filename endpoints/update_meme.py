import allure
import requests

from endpoints.endpoint import Endpoint


class UpdateMeme(Endpoint):
    @allure.step('Обновление мема')
    def update(self, meme_id, body):
        self.response = requests.put(f'{self.url}/meme/{meme_id}', json=body, headers=self.headers)

        match self.response.status_code:
            case 200:
                print(f'Успешное создание записи')
                self.response_json = self.response.json()
            case 400:
                print(f'Ошибка валидации при обновлении записи: статус {self.response.status_code}')
                print(f'Ответ: {self.response.text}')
                return None
            case 401:
                print(f'Ошибка авторизации при обновлении записи: {self.response.status_code}')
                print(f'Ответ: {self.response.text}')
                return None
            case 403:
                print(f'Ошибка доступов при обновлении записи: {self.response.status_code}')
                print(f'Ответ: {self.response.text}')
                return None
            case _:
                print(f'Ошибка обновления записи id={meme_id}: статус {self.response.status_code}')
                print(f'Тело запроса: {body}')
                print(f'Ответ: {self.response.text}')

                self.response.raise_for_status()

        self.response_json = self.response.json()
