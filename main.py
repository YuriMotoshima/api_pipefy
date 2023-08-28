from os import environ
from api_pipefy.api.pipefy import Pipefy
from dotenv import load_dotenv
load_dotenv('./.env')
from tests import Resp, VariablesPipefy

schema = {"_query":'''{ me { id }} }'''}
variable_pipefy = VariablesPipefy()
pipefy = Pipefy(token=environ.get("TOKEN_TEST"), host=environ.get("HOST_TEST"))
check_variables = pipefy.func_pattern_query("str",1,"str")
response = pipefy.cards(pipe_id=variable_pipefy.pipe_id)
r = Resp()
print()

t = lambda item, typing: True if type(item) != typing else False


