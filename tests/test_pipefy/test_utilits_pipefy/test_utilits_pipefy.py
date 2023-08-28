import pytest
from requests import Session

class TestInitConftestPipefy:
    def test_collection_variables_pipefy(self,variable_pipefy):
        assert isinstance(variable_pipefy, object)

    def test_collection_pipefy(self,collection_pipefy_fixture):
        assert isinstance(collection_pipefy_fixture, object)

    def test_type_schema_sucess(self,variable_schema_sucess):
        assert type(variable_schema_sucess) == dict

    def test_schema_sucess_if_content_is_correct(self,variable_schema_sucess):
        assert variable_schema_sucess == {"query":'''{ me { id } }'''}

    def test_type_schema_error(self,variable_schema_error_500):
        assert type(variable_schema_error_500) == dict

    def test_schema_error_if_content_is_correct(self,variable_schema_error_500):
        assert variable_schema_error_500 == {"_query":'''{ me { id } }'''}


class TestPipefy():
    __message_errors_variable = r"Check passed variables, something is wrong."
    __message_variable_not_send = r"required positional argument"
    __message_wrong_query = r"Errors, something wrong in your query. Check on logging error."
    __message_error_lambda = r"invalid literal for"

    def test_init_is_instance(self, collection_pipefy_fixture):
        pipefy=collection_pipefy_fixture
        assert isinstance(pipefy.session, Session)
        
    def test_init_token(self, collection_pipefy_fixture, variable_pipefy):
        pipefy=collection_pipefy_fixture
        assert pipefy.token == f"Bearer {variable_pipefy.token}"
        
    def test_init_host_in_endpoint(self, collection_pipefy_fixture, variable_pipefy):
        pipefy=collection_pipefy_fixture
        assert pipefy.endpoint == f"https://{variable_pipefy.host_test}.pipefy.com/graphql"
    
    # LAMBDA
    def test_self_schema_send_any_params_and_return_dict(self, collection_pipefy_fixture):
        pipefy=collection_pipefy_fixture
        schema = pipefy.schema(query="xpto")
        assert type(schema) == dict

    def test_self_schema_dont_send_params_and_return_typeerror(self, collection_pipefy_fixture):
        pipefy=collection_pipefy_fixture
        with pytest.raises(TypeError, match=self.__message_variable_not_send):
            pipefy.schema()

    def test_self_check_variable_similarity_type_dont_send_one_param_and_return_typeerror(self, collection_pipefy_fixture):
        pipefy=collection_pipefy_fixture
        with pytest.raises(TypeError, match=self.__message_variable_not_send):
            pipefy.check_variable_similarity_type(int)

    def test_self_check_variable_similarity_type_send_wrong_param_and_return_typeerror(self, collection_pipefy_fixture):
        pipefy=collection_pipefy_fixture
        check_variables = pipefy.check_variable_similarity_type("1",int)
        assert check_variables == False

    def test_self_check_variable_similarity_type_send_correct_param_and_return_typeerror(self, collection_pipefy_fixture):
        pipefy=collection_pipefy_fixture
        check_variables = pipefy.check_variable_similarity_type(1,int)
        assert check_variables == True

    def test_self_func_pattern_query_dont_send_one_param_and_return_typeerror(self, collection_pipefy_fixture):
        pipefy=collection_pipefy_fixture
        with pytest.raises(TypeError, match=self.__message_variable_not_send):
            pipefy.func_pattern_query()

    def test_self_func_pattern_query_send_wrong_param_and_return_typeerror(self, collection_pipefy_fixture):
        pipefy=collection_pipefy_fixture
        with pytest.raises(ValueError, match=self.__message_error_lambda):
            pipefy.func_pattern_query(1,"int","int")

    def test_self_func_pattern_query_send_correct_param_and_return_typeerror(self, collection_pipefy_fixture):
        pipefy=collection_pipefy_fixture
        check_variables = pipefy.func_pattern_query("str",1,"str")
        assert check_variables == "{ str (1) str }"

    # ME
    def test_me_send_new_valid_query_and_return_dict(self, collection_pipefy_fixture,variable_pipefy):
        pipefy=collection_pipefy_fixture
        response = pipefy._me(response_fields=variable_pipefy.generic_valid_response_fields)
        assert type(response) == dict

    def test_me_dont_send_params_and_return_dict(self, collection_pipefy_fixture):
        pipefy=collection_pipefy_fixture
        response = pipefy._me()
        assert type(response) == dict

    def test_me_check_if_name_query_into_return_data(self, collection_pipefy_fixture):
        pipefy=collection_pipefy_fixture
        response = pipefy._me()
        assert "me" in response

    def test_me_send_wrong_response_fields_and_return_valueerror(self, collection_pipefy_fixture, variable_pipefy):
        pipefy=collection_pipefy_fixture
        with pytest.raises(ValueError, match=self.__message_wrong_query):
            pipefy._me(response_fields=variable_pipefy.generic_wrong_response_fields)

    def test_me_send_wrong_type_variable_and_return_valueerror(self, collection_pipefy_fixture):
        pipefy=collection_pipefy_fixture
        with pytest.raises(ValueError, match=self.__message_errors_variable):
            pipefy._me(response_fields=123)
