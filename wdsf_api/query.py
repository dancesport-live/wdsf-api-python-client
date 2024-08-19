import datetime
from enum import Enum
from typing import Any, List

from pydantic import BaseModel, Field, field_serializer

from wdsf_api.schema import Competition, Country

class BaseQuery(BaseModel):
    def build(self):
        return self.model_dump(by_alias=True, exclude_none=True)

class CompetitionQuery(BaseQuery):
    '''Use query parameter to filter by
    
    from [DateTime] : list competitions since and including this date (YYYY/MM/DD)
    to [DateTime] : list competitions after and including this date (YYYY/MM/DD)
    modifiedsince [Date] : list competitions that have been modified since this date (YYYY/MM/DDThh:mm:ss)
    worldranking [bool] : true to list competitions that are included in the world ranking list
    division [string] : General/Professional
    status: The status of the competition. Valid values are: PreRegistration, Registering, RegistrationClosed, Processing, Closed, Canceled
    location: The city name where the competition takes/took place.
    '''
    from_date: datetime.date = Field(default=None, serialization_alias='from')
    to_date: datetime.date = Field(default=None, serialization_alias='to')
    modifiedsince: datetime.datetime = None
    worldranking: bool = None
    division: Competition.Division = None
    status: Competition.Status = None
    location: str = None

    @field_serializer('from_date', 'to_date')
    def serialize_date(date: datetime.date):
        if not date: return date
        return date.strftime('%Y/%m/%d')
    
    @field_serializer('modifiedsince')
    def serialize_datetime(dtime: datetime.datetime):
        if not dtime: return dtime
        return dtime.strftime('%Y/%m/%dT%H:%M:%S')
    
    @field_serializer('division', 'status')
    def serialize_enum(value) -> str:
        return str(value.value)

class CoupleQuery(BaseQuery):
    '''Use query parameter to filter by
        
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

    name: str = None
    phonetic: bool = None
    min: int | List[int] | tuple[int, int]
    nameOrMin: str | int = None
    ageGroup: str = None
    # TODO Change to Division(General/Professional)
    division: str = None
    # TODO Change to Status
    status: str = None
    country: str | List[str] = None

    @field_serializer('country')
    def serialize_country(country) -> str:
        if isinstance(country, list):
            return '|'.join(country)
        return country

    @field_serializer('min')
    def serialize_min(min) -> str:
        if isinstance(min, int):
            return str(min)
        if isinstance(min, tuple):
            return '{}+{}'.format(*min)
        if isinstance(min, list):
            return ','.join(map(str, min))
        
class TeamQuery(BaseQuery):
    '''Use query parameter to filter by

    name [string] : list only couples where any member's name starts with this filter's value
    phonetic [bool/optional/default=false] : when true, the name filter is used phonetical instead of litteral.
    '''

    name: str = None
    phonetic: bool = None

class PersonQuery(BaseQuery):
    '''Use query parameter to filter by

    name [string] : list all persons having a name starting with this filter's value. Separate name und surname with a comma(,). The order is not relevant.
    phonetic [bool/optional/default=false] : when true, the name filter is used phonetical instead of litteral.
    min [int] : list person with this MIN (1xxxxxxx can be omitted)
    nameOrMin [string] : list persons having a name or MIN starting with this filter's value
    ageGroup [string] : list persons of an age group (Adult, Senior I, Senior II, Youth, ...)
    division [string] : General/Professional
    type [string,string,...] : list persons of a certain type (Athlete, Adjudicator, Chairman)
    status [string] : list of the person's license status (Active, Retired, Expired, Suspended, Revoked).
    '''

    name: str = None
    phonetic: bool = None
    min: int = None
    nameOrMin: str | int = None
    ageGroup: str = None
    # TODO:
    division: str = None
    # TODO:
    type: str | List[str] = None
    # TODO:
    status: str = None

class RankingQuery(BaseQuery):
    '''Use query paramter to filter by

    ageGroup [string] : the age group (Adult, Senior I, Senior II, Youth, ...)
    discipline [string] : the discipline (Latin, Standard, Ten Dance)
    division [string] : the division (General, Professional)
    form [string] : the dance form (not used yet)
    gender [string] : the gender (Male, Female)
    date [Date/optional] : The date of the ranking list (YYYY/MM/DD)
    limit [int/optional] : Provide only the top x entries
    '''

    ageGroup: str = None
    discipline: str = None
    division: str = None
    # form: str = None
    gender: str = None
    date: datetime.date = None
    limit: int = None