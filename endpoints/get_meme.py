import allure
import requests

from endpoints.endpoint import Endpoint


class GetMeme(Endpoint):
    @allure.step('Получение всех существующих мемов')
    def get_all(self):
        self.response = requests.get(f'{self.url}/meme', headers=self.headers)
        print(self.headers)
        if self.response.status_code != 200:
            print(f'Ошибка получения всех записей: статус {self.response.status_code}')
            print(f'Ответ: {self.response.text}')
        self.response_json = self.response.json()

    @allure.step('Получение мема по id')
    def get_by_id(self, meme_id):
        self.response = requests.get(f'{self.url}/meme/{meme_id}', headers=self.headers)

        match self.response.status_code:
            case 404:
                print(f'404. Не смог найти запись с указанным id. {self.response.text}')
            case 200:
                print(f'Успешно найдена запись с id={meme_id}')
                self.response_json = self.response.json()
            case _:
                print(f'Ошибка получения записи по id={meme_id}: статус {self.response.status_code}')
                print(f'Ответ: {self.response.text}')

                self.response.raise_for_status()


