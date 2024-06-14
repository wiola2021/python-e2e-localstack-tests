import requests

from api.data.register import RegisterRequestDto
from api.base_api import BaseAPI

class SignUp(BaseAPI):
    def api_call(self, user: RegisterRequestDto):
        user_data = user.to_dict()
        headers = {'Content-Type': 'application/json'}
        response = self.make_request("POST", "users/signup", json=user_data, headers=headers)
        return response



