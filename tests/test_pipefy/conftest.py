
from api_pipefy.api.pipefy import Pipefy
from tests import Resp, VariablesPipefy
import pytest

@pytest.fixture
def variable_pipefy():
    return VariablesPipefy()

@pytest.fixture(scope="function")
def collection_pipefy_fixture(variable_pipefy):
    return Pipefy(variable_pipefy.token, variable_pipefy.host_test)

@pytest.fixture
def variable_schema_sucess():
    return {"query":'''{ me { id } }'''}

@pytest.fixture
def variable_schema_error_500():
    return {"_query":'''{ me { id } }'''}

@pytest.fixture
def variable_response_none_content():
    return Resp()