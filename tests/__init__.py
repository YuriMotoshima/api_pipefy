# pip install pytest, tox, coverage
# tox -e py310 -- --cov-report xml --cov=.
# ------------------------
# pytest tests/ -v --cov=nova_api
from os import environ
from requests.models import Response
from dotenv import load_dotenv
load_dotenv('./.env')

class Resp(Response):
    def __init__(self, _content:str=None,status_code:int=200) -> None:
        super().__init__()
        self._content = _content
        self.status_code = status_code
        self.headers = {"Content-Type": "application/text", "Authorization": "Token 123"}
        self.url = "http://localhost/main"

class VariablesPipefy():
    __message_env_not_found = "Check your .env, not found variable."
    def __init__(self) -> None:
        self.token = environ.get("TOKEN_TEST") if environ.get("TOKEN_TEST") else ValueError(self.__message_env_not_found)
        self.host_test = environ.get("HOST_TEST") if environ.get("HOST_TEST") else ValueError(self.__message_env_not_found)
        self.organization_id = int(environ.get("ORGANIZATION_ID")) if environ.get("ORGANIZATION_ID") else ValueError(self.__message_env_not_found)
        self.pipe_id = int(environ.get("PIPE_ID")) if environ.get("PIPE_ID") else ValueError(self.__message_env_not_found)
        self.phase_id = int(environ.get("PHASE_ID")) if environ.get("PHASE_ID") else ValueError(self.__message_env_not_found)
        self.generic_valid_response_fields = '''{ id }'''
        self.generic_wrong_response_fields = '''{ }'''
    
