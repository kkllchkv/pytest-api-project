import allure
import requests

from endpoints.endpoint import Endpoint


class DeleteMeme(Endpoint):
    @allure.step('Удаление мема')
    def delete(self, meme_id):
        self.response = requests.delete(f'{self.url}/meme/{meme_id}', headers=self.headers)

        match self.response.status_code:
            case 200:
                print(f'Успешное удаление записи')
            case 401:
                print(f'Ошибка авторизации при удалении записи: {self.response.status_code}')
                print(f'Ответ: {self.response.text}')
                return None
            case 403:
                print(f'Ошибка доступов при удалении записи: {self.response.status_code}')
                print(f'Ответ: {self.response.text}')
                return None
            case 404:
                print(f'404. Записи с указанными id={meme_id} не существует. {self.response.text}')
                return None
            case _:
                print(f'Ошибка удаления записи {meme_id}: статус {self.response.status_code}')

                self.response.raise_for_status()
