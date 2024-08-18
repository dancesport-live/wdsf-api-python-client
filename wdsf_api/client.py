from typing import List
from uplink import Consumer, get, headers, Path, Query, QueryMap, returns

from wdsf_api.schema import *


@headers({
    'Accept': 'application/json',
    'User-Agent': 'WDSF API Python Client',
})
class WdsfApi(Consumer):
    '''A Python Client for the WDSF API.'''

    BASE_URLS = {
        'staging': 'https://sandbox.worlddancesport.org/api/1/',
        'production': 'https://services.worlddancesport.org/api/1/'
    }

    def __init__(self, env="production", **kwargs):
        super().__init__(self.BASE_URLS[env], **kwargs)

    @returns.json
    @get('competition')
    def get_competitions(self, **filter: QueryMap):
        '''Get a list of all competitions
        
        Use query parameter to filter by

        from [DateTime] : list competitions since and including this date (YYYY/MM/DD)
        to [DateTime] : list competitions after and including this date (YYYY/MM/DD)
        modifiedsince [Date] : list competitions that have been modified since this date (YYYY/MM/DDThh:mm:ss)
        worldranking [bool] : true to list competitions that are included in the world ranking list
        division [string] : General/Professional
        status: The status of the competition. Valid values are: PreRegistration, Registering, RegistrationClosed, Processing, Closed, Canceled
        location: The city name where the competition takes/took place.
        '''

    @returns.json(Competition)
    @get('competition/{competition_id}')
    def get_competition(self, competition_id: Path) -> Competition:
        '''Get competition by id.'''

    @returns.json
    @get('participant')
    def get_participants(self, competition_id: Query('competitionId')) -> List[Participant]:
        '''Get participants of a competition.'''
    
    @returns.json
    @get('participant/{participant_id}')
    def get_participant(self, participant_id: Path) -> Participant:
        '''Get participant of a competition by id.'''
    
    @returns.json
    @get('official')
    def get_officials(self, competition_id: Query('competitionId')) -> List[Official]:
        '''Get officials of a ccompetition.'''

    @returns.json
    @get('official/{official_id}')
    def get_official(self, official_id: Path) -> Official:
        '''Get official of a competition by id.'''

    @returns.json
    @get('couple')
    def get_couples(self, **filter: QueryMap) -> List[Couple]:
        '''Get a list of all active couples
        
        Use query parameter to filter by
        
        name [string] : list only couples where any member's name starts with this filter's value
        phonetic [bool/optional/default=false] : when true, the name filter is used phonetical instead of litteral.
        min [list of int] :
        min,min,min.. : list all couples where the members have any of the MIN given
        min+min : list all couples where all members have the MIN given (make sure the + is URL encoded!)
        nameOrMin [string] : list couple having a name or MIN starting with this filter's value
        ageGroup [string] : list couples of an age group (Adult, Senior I, Senior II, Youth, ...)
        division [string] : General/Professional
        status [string] : The couple's status, if not given only active couples will be shown. "Any" will show all.
        country [string] : The couple's country. Separate each country name by a pipe (|).
        '''

    @returns.json
    @get('couple/{couple_id}')
    def get_couple(self, couple_id: Path) -> Couple:
        '''Get couple by id'''

    @returns.json
    @get('team')
    def get_teams(self) -> List[Team]:
        '''Get a list of all active teams

        Use query parameter to filter by

        name [string] : list only couples where any member's name starts with this filter's value
        phonetic [bool/optional/default=false] : when true, the name filter is used phonetical instead of litteral.
        '''

    @returns.json
    @get('team/{team_id}')
    def get_team(self, team_id: Path) -> Team:
        '''Get team by id.'''

    @returns.json
    @get('person')
    def get_persons(self, **filter: QueryMap) -> List[Person]:
        '''Get a list of all active persons (athletes/adjudicators/chairman)

        Use query parameter to filter by

        name [string] : list all persons having a name starting with this filter's value. Separate name und surname with a comma(,). The order is not relevant.
        phonetic [bool/optional/default=false] : when true, the name filter is used phonetical instead of litteral.
        min [int] : list person with this MIN (1xxxxxxx can be omitted)
        nameOrMin [string] : list persons having a name or MIN starting with this filter's value
        ageGroup [string] : list persons of an age group (Adult, Senior I, Senior II, Youth, ...)
        division [string] : General/Professional
        type [string,string,...] : list persons of a certain type (Athlete, Adjudicator, Chairman)
        status [string] : list of the person's license status (Active, Retired, Expired, Suspended, Revoked).
        '''

    @returns.json
    @get('person/{min}')
    def get_person(self, min: Path) -> Person:
        '''Get person by MIN'''
    
    @returns.json
    @get('ranking')
    def get_ranking(self, **filter: QueryMap):
        '''Get the world ranking list

        Use query paramter to filter by

        ageGroup [string] : the age group (Adult, Senior I, Senior II, Youth, ...)
        discipline [string] : the discipline (Latin, Standard, Ten Dance)
        division [string] : the division (General, Professional)
        form [string] : the dance form (not used yet)
        gender [string] : the gender (Male, Female)
        date [Date/optional] : The date of the ranking list (YYYY/MM/DD)
        limit [int/optional] : Provide only the top x entries
        '''
    
    @returns.json
    @get('country')
    def get_countries(self) -> List[Country]:
        '''Get a list of allowed country names.'''

    @returns.json
    @get('age')
    def get_age(self):
        '''Get a list of age restrictions'''
    
    @returns.json
    @get('age/checkforcompetition/{min1},{min2}/{competition_id}')
    def check_for_competition(self, min1: Path, min2: Path, competition_id: Path):
        '''Check if a couple is allowed to take part in a competition by their age group.

        The couple is defined by their MINs.
        This also works for competitions in years other than the current.'''


'''
TODO: Helper functions to create filters:

from [DateTime] : list competitions since and including this date (YYYY/MM/DD)
to [DateTime] : list competitions after and including this date (YYYY/MM/DD)
modifiedsince [Date] : list competitions that have been modified since this date (YYYY/MM/DDThh:mm:ss)
worldranking [bool] : true to list competitions that are included in the world ranking list
division [string] : General/Professional
status: The status of the competition. Valid values are:PreRegistration, Registering, RegistrationClosed, Processing, Closed, Canceled
location: The city name where the competition takes/took place.

name [string] : list only couples where any member's name starts with this filter's value
phonetic [bool/optional/default=false] : when true, the name filter is used phonetical instead of litteral.
min [list of int] :
min,min,min.. : list all couples where the members have any of the MIN given
min+min : list all couples where all members have the MIN given (make sure the + is URL encoded!)
nameOrMin [string] : list couple having a name or MIN starting with this filter's value
ageGroup [string] : list couples of an age group (Adult, Senior I, Senior II, Youth, ...)
division [string] : General/Professional
status [string] : The couple's status, if not given only active couples will be shown. "Any" will show all.
country [string] : The couple's country. Separate each country name by a pipe (|).

name [string] : list only couples where any member's name starts with this filter's value
phonetic [bool/optional/default=false] : when true, the name filter is used phonetical instead of litteral.

name [string] : list all persons having a name starting with this filter's value. Separate name und surname with a comma(,). The order is not relevant.
phonetic [bool/optional/default=false] : when true, the name filter is used phonetical instead of litteral.
min [int] : list person with this MIN (1xxxxxxx can be omitted)
nameOrMin [string] : list persons having a name or MIN starting with this filter's value
ageGroup [string] : list persons of an age group (Adult, Senior I, Senior II, Youth, ...)
division [string] : General/Professional
type [string,string,...] : list persons of a certain type (Athlete, Adjudicator, Chairman)
status [string] : list of the person's license status (Active, Retired, Expired, Suspended, Revoked).

ageGroup [string] : the age group (Adult, Senior I, Senior II, Youth, ...)
discipline [string] : the discipline (Latin, Standard, Ten Dance)
division [string] : the division (General, Professional)
form [string] : the dance form (not used yet)
gender [string] : the gender (Male, Female)
date [Date/optional] : The date of the ranking list (YYYY/MM/DD)
limit [int/optional] : Provide only the top x entries
'''