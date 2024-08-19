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

    def __init__(self, environment="production", **kwargs):
        super().__init__(self.BASE_URLS[environment], **kwargs)

    @returns.json
    @get('competition')
    def get_competitions(self, **filter: QueryMap):
        '''Get a list of all competitions.
        
        See also :class:`wdsf_api.query.CompetitionQuery`.'''

    @returns.json
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
        '''Get officials of a competition.'''

    @returns.json
    @get('official/{official_id}')
    def get_official(self, official_id: Path) -> Official:
        '''Get official of a competition by id.'''

    @returns.json
    @get('couple')
    def get_couples(self, **filter: QueryMap) -> List[Couple]:
        '''Get a list of all active couples.
        
        See also :class:`wdsf_api.query.CoupleQuery`.
        '''

    @returns.json
    @get('couple/{couple_id}')
    def get_couple(self, couple_id: Path) -> Couple:
        '''Get couple by id'''

    @returns.json
    @get('team')
    def get_teams(self) -> List[Team]:
        '''Get a list of all active teams

        See also :class:`wdsf_api.query.TeamQuery`
        '''

    @returns.json
    @get('team/{team_id}')
    def get_team(self, team_id: Path) -> Team:
        '''Get team by id.'''

    @returns.json
    @get('person')
    def get_persons(self, **filter: QueryMap) -> List[Person]:
        '''Get a list of all active persons (athletes/adjudicators/chairman).

        See also `wdsf_api.query.PersonQuery`.
        '''

    @returns.json
    @get('person/{min}')
    def get_person(self, min: Path) -> Person:
        '''Get person by MIN.'''
    
    @returns.json
    @get('ranking')
    def get_ranking(self, **filter: QueryMap):
        '''Get the world ranking list.

        See also :class:`wdsf_api.query.RankingQuery`.
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