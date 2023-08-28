from os import environ
from api_pipefy.libs.session import Sessions
from tests import Resp
import pytest

@pytest.fixture
def variable_host():
    return environ.get("HOST_TEST")

@pytest.fixture
def variable_token():
    return environ.get("TOKEN_TEST")

@pytest.fixture
def variable_headers_default(variable_token):
    return {
        "User-Agent": "python-requests/2.28.2", 
        "Accept-Encoding": "gzip, deflate", 
        "Accept": "*/*", 
        "Connection": "keep-alive", 
        "accept": "application/json", 
        "Content-Type": "application/json", 
        "Authorization": f"Bearer {variable_token}"}

@pytest.fixture
def variable_headers_change():
    return {"Content-Type": "application/text", "Authorization": "Token 123"}

@pytest.fixture
def session_fixture(variable_token, variable_host):
    return Sessions(variable_token, variable_host)

@pytest.fixture
def variable_schema_sucess():
    return {"query":'''{ me { id } }'''}

@pytest.fixture
def variable_schema_error_500():
    return {"_query":'''{ me { id } }'''}

@pytest.fixture
def variable_response_none_content():
    return Resp()

@pytest.fixture
def variable_response_error_content():
    return Resp(_content=b'{"error":{"error_description": "Nothing"}}')

@pytest.fixture
def variable_response_errors_content():
    return Resp(_content=b'{"errors":[{"message":"Any wrong"}]}')

@pytest.fixture
def variable_response_success_content():
    return Resp(_content=b'{"data":{"pipe":"123"}}')

