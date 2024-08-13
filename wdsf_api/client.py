from collections import namedtuple

from wdsf_api.session import Session
from wdsf_api.parser import Parser

ApiResponse = namedtuple('ApiResponse', ['response', 'data'])

class Client:

    def __init__(self, username, password, **kwargs) -> None:

        self.base_url = 'https://services.worlddancesport.org/api/1/'
        self.raise_for_status = kwargs.get('raise_for_status', False)

        # Initialize the session
        self.session = Session()

        # If credentials are provided, pass them to the session
        if username and password:
            self.session.init_basic_auth(username, password)
    

    def get(
            self,
            path,
            params = {},
            **kwargs
            ):
        
        response = self.session.get(self.base_url + path, params=params)
        
        if kwargs.get('raise_for_status', self.raise_for_status):
            response.raise_for_status()
        
        return response


    def get_competitions(self, **kwargs):
        response = self.get(
            'competition',
            **kwargs
            )
        data = None
        return ApiResponse(response, data)


    def get_competition(self, competition_id, **kwargs):
        response = self.get('competition/' + competition_id, **kwargs)
        data = Parser.parse_competition(response.text)
        return ApiResponse(response, data)
    

    def get_participants(self, competition_id, **kwargs):
        response = self.get(
            'participant',
            params={ 'competitionId': competition_id },
            **kwargs
            )
        data = None
        return ApiResponse(response, data)
    

    def get_participant(self, participant_id, **kwargs):
        response = self.get('participant/' + participant_id, **kwargs)
        data = Parser.parse_participant(response.text)
        return ApiResponse(response, data)
    

    def get_officials(self, competition_id, **kwargs):
        response = self.get(
            'official',
            params={ 'competitionId': competition_id },
            **kwargs
            )
        data = None
        return ApiResponse(response, data)


    def get_official(self, official_id, **kwargs):
        response = self.get('official/' + official_id, **kwargs)
        data = Parser.parse_official(response.text)
        return ApiResponse(response, data)

    
    def get_couples(self, **kwargs):
        raise('Not implemented.')


    def get_couple(self, couple_id, **kwargs):
        raise('Not implemented.')


    def get_teams(self, **kwargs):
        raise('Not implemented.')


    def get_team(self, team_id, **kwargs):
        raise('Not implemented.')


    def get_persons(self, **kwargs):
        raise('Not implemented.')


    def get_person(self, min, **kwargs):
        response = self.get('person/' + min, **kwargs)
        data = Parser.parse_person(response.text)
        return ApiResponse(response, data)