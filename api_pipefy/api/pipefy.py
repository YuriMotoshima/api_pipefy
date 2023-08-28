from api_pipefy.libs.session import Sessions


class Pipefy(Sessions):
    def __init__(self, token:str, host:str="api") -> None:
        super().__init__(token=token, host=host)
        self.schema = lambda query: { "query" : query }
        self.check_variable_similarity_type = lambda item, typing: True if item == None or type(item) == typing else False
        self.func_pattern_query= lambda name_query, id, response_fields: '''{ %(name_query)s (%(id)s) %(response_fields)s }''' % {'name_query':str(name_query), 'id':id,'response_fields':str(response_fields)}
        self.__message_errors_variable = "Check passed variables, something is wrong."
    
    # QUERY
    def _me(self, response_fields:str=None) -> dict:
        check_variables = all(map(self.check_variable_similarity_type,[response_fields],[str]))
        if not check_variables:
            raise ValueError(self.__message_errors_variable)

        response_fields = response_fields or '''{ id name email }'''
        query = '''{ me %(response_fields)s}''' %{
            'response_fields':response_fields
        }
        schema = self.schema(query=query)
        response = self.get_request(schema=schema)
        return response.get("data", {})
    
    def organization(self, organization_id:int, response_fields:str=None) -> dict:
        check_variables = all(map(self.check_variable_similarity_type,[organization_id,response_fields],[int,str]))
        if not check_variables:
            raise ValueError(self.__message_errors_variable)

        response_fields = response_fields or '''{ id name membersCount }'''

        query = '''{ organization(id:%(organization_id)s) %(response_fields)s}''' % {
            'organization_id':organization_id,
            'response_fields':response_fields
        } 

        schema = self.schema(query=query)
        response = self.get_request(schema=schema)
        return response.get("data", {})

    def members_organization(self, organization_id:int, response_fields:str=None) -> dict:
        check_variables = all(map(self.check_variable_similarity_type,[organization_id,response_fields],[int,str]))
        if not check_variables:
            raise ValueError(self.__message_errors_variable)

        response_fields = response_fields or '''{ id name membersCount members{ role_name user{ id uuid username name email phone locale departmentKey hasUnreadNotifications } } }'''

        query = self.func_pattern_query(name_query="organization", id=f"id:{organization_id}", response_fields=response_fields) 
        schema = self.schema(query=query)
        response = self.get_request(schema=schema)
        return response.get("data", {})

    def pipes_organization(self, organization_id:int, response_fields:str=None) -> dict:
        check_variables = all(map(self.check_variable_similarity_type,[organization_id,response_fields],[int,str]))
        if not check_variables:
            raise ValueError(self.__message_errors_variable)

        response_fields = response_fields or '''{ id name pipesCount pipes{ cards_count id uuid name created_at description emailAddress users_count webhooks{ id name headers } } }'''

        query = self.func_pattern_query(name_query="organization", id=f"id:{organization_id}", response_fields=response_fields) 
        schema = self.schema(query=query)
        response = self.get_request(schema=schema)
        return response.get("data", {})

    def tables_organization(self, organization_id:int, response_fields:str=None) -> dict:
        check_variables = all(map(self.check_variable_similarity_type,[organization_id,response_fields],[int,str]))
        if not check_variables:
            raise ValueError(self.__message_errors_variable)

        response_fields = response_fields or '''{ id name tables{ edges{ cursor node{ table_records_count authorization id uuid name users_count } } } }'''

        query = self.func_pattern_query(name_query="organization", id=f"id:{organization_id}", response_fields=response_fields) 
        schema = self.schema(query=query)
        response = self.get_request(schema=schema)
        return response.get("data", {})
    
    def pipe(self, pipe_id:int, response_fields:str=None) -> dict:
        check_variables = all(map(self.check_variable_similarity_type,[pipe_id,response_fields],[int,str]))
        if not check_variables:
            raise ValueError(self.__message_errors_variable)

        response_fields = response_fields or ''' { id name start_form_fields { label id } labels { name id } phases { name fields { label id } } }'''

        query = self.func_pattern_query(name_query="pipe", id=f"id:{pipe_id}", response_fields=response_fields)
        schema = self.schema(query=query)
        response = self.get_request(schema=schema)
        return response.get("data", {})
    
    def pipe_informations(self, pipe_id:int, response_fields:str=None) -> dict:
        check_variables = all(map(self.check_variable_similarity_type,[pipe_id,response_fields],[int,str]))
        if not check_variables:
            raise ValueError(self.__message_errors_variable)

        response_fields = response_fields or '''{ id suid uuid name cards_count users_count opened_cards_count created_at description emailAddress organizationId phases{ id name } }'''

        query = self.func_pattern_query(name_query="pipe", id=f"id:{pipe_id}", response_fields=response_fields)
        schema = self.schema(query=query)
        response = self.get_request(schema=schema)
        return response.get("data", {})

    def pipe_fields(self, pipe_id:int, response_fields:str=None) -> dict:
        check_variables = all(map(self.check_variable_similarity_type,[pipe_id, response_fields],[int,str]))
        if not check_variables:
            raise ValueError(self.__message_errors_variable)

        response_fields = response_fields or '''{ organization { id } cards_count phases { id name fields { id label editable uuid required} } start_form_fields { id label editable uuid required } }'''

        query = self.func_pattern_query(name_query="pipe", id=f"id:{pipe_id}", response_fields=response_fields)
        schema = self.schema(query=query)
        response = self.get_request(schema=schema)
        return response.get("data", {})

    def pipe_weebhooks(self, pipe_id:int, response_fields:str=None) -> dict:
        check_variables = all(map(self.check_variable_similarity_type,[pipe_id, response_fields],[int,str]))
        if not check_variables:
            raise ValueError(self.__message_errors_variable)

        response_fields = response_fields or '''{ id name webhooks{ id name url actions email headers } }'''

        query = self.func_pattern_query(name_query="pipe", id=f"id:{pipe_id}", response_fields=response_fields)
        schema = self.schema(query=query)
        response = self.get_request(schema=schema)
        return response.get("data", {})

    def phase(self, phase_id:int, response_fields:str=None, after:str=None) -> dict:
        check_variables = all(map(self.check_variable_similarity_type,[phase_id, response_fields, after],[int, str, str]))
        if not check_variables:
            raise ValueError(self.__message_errors_variable)

        response_fields = response_fields or '{ cards{ pageInfo { endCursor hasNextPage } edges { node { id title createdAt finished_at updated_at createdBy { id name } assignees { id name email } comments { text } comments_count current_phase { name } done due_date fields { name value datetime_value field { id options type label } array_value  } labels { name } createdAt phases_history { phase { name id } created_at duration firstTimeIn lastTimeOut } url } } } }'
        
        query = self.func_pattern_query(name_query="phase", id=f"id:{phase_id}", response_fields=response_fields)
        if after:
            query = query.replace("cards", f'cards(after:"{after}")')

        schema = self.schema(query=query)
        response = self.get_request(schema=schema)
        return response.get("data", {})

    def phase_fields(self, phase_id:int, response_fields:str=None) -> dict:
        check_variables = all(map(self.check_variable_similarity_type,[phase_id, response_fields],[int, str]))
        if not check_variables:
            raise ValueError(self.__message_errors_variable)

        response_fields = response_fields or '{ fields{ id options label type required editable internal_id synced_with_card } }'
        
        query = self.func_pattern_query(name_query="phase", id=f"id:{phase_id}", response_fields=response_fields)

        schema = self.schema(query=query)
        response = self.get_request(schema=schema)
        return response.get("data", {})

    def cards(self, pipe_id:int, response_fields:str=None, after:str=None) -> dict:
        check_variables = all(map(self.check_variable_similarity_type,[pipe_id, response_fields, after],[int, str, str]))
        if not check_variables:
            raise ValueError(self.__message_errors_variable)

        response_fields = response_fields or '{ cards{ pageInfo { endCursor hasNextPage } edges { node { id title createdAt finished_at updated_at createdBy { id name } assignees { id name email } comments { text } comments_count current_phase { name } done due_date fields { name value datetime_value field { id options type label } array_value  } labels { name } createdAt phases_history { phase { name id } created_at duration firstTimeIn lastTimeOut } url } } } }'
        
        query = self.func_pattern_query(name_query="cards", id=f"pipe_id:{pipe_id}", response_fields=response_fields)
        if after:
            query = query.replace("cards", f'cards(after:"{after}")')

        schema = self.schema(query=query)
        response = self.get_request(schema=schema)
        return response.get("data", {})


    def __(self, response_fields:str=None) -> dict:
        check_variables = all(map(self.check_variable_similarity_type,[response_fields],[str]))
        if not check_variables:
            raise ValueError(self.__message_errors_variable)

        response_fields = response_fields or '''{ id name membersCount }'''

        query = self.func_pattern_query(name_query="", id="", response_fields=response_fields)
        schema = self.schema(query=query)
        response = self.get_request(schema=schema)
        return response.get("data", {})
    

 