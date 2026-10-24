import allure
import requests

from endpoints.endpoint import Endpoint


class GetMeme(Endpoint):
    @allure.step('Получение всех существующих мемов')
    def get_all(self):
        self.response = requests.get(f'{self.url}/meme', headers=self.headers)
        match self.response.status_code:
            case 200:
                print(f'Успешное получение всех записей')
                self.response_json = self.response.json()
            case 401:
                print(f'Ошибка авторизации при получении записей: {self.response.status_code}')
                print(f'Ответ: {self.response.text}')
                return None
            case _:
                print(f'Ошибка получения всех записей: статус {self.response.status_code}')
                print(f'Ответ: {self.response.text}')

                self.response.raise_for_status()


    @allure.step('Получение мема по id')
    def get_by_id(self, meme_id):
        self.response = requests.get(f'{self.url}/meme/{meme_id}', headers=self.headers)

        match self.response.status_code:
            case 200:
                print(f'Успешно найдена запись с id={meme_id}')
                self.response_json = self.response.json()
            case 401:
                print(f'Ошибка авторизации при поиске записи: {self.response.status_code}')
                print(f'Ответ: {self.response.text}')
                return None
            case 404:
                print(f'404. Записи с указанными id={meme_id} не существует. {self.response.text}')
            case _:
                print(f'Ошибка получения записи по id={meme_id}: статус {self.response.status_code}')
                print(f'Ответ: {self.response.text}')

                self.response.raise_for_status()

    def assert_meme_id(self, meme_id):
        assert self.response_json['id'] == meme_id