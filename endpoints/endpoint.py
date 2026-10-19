class Endpoint:
    def __init__(self, token_manager=None):
        self.url = 'http://memesapi.course.qa-practice.com/'
        self.response = None
        self.response_json = None
        self.headers = {}
        self.auth_token = None
        self.auth_user = None

        self.token_manager = token_manager

        if token_manager and not self.auth_token:
            auth_headers = self.token_manager.get_auth_headers()
            self.auth_token = auth_headers['Authorization']
            self.headers.update(auth_headers)

    def assert_status_200(self):
        assert self.response.status_code == 200, 'Статус ответа != 200'

    def assert_status_400(self):
        assert self.response.status_code == 400, 'Статус ответа != 400'

    def assert_status_404(self):
        assert self.response.status_code == 404, 'Статус ответа != 404'

    def assert_response_not_null(self):
        # для POST / PUT / GET методов, у которых в теле ответа - json
        if self.response_json:
            assert len(self.response_json) > 0, 'В ответе отсутсвтуют структуры данных'
        # для DELETE метода или проверки ошибок, у которого в теле ответа - text
        elif self.response.text:
            assert len(self.response.text) > 0, 'Тело ответа - пустое'
        else:
            raise AssertionError('Не получилось подобрать подходящий формат тела ответа')

    def assert_param(self, body: dict, param):
        assert self.response_json[param] == body[param], f'Параметр {param} не обновлен'

    def assert_all_params(self, body: dict, need_id=False):
        required_data = self.response_json.copy()

        if not need_id:
            required_data.pop('id', None)
        else:
            required_data['id'] = int(required_data['id'])

        required_data.pop('updated_by', None)

        assert required_data == body, ('Параметры из тела запроса не соответствуют данным из ответа',
                                       f'Ожидаемые данные: {required_data}',
                                       f'Подаваемые данные: {body}')

    def assert_nested_param(self, body: dict, path_to_param: str):
        """
        проверка вложенных значений в ответе метода
        структура ответа:
        {"id": "", "info": { "colors": [],"objects": [] },"tags": [],"text": "", "updated_by": "", "url": ""}
        """

        params = path_to_param.split('.')
        nested_value_response = self.response_json.copy()
        nested_value_request = body.copy()

        for param in params:
            nested_value_response = nested_value_response[param]
            nested_value_request = nested_value_request[param]

        print(nested_value_response)
        print(nested_value_request)
        assert nested_value_response == nested_value_request, f'Параметр {path_to_param} не обновлен'

    def assert_has_required_keys(self):
        """проверка наличия обязательных ключей в ответе метода"""
        required_keys = {"id", "url", "text", "tags", "info", "updated_by"}

        # условие для структуры {"data": [{}, {}]} - например, ответ get_all метода
        if self.response_json.get("data"):
            for data in self.response_json["data"]:
                # для каждого блока убеждаемся, что существует id + параметры, обязательные при создании
                shared_keys = required_keys.intersection(data)
                assert required_keys == shared_keys, (f'Для мема с id={data["id"]} присутсвуют '
                                                      f'не все обязательные параметры')

        # условие для структуры обычного словаря {"":.., "":..} - ответ методов get_by_id, create_meme, update_meme
        else:
            shared_keys = required_keys.intersection(self.response_json)
            assert required_keys == shared_keys, (f'Для мема с id={self.response_json["id"]} присутсвуют '
                                                  f'не все обязательные параметры')

    def test_body_constructor(self, **kwargs):
        default_body = {
            "info": {
                "colors": [
                    "black",
                    "white"
                ],
                "objects": [
                    "picture",
                    "text"
                ]
            },
            "tags": [
                "QA"
            ],
            "text": "qa test meme",
            "url": "https://images.meme-arsenal.com/82498a472778d42ccbe790816f5575e6.jpg"
        }

        if kwargs:
            for key, new_value in kwargs.items():
                if default_body.get(key) and type(kwargs[key]) != type(default_body[key]):
                    # сравнение типов данных для параметров дефолтного тела запроса
                    continue

                default_body[key] = new_value

        return default_body
