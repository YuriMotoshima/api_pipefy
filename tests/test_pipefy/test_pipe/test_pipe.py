import pytest

class TestPipefyPipe():
    __message_errors_variable = r"Check passed variables, something is wrong."
    __message_variable_not_send = r"required positional argument"
    __message_wrong_query = r"Errors, something wrong in your query. Check on logging error."
    __check_pattern_response_id = "{ id }"

    # PIPE
    def test_pipe_send_new_valid_response_fields_and_return_dict(self, collection_pipefy_fixture,variable_pipefy):
        pipefy=collection_pipefy_fixture
        response = pipefy.pipe(pipe_id=variable_pipefy.pipe_id, response_fields=variable_pipefy.generic_valid_response_fields)
        assert type(response) == dict

    def test_pipe_verify_type_return_dict(self, collection_pipefy_fixture,variable_pipefy):
        pipefy=collection_pipefy_fixture
        response = pipefy.pipe(pipe_id=variable_pipefy.pipe_id)
        assert type(response) == dict

    def test_pipe_dont_send_param_require_return_typeerror(self, collection_pipefy_fixture):
        pipefy=collection_pipefy_fixture
        with pytest.raises(TypeError, match=self.__message_variable_not_send):
            pipefy.pipe()

    def test_pipe_check_if_name_query_into_return_data(self, collection_pipefy_fixture,variable_pipefy):
        pipefy=collection_pipefy_fixture
        response = pipefy.pipe(pipe_id=variable_pipefy.pipe_id)
        assert "pipe" in response
    
    def test_pipe_send_wrong_query_and_return_valueerror(self, collection_pipefy_fixture,variable_pipefy):
        pipefy=collection_pipefy_fixture
        with pytest.raises(ValueError, match=self.__message_wrong_query):
            pipefy.pipe(pipe_id=variable_pipefy.pipe_id, response_fields=variable_pipefy.generic_wrong_response_fields)

    def test_pipe_send_wrong_one_type_variable_not_required_and_return_valueerror(self, collection_pipefy_fixture):
        pipefy=collection_pipefy_fixture
        with pytest.raises(ValueError, match=self.__message_errors_variable):
            pipefy.pipe(pipe_id=123, response_fields=123)

    def test_pipe_send_wrong_more_one_type_variable_and_return_valueerror(self, collection_pipefy_fixture):
        pipefy=collection_pipefy_fixture
        with pytest.raises(ValueError, match=self.__message_errors_variable):
            pipefy.pipe(pipe_id="123", response_fields=123)

    def test_pipe_send_wrong_one_type_variable_required_and_return_valueerror(self, collection_pipefy_fixture):
        pipefy=collection_pipefy_fixture
        with pytest.raises(ValueError, match=self.__message_errors_variable):
            pipefy.pipe(pipe_id="123", response_fields=self.__check_pattern_response_id)

    # PIPE INFORMATIONS
    def test_pipe_informations_send_new_valid_response_fields_and_return_dict(self, collection_pipefy_fixture,variable_pipefy):
        pipefy=collection_pipefy_fixture
        response = pipefy.pipe_informations(pipe_id=variable_pipefy.pipe_id, response_fields=variable_pipefy.generic_valid_response_fields)
        assert type(response) == dict

    def test_pipe_informations_verify_type_return_dict(self, collection_pipefy_fixture,variable_pipefy):
        pipefy=collection_pipefy_fixture
        response = pipefy.pipe_informations(pipe_id=variable_pipefy.pipe_id)
        assert type(response) == dict

    def test_pipe_informations_dont_send_param_require_return_typeerror(self, collection_pipefy_fixture):
        pipefy=collection_pipefy_fixture
        with pytest.raises(TypeError, match=self.__message_variable_not_send):
            pipefy.pipe_informations()

    def test_pipe_informations_check_if_name_query_into_return_data(self, collection_pipefy_fixture,variable_pipefy):
        pipefy=collection_pipefy_fixture
        response = pipefy.pipe_informations(pipe_id=variable_pipefy.pipe_id)
        assert "pipe" in response
    
    def test_pipe_informations_send_wrong_query_and_return_valueerror(self, collection_pipefy_fixture,variable_pipefy):
        pipefy=collection_pipefy_fixture
        with pytest.raises(ValueError, match=self.__message_wrong_query):
            pipefy.pipe_informations(pipe_id=variable_pipefy.pipe_id, response_fields=variable_pipefy.generic_wrong_response_fields)

    def test_pipe_informations_send_wrong_one_type_variable_not_required_and_return_valueerror(self, collection_pipefy_fixture):
        pipefy=collection_pipefy_fixture
        with pytest.raises(ValueError, match=self.__message_errors_variable):
            pipefy.pipe_informations(pipe_id=123, response_fields=123)

    def test_pipe_informations_send_wrong_more_one_type_variable_and_return_valueerror(self, collection_pipefy_fixture):
        pipefy=collection_pipefy_fixture
        with pytest.raises(ValueError, match=self.__message_errors_variable):
            pipefy.pipe_informations(pipe_id="123", response_fields=123)

    def test_pipe_informations_send_wrong_one_type_variable_required_and_return_valueerror(self, collection_pipefy_fixture):
        pipefy=collection_pipefy_fixture
        with pytest.raises(ValueError, match=self.__message_errors_variable):
            pipefy.pipe_informations(pipe_id="123", response_fields=self.__check_pattern_response_id)

    # PIPE FIELDS
    def test_pipe_fields_send_new_valid_response_fields_and_return_dict(self, collection_pipefy_fixture,variable_pipefy):
        pipefy=collection_pipefy_fixture
        response = pipefy.pipe_fields(pipe_id=variable_pipefy.pipe_id, response_fields=variable_pipefy.generic_valid_response_fields)
        assert type(response) == dict

    def test_pipe_fields_verify_type_return_dict(self, collection_pipefy_fixture,variable_pipefy):
        pipefy=collection_pipefy_fixture
        response = pipefy.pipe_fields(pipe_id=variable_pipefy.pipe_id)
        assert type(response) == dict

    def test_pipe_fields_dont_send_param_require_return_typeerror(self, collection_pipefy_fixture):
        pipefy=collection_pipefy_fixture
        with pytest.raises(TypeError, match=self.__message_variable_not_send):
            pipefy.pipe_fields()

    def test_pipe_fields_check_if_name_query_into_return_data(self, collection_pipefy_fixture,variable_pipefy):
        pipefy=collection_pipefy_fixture
        response = pipefy.pipe_fields(pipe_id=variable_pipefy.pipe_id)
        assert "pipe" in response
    
    def test_pipe_fields_send_wrong_query_and_return_valueerror(self, collection_pipefy_fixture,variable_pipefy):
        pipefy=collection_pipefy_fixture
        with pytest.raises(ValueError, match=self.__message_wrong_query):
            pipefy.pipe_fields(pipe_id=variable_pipefy.pipe_id, response_fields=variable_pipefy.generic_wrong_response_fields)

    def test_pipe_fields_send_wrong_one_type_variable_not_required_and_return_valueerror(self, collection_pipefy_fixture):
        pipefy=collection_pipefy_fixture
        with pytest.raises(ValueError, match=self.__message_errors_variable):
            pipefy.pipe_fields(pipe_id=123, response_fields=123)

    def test_pipe_fields_send_wrong_more_one_type_variable_and_return_valueerror(self, collection_pipefy_fixture):
        pipefy=collection_pipefy_fixture
        with pytest.raises(ValueError, match=self.__message_errors_variable):
            pipefy.pipe_fields(pipe_id="123", response_fields=123)

    def test_pipe_fields_send_wrong_one_type_variable_required_and_return_valueerror(self, collection_pipefy_fixture):
        pipefy=collection_pipefy_fixture
        with pytest.raises(ValueError, match=self.__message_errors_variable):
            pipefy.pipe_fields(pipe_id="123", response_fields=self.__check_pattern_response_id)

    # PIPE WEEBHOOK
    def test_pipe_weebhooks_send_new_valid_response_fields_and_return_dict(self, collection_pipefy_fixture,variable_pipefy):
        pipefy=collection_pipefy_fixture
        response = pipefy.pipe_weebhooks(pipe_id=variable_pipefy.pipe_id, response_fields=variable_pipefy.generic_valid_response_fields)
        assert type(response) == dict

    def test_pipe_weebhooks_verify_type_return_dict(self, collection_pipefy_fixture,variable_pipefy):
        pipefy=collection_pipefy_fixture
        response = pipefy.pipe_weebhooks(pipe_id=variable_pipefy.pipe_id)
        assert type(response) == dict

    def test_pipe_weebhooks_dont_send_param_require_return_typeerror(self, collection_pipefy_fixture):
        pipefy=collection_pipefy_fixture
        with pytest.raises(TypeError, match=self.__message_variable_not_send):
            pipefy.pipe_weebhooks()

    def test_pipe_weebhooks_check_if_name_query_into_return_data(self, collection_pipefy_fixture,variable_pipefy):
        pipefy=collection_pipefy_fixture
        response = pipefy.pipe_weebhooks(pipe_id=variable_pipefy.pipe_id)
        assert "pipe" in response
    
    def test_pipe_weebhooks_send_wrong_query_and_return_valueerror(self, collection_pipefy_fixture,variable_pipefy):
        pipefy=collection_pipefy_fixture
        with pytest.raises(ValueError, match=self.__message_wrong_query):
            pipefy.pipe_weebhooks(pipe_id=variable_pipefy.pipe_id, response_fields=variable_pipefy.generic_wrong_response_fields)

    def test_pipe_weebhooks_send_wrong_one_type_variable_not_required_and_return_valueerror(self, collection_pipefy_fixture):
        pipefy=collection_pipefy_fixture
        with pytest.raises(ValueError, match=self.__message_errors_variable):
            pipefy.pipe_weebhooks(pipe_id=123, response_fields=123)

    def test_pipe_weebhooks_send_wrong_more_one_type_variable_and_return_valueerror(self, collection_pipefy_fixture):
        pipefy=collection_pipefy_fixture
        with pytest.raises(ValueError, match=self.__message_errors_variable):
            pipefy.pipe_weebhooks(pipe_id="123", response_fields=123)

    def test_pipe_weebhooks_send_wrong_one_type_variable_required_and_return_valueerror(self, collection_pipefy_fixture):
        pipefy=collection_pipefy_fixture
        with pytest.raises(ValueError, match=self.__message_errors_variable):
            pipefy.pipe_weebhooks(pipe_id="123", response_fields=self.__check_pattern_response_id)
