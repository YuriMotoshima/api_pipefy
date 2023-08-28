from tests import Resp, VariablesPipefy
import tests.test_pipefy.conftest

class TestInitResp():
    __headers = {"Content-Type": "application/text", "Authorization": "Token 123"}
    __url = "http://localhost/main"
    
    def test_class_resp_is_instance(self):
        resp = Resp()
        assert isinstance(resp, object)
    
    def test_class_resp_dont_send_content_if_igual_none(self):
        resp = Resp()
        assert resp._content == None

    def test_class_resp_send_content_if_different_none(self):
        resp = Resp(_content="teste")
        assert resp._content != None

    def test_class_resp_content_if_igual_sended(self):
        resp = Resp(_content="teste")
        assert resp._content == "teste"
    
    def test_class_resp_dont_send_status_code_if_igual_200(self):
        resp = Resp()
        assert resp.status_code == 200

    def test_class_resp_send_status_code_if_different_none(self):
        resp = Resp(status_code=200)
        assert resp.status_code != None

    def test_class_resp_status_code_if_igual_sended(self):
        resp = Resp(status_code=200)
        assert resp.status_code == 200

    def test_class_resp_header_is_correct(self):
        resp = Resp()
        assert resp.headers == self.__headers

    def test_class_resp_url_is_correct(self):
        resp = Resp()
        assert resp.url == self.__url
    

class TestInitVariablesPipefy():
    
    def test_class_variable_pipefy_is_instance(self):
        variable = VariablesPipefy()
        assert isinstance(variable, object)
    
    def test_class_variable_pipefy_token_not_is_none(self):
        variable = VariablesPipefy()
        assert variable.token != None

    def test_class_variable_pipefy_token_is_srt(self):
        variable = VariablesPipefy()
        assert type(variable.token) == str
    
    def test_class_variable_pipefy_organization_id_not_is_none(self):
        variable = VariablesPipefy()
        assert variable.organization_id != None

    def test_class_variable_pipefy_organization_id_is_srt(self):
        variable = VariablesPipefy()
        assert type(variable.organization_id) == int
    
    def test_class_variable_pipefy_pipe_id_not_is_none(self):
        variable = VariablesPipefy()
        assert variable.pipe_id != None

    def test_class_variable_pipefy_pipe_id_is_srt(self):
        variable = VariablesPipefy()
        assert type(variable.pipe_id) == int

    def test_class_variable_pipefy_host_test_not_is_none(self):
        variable = VariablesPipefy()
        assert variable.host_test != None

    def test_class_variable_pipefy_host_test_is_srt(self):
        variable = VariablesPipefy()
        assert type(variable.host_test) == str

    def test_class_variable_pipefy_generic_valid_response_fields_not_is_none(self):
        variable = VariablesPipefy()
        assert variable.generic_valid_response_fields != None

    def test_class_variable_pipefy_generic_valid_response_fields_is_srt(self):
        variable = VariablesPipefy()
        assert type(variable.generic_valid_response_fields) == str

    def test_class_variable_pipefy_generic_valid_response_fields(self):
        variable = VariablesPipefy()
        assert variable.generic_valid_response_fields == '''{ id }'''

    def test_class_variable_pipefy_generic_wrong_response_fields_not_is_none(self):
        variable = VariablesPipefy()
        assert variable.generic_wrong_response_fields != None

    def test_class_variable_pipefy_generic_wrong_response_fields_is_srt(self):
        variable = VariablesPipefy()
        assert type(variable.generic_wrong_response_fields) == str

    def test_class_variable_pipefy_generic_wrong_response_fields(self):
        variable = VariablesPipefy()
        assert variable.generic_wrong_response_fields == '''{ }'''

