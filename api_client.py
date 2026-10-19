from endpoints.create_meme import CreateMeme
from endpoints.delete_meme import DeleteMeme
from endpoints.get_meme import GetMeme
from endpoints.authorization import Authorization
from endpoints.token_manager import TokenManager
from endpoints.update_meme import UpdateMeme


class ApiClient:
    def __init__(self, auth_user: None | str):
        self.auth_user = auth_user
        self.authorization = Authorization()
        self.token_manager = TokenManager(auth_client=self.authorization,auth_user=self.auth_user)

        self.get_meme_client = GetMeme(token_manager=self.token_manager)
        self.create_meme_client = CreateMeme(token_manager=self.token_manager)
        self.update_meme_client = UpdateMeme(token_manager=self.token_manager)
        self.delete_meme_client = DeleteMeme(token_manager=self.token_manager)
