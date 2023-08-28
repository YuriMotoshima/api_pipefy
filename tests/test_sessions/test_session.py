import pytest
from requests import Session

class TestSessions():
    def test_init_is_instance(self, session_fixture):
        session = session_fixture
        assert isinstance(session.session, Session)
        
    def test_init_token(self, session_fixture, variable_token):
        session = session_fixture
        assert session.token == f"Bearer {variable_token}"
        
    def test_init_host_in_endpoint(self, session_fixture, variable_host):
        session = session_fixture
        assert session.endpoint == f"https://{variable_host}.pipefy.com/graphql"
        
    def test_criar_session_retry_total(self, session_fixture):
        session = session_fixture
        retry = session.session.adapters["https://"].max_retries
        # assert retry.total == 5
        assert retry.total == 1
        
    def test_criar_session_retry_backoff_factor(self, session_fixture):
        session = session_fixture
        retry = session.session.adapters["https://"].max_retries
        # assert retry.backoff_factor == 45
        assert retry.backoff_factor == 3
        
    def test_criar_session_headers_igual_to_headers_default(self, session_fixture, variable_headers_default):
        session = session_fixture
        assert session.session.headers == variable_headers_default

    def test_set_header_with_valid_keys_header(self, session_fixture, variable_headers_change):
        session = session_fixture
        session.set_header(variable_headers_change)
        set_header_change = set(variable_headers_change)
        set_header = set(session.session.headers)
        
        assert set_header.intersection(set_header_change) == set_header_change

    def test_set_header_with_valid_values_header(self, session_fixture, variable_headers_change):
        session = session_fixture
        session.set_header(variable_headers_change)
        set_header_change = set(variable_headers_change.values())
        set_header = set(session.session.headers.values())
        
        assert set_header.intersection(set_header_change) == set_header_change
        
    def test_set_header_with_incorrect_type(self, session_fixture):
        session = session_fixture
        with pytest.raises(TypeError, match=r"headers type incorret."):
            session.set_header("application/json")
            
    def test_set_header_with_empty_headers(self, session_fixture):
        session = session_fixture
        with pytest.raises(ValueError, match=r"headers empty."):
            session.set_header({})
            
    def test_get_headers(self, session_fixture, variable_headers_default):
        session = session_fixture
        assert session.get_headers() == variable_headers_default
        
    def test_remove_headers(self, session_fixture):
        session = session_fixture
        session.remove_headers("Content-Type")
        assert "Content-Type" not in session.session.headers
        
    def test_remove_headers_with_incorrect_type(self, session_fixture):
        session = session_fixture
        with pytest.raises(TypeError, match=r"headers type incorret."):
            session.remove_headers(123)
            
    def test_update_headers(self, session_fixture):
        session = session_fixture
        session.update_headers("Content-Type", "application/json")
        assert session.session.headers["Content-Type"] == "application/json"
        
    def test_update_headers_with_incorrect_type(self, session_fixture):
        session = session_fixture
        with pytest.raises(TypeError, match=r"Type incorret."):
            session.update_headers("Content-Type", 123)

    def test_request_get_return_type_dict(self, session_fixture, variable_schema_sucess):
        session = session_fixture
        response = session.get_request(schema=variable_schema_sucess)
        assert type(response) == dict

    def test_request_get_return_error_500(self, session_fixture, variable_schema_error_500):
        session = session_fixture
        with pytest.raises(ValueError, match=r"Wrong response, didn't convert to json."):
            session.get_request(schema=variable_schema_error_500)

    def test_validation_response_return_any_errors(self, session_fixture, variable_response_errors_content):
        session = session_fixture
        with pytest.raises(ValueError, match=r"Errors, something wrong in your query. Check on logging error."):
            session._validation_response(response=variable_response_errors_content)

    def test_validation_response_return_one_error(self, session_fixture, variable_response_error_content):
        session = session_fixture
        with pytest.raises(ValueError, match=r"Check this wrong on logging."):
            session._validation_response(response=variable_response_error_content)

    def test_validation_response_return_error_none_content(self, session_fixture, variable_response_none_content):
        session = session_fixture
        with pytest.raises(ValueError, match=r"Wrong response, didn't convert to json."):
            session._validation_response(response=variable_response_none_content)

    def test_validation_response_return_dict(self, session_fixture, variable_response_success_content):
        session = session_fixture
        resp = session._validation_response(response=variable_response_success_content)
        assert type(resp) == dict

    def test_validation_response_return_not_empty(self, session_fixture, variable_response_success_content):
        session = session_fixture
        resp = session._validation_response(response=variable_response_success_content)
        assert resp != {}
