import pytest

class TestPipefyOrganization():
    __message_errors_variable = r"Check passed variables, something is wrong."
    __message_variable_not_send = r"required positional argument"
    __message_wrong_query = r"Errors, something wrong in your query. Check on logging error."
    __check_pattern_response_id = "{ id }"

    # ORGANIZATION
    def test_organization_send_new_valid_response_fields_and_return_dict(self, collection_pipefy_fixture,variable_pipefy):
        pipefy=collection_pipefy_fixture
        response = pipefy.organization(organization_id=variable_pipefy.organization_id, response_fields=variable_pipefy.generic_valid_response_fields)
        assert type(response) == dict

    def test_organization_verify_type_return_dict(self, collection_pipefy_fixture,variable_pipefy):
        pipefy=collection_pipefy_fixture
        response = pipefy.organization(organization_id=variable_pipefy.organization_id)
        assert type(response) == dict

    def test_organization_dont_send_param_require_return_typeerror(self, collection_pipefy_fixture):
        pipefy=collection_pipefy_fixture
        with pytest.raises(TypeError, match=self.__message_variable_not_send):
            pipefy.organization()

    def test_organization_check_if_name_query_into_return_data(self, collection_pipefy_fixture,variable_pipefy):
        pipefy=collection_pipefy_fixture
        response = pipefy.organization(organization_id=variable_pipefy.organization_id)
        assert "organization" in response
    
    def test_organization_send_wrong_query_and_return_valueerror(self, collection_pipefy_fixture,variable_pipefy):
        pipefy=collection_pipefy_fixture
        with pytest.raises(ValueError, match=self.__message_wrong_query):
            pipefy.organization(organization_id=variable_pipefy.organization_id, response_fields=variable_pipefy.generic_wrong_response_fields)

    def test_organization_send_wrong_one_type_variable_not_required_and_return_valueerror(self, collection_pipefy_fixture):
        pipefy=collection_pipefy_fixture
        with pytest.raises(ValueError, match=self.__message_errors_variable):
            pipefy.organization(organization_id=123, response_fields=123)

    def test_organization_send_wrong_more_one_type_variable_and_return_valueerror(self, collection_pipefy_fixture):
        pipefy=collection_pipefy_fixture
        with pytest.raises(ValueError, match=self.__message_errors_variable):
            pipefy.organization(organization_id="123", response_fields=123)

    def test_organization_send_wrong_one_type_variable_required_and_return_valueerror(self, collection_pipefy_fixture):
        pipefy=collection_pipefy_fixture
        with pytest.raises(ValueError, match=self.__message_errors_variable):
            pipefy.organization(organization_id="123", response_fields=self.__check_pattern_response_id)

    # MEMBERS ORGANIZATION
    def test_members_organization_send_new_valid_response_fields_and_return_dict(self, collection_pipefy_fixture,variable_pipefy):
        pipefy=collection_pipefy_fixture
        response = pipefy.members_organization(organization_id=variable_pipefy.organization_id, response_fields=variable_pipefy.generic_valid_response_fields)
        assert type(response) == dict

    def test_members_organization_verify_type_return_dict(self, collection_pipefy_fixture,variable_pipefy):
        pipefy=collection_pipefy_fixture
        response = pipefy.members_organization(organization_id=variable_pipefy.organization_id)
        assert type(response) == dict

    def test_members_organization_dont_send_param_require_return_typeerror(self, collection_pipefy_fixture):
        pipefy=collection_pipefy_fixture
        with pytest.raises(TypeError, match=self.__message_variable_not_send):
            pipefy.members_organization()

    def test_members_organization_check_if_name_query_into_return_data(self, collection_pipefy_fixture,variable_pipefy):
        pipefy=collection_pipefy_fixture
        response = pipefy.members_organization(organization_id=variable_pipefy.organization_id)
        assert "organization" in response
    
    def test_members_organization_send_wrong_query_and_return_valueerror(self, collection_pipefy_fixture,variable_pipefy):
        pipefy=collection_pipefy_fixture
        with pytest.raises(ValueError, match=self.__message_wrong_query):
            pipefy.members_organization(organization_id=variable_pipefy.organization_id, response_fields=variable_pipefy.generic_wrong_response_fields)

    def test_members_organization_send_wrong_one_type_variable_not_required_and_return_valueerror(self, collection_pipefy_fixture):
        pipefy=collection_pipefy_fixture
        with pytest.raises(ValueError, match=self.__message_errors_variable):
            pipefy.members_organization(organization_id=123, response_fields=123)

    def test_members_organization_send_wrong_more_one_type_variable_and_return_valueerror(self, collection_pipefy_fixture):
        pipefy=collection_pipefy_fixture
        with pytest.raises(ValueError, match=self.__message_errors_variable):
            pipefy.members_organization(organization_id="123", response_fields=123)

    def test_members_organization_send_wrong_one_type_variable_required_and_return_valueerror(self, collection_pipefy_fixture):
        pipefy=collection_pipefy_fixture
        with pytest.raises(ValueError, match=self.__message_errors_variable):
            pipefy.members_organization(organization_id="123", response_fields=self.__check_pattern_response_id)

    # PIPES ORGANIZATION
    def test_pipes_organization_send_new_valid_response_fields_and_return_dict(self, collection_pipefy_fixture,variable_pipefy):
        pipefy=collection_pipefy_fixture
        response = pipefy.pipes_organization(organization_id=variable_pipefy.organization_id, response_fields=variable_pipefy.generic_valid_response_fields)
        assert type(response) == dict

    def test_pipes_organization_verify_type_return_dict(self, collection_pipefy_fixture,variable_pipefy):
        pipefy=collection_pipefy_fixture
        response = pipefy.pipes_organization(organization_id=variable_pipefy.organization_id)
        assert type(response) == dict

    def test_pipes_organization_dont_send_param_require_return_typeerror(self, collection_pipefy_fixture):
        pipefy=collection_pipefy_fixture
        with pytest.raises(TypeError, match=self.__message_variable_not_send):
            pipefy.pipes_organization()

    def test_pipes_organization_check_if_name_query_into_return_data(self, collection_pipefy_fixture,variable_pipefy):
        pipefy=collection_pipefy_fixture
        response = pipefy.pipes_organization(organization_id=variable_pipefy.organization_id)
        assert "organization" in response
    
    def test_pipes_organization_send_wrong_query_and_return_valueerror(self, collection_pipefy_fixture,variable_pipefy):
        pipefy=collection_pipefy_fixture
        with pytest.raises(ValueError, match=self.__message_wrong_query):
            pipefy.pipes_organization(organization_id=variable_pipefy.organization_id, response_fields=variable_pipefy.generic_wrong_response_fields)

    def test_pipes_organization_send_wrong_one_type_variable_not_required_and_return_valueerror(self, collection_pipefy_fixture):
        pipefy=collection_pipefy_fixture
        with pytest.raises(ValueError, match=self.__message_errors_variable):
            pipefy.pipes_organization(organization_id=123, response_fields=123)

    def test_pipes_organization_send_wrong_more_one_type_variable_and_return_valueerror(self, collection_pipefy_fixture):
        pipefy=collection_pipefy_fixture
        with pytest.raises(ValueError, match=self.__message_errors_variable):
            pipefy.pipes_organization(organization_id="123", response_fields=123)

    def test_pipes_organization_send_wrong_one_type_variable_required_and_return_valueerror(self, collection_pipefy_fixture):
        pipefy=collection_pipefy_fixture
        with pytest.raises(ValueError, match=self.__message_errors_variable):
            pipefy.pipes_organization(organization_id="123", response_fields=self.__check_pattern_response_id)

    # TABLES ORGANIZATION
    def test_tables_organization_send_new_valid_response_fields_and_return_dict(self, collection_pipefy_fixture,variable_pipefy):
        pipefy=collection_pipefy_fixture
        response = pipefy.tables_organization(organization_id=variable_pipefy.organization_id, response_fields=variable_pipefy.generic_valid_response_fields)
        assert type(response) == dict

    def test_tables_organization_verify_type_return_dict(self, collection_pipefy_fixture,variable_pipefy):
        pipefy=collection_pipefy_fixture
        response = pipefy.tables_organization(organization_id=variable_pipefy.organization_id)
        assert type(response) == dict

    def test_tables_organization_dont_send_param_require_return_typeerror(self, collection_pipefy_fixture):
        pipefy=collection_pipefy_fixture
        with pytest.raises(TypeError, match=self.__message_variable_not_send):
            pipefy.tables_organization()

    def test_tables_organization_check_if_name_query_into_return_data(self, collection_pipefy_fixture,variable_pipefy):
        pipefy=collection_pipefy_fixture
        response = pipefy.tables_organization(organization_id=variable_pipefy.organization_id)
        assert "organization" in response
    
    def test_tables_organization_send_wrong_query_and_return_valueerror(self, collection_pipefy_fixture,variable_pipefy):
        pipefy=collection_pipefy_fixture
        with pytest.raises(ValueError, match=self.__message_wrong_query):
            pipefy.tables_organization(organization_id=variable_pipefy.organization_id, response_fields=variable_pipefy.generic_wrong_response_fields)

    def test_tables_organization_send_wrong_one_type_variable_not_required_and_return_valueerror(self, collection_pipefy_fixture):
        pipefy=collection_pipefy_fixture
        with pytest.raises(ValueError, match=self.__message_errors_variable):
            pipefy.tables_organization(organization_id=123, response_fields=123)

    def test_tables_organization_send_wrong_more_one_type_variable_and_return_valueerror(self, collection_pipefy_fixture):
        pipefy=collection_pipefy_fixture
        with pytest.raises(ValueError, match=self.__message_errors_variable):
            pipefy.tables_organization(organization_id="123", response_fields=123)

    def test_tables_organization_send_wrong_one_type_variable_required_and_return_valueerror(self, collection_pipefy_fixture):
        pipefy=collection_pipefy_fixture
        with pytest.raises(ValueError, match=self.__message_errors_variable):
            pipefy.tables_organization(organization_id="123", response_fields=self.__check_pattern_response_id)