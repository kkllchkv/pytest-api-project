import allure
import requests

from endpoints.endpoint import Endpoint


class DeleteMeme(Endpoint):
    @allure.step('Удаление мема')
    def delete(self, meme_id):
        self.response = requests.delete(f'{self.url}/meme/{meme_id}', headers=self.headers)
        print(f'Успешное удаление юзера {meme_id}')

        if self.response.status_code != 200:
            print(f'Ошибка удаления записи {meme_id}: статус {self.response.status_code}')
