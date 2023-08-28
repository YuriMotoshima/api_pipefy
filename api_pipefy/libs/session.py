import json
import time

import requests
from requests import Session
from requests.adapters import HTTPAdapter

import urllib3
from urllib3.util.retry import Retry

from api_pipefy.libs.excepts import exceptions

class Sessions():
    def __init__(self, token:str, host:str) -> None:
        urllib3.disable_warnings()
        self.token = token if "Bearer" in token else "Bearer %s" % token
        self.endpoint = f"https://{host}.pipefy.com/graphql"
        self.session = self.__criar_session()
        
    def __criar_session(self) -> Session:
        self.session = requests.Session()
        # retry = Retry(total=5, backoff_factor=45)
        retry = Retry(total=1, backoff_factor=3)
        adapter = HTTPAdapter(max_retries=retry)
        self.session.mount("https://", adapter)
        self.session.headers["Accept"] = "application/json"
        self.session.headers["Content-Type"] = "application/json"
        self.session.headers["Authorization"] = self.token
        return self.session
    
    def set_header(self, headers:dict) -> None:
        if type(headers) != dict:
            raise TypeError("headers type incorret.")
        elif len(headers) < 1:
            raise ValueError("headers empty.")
        
        for keys, values in headers.items():
            self.session.headers[keys] = values
        
    def get_headers(self) -> dict:
        return self.session.headers
    
    def remove_headers(self, header:str) -> None:
        if type(header) != str:
            raise TypeError("headers type incorret.")
        return self.session.headers.pop(header)
    
    def update_headers(self, header:str, new_value:str) -> None:
        if type(header) != str or type(new_value) != str:
            raise TypeError("Type incorret.")
        self.session.headers[header] = new_value

    def _validation_response(self, response:object):
        try:
            _response = json.loads(response.text)
        except ValueError:
            exceptions(response.text)
            raise ValueError("Wrong response, didn't convert to json.")
        
        key_data = list(_response.keys()) if type(_response) == dict else _response

        if ("error" in key_data) or ("errors" in key_data):

            if _response.get('error'):
                error = {"Error":_response.get('error_description', _response.get('error'))}
                exceptions(error)
                raise ValueError("Check this wrong on logging.")
            
            elif _response.get('errors'):
                errors = {"Error":[error.get('message') for error in _response.get('errors')]}
                exceptions(errors)
                raise ValueError("Errors, something wrong in your query. Check on logging error.")
          
        return _response

    def get_request(self, schema:dict, method:str="POST"):
      
        response = self.session.request(method=method, url=self.endpoint, json=schema, verify=False)
      
        count_try = 0
        status_code = int(response.status_code)
        
        # while count_try < 4 and status_code > 399:
        while count_try < 1 and status_code > 399:
            time.sleep(40)
            response = self.session.request(method=method, url=self.endpoint, json=schema, verify=False)
            count_try = count_try + 1
            status_code = int(response.status_code)
            print(f"{count_try} connection attempt made. Status Code: {status_code}")
        
        return self._validation_response(response=response)