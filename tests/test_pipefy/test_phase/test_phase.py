import pytest

class TestPipefyPhase():
    __message_errors_variable = r"Check passed variables, something is wrong."
    __message_variable_not_send = r"required positional argument"
    __message_wrong_query = r"Errors, something wrong in your query. Check on logging error."
    __check_pattern_response_id = "{ id }"

    # PHASE
    def test_phase_send_new_valid_response_fields_and_return_dict(self, collection_pipefy_fixture,variable_pipefy):
        pipefy=collection_pipefy_fixture
        response = pipefy.phase(phase_id=variable_pipefy.phase_id, response_fields=variable_pipefy.generic_valid_response_fields)
        assert type(response) == dict

    def test_phase_verify_type_return_dict(self, collection_pipefy_fixture,variable_pipefy):
        pipefy=collection_pipefy_fixture
        response = pipefy.phase(phase_id=variable_pipefy.phase_id)
        assert type(response) == dict

    def test_phase_dont_send_param_require_return_typeerror(self, collection_pipefy_fixture):
        pipefy=collection_pipefy_fixture
        with pytest.raises(TypeError, match=self.__message_variable_not_send):
            pipefy.phase()

    def test_phase_check_if_name_query_into_return_data(self, collection_pipefy_fixture,variable_pipefy):
        pipefy=collection_pipefy_fixture
        response = pipefy.phase(phase_id=variable_pipefy.phase_id)
        assert "phase" in response
    
    def test_phase_send_wrong_query_and_return_valueerror(self, collection_pipefy_fixture,variable_pipefy):
        pipefy=collection_pipefy_fixture
        with pytest.raises(ValueError, match=self.__message_wrong_query):
            pipefy.phase(phase_id=variable_pipefy.phase_id, response_fields=variable_pipefy.generic_wrong_response_fields)

    def test_phase_send_wrong_one_type_variable_not_required_and_return_valueerror(self, collection_pipefy_fixture):
        pipefy=collection_pipefy_fixture
        with pytest.raises(ValueError, match=self.__message_errors_variable):
            pipefy.phase(phase_id=123, response_fields=123)

    def test_phase_send_wrong_more_one_type_variable_and_return_valueerror(self, collection_pipefy_fixture):
        pipefy=collection_pipefy_fixture
        with pytest.raises(ValueError, match=self.__message_errors_variable):
            pipefy.phase(phase_id="123", response_fields=123)

    def test_phase_send_wrong_one_type_variable_required_and_return_valueerror(self, collection_pipefy_fixture):
        pipefy=collection_pipefy_fixture
        with pytest.raises(ValueError, match=self.__message_errors_variable):
            pipefy.phase(phase_id="123", response_fields=self.__check_pattern_response_id)