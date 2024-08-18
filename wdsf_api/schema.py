import datetime
from enum import Enum
from typing import Any, List

from pydantic import AliasChoices, BaseModel, Field, HttpUrl


class Link(BaseModel):
    href: HttpUrl
    rel: str
    type: str = None


class Competition(BaseModel):

    class Status(str, Enum):
        PreRegistration = 'PreRegistration'
        Registering = 'Registering'
        RegistrationClosed = 'RegistrationClosed'
        Processing = 'Processing'
        Closed = 'Closed'
        Canceled = 'Canceled'
    
    class Division(str, Enum):
        General = 'General'
        Professional = 'Professional'

    id: int
    name: str = ''
    location: str = ''
    country: str = ''
    type: str = ''
    date: datetime.datetime = None
    age: str = ''
    discipline: str = ''
    # danceform: str
    division: Division = None
    status: Status = None
    coefficient: float = None
    lastModifiedDate: datetime.datetime = None
    eventId: int = None
    groupId: int = None
    link: List[Link] | None


class License(BaseModel):

    class Status(str, Enum):
        Active = 'Active'
        Retired = 'Retired'
        Expired = 'Expired'
        Suspended = 'Suspended'
        Revoked = 'Revoked'

    type: str
    status: Status
    division: str
    # disciplines: [str]
    expiresOn: datetime.date


class Person(BaseModel):
    id: int
    name: str = ''
    surname: str = ''
    sex: str = ''
    nationality: str = ''
    country: str = ''
    ageGroup: str = ''
    yearOfBirth: int = None
    nationalReference: str = ''
    licenses: List[License] = None


class MarkScore(BaseModel):
    kind: str # 'mark'
    adjudicator: int
    link: List[Link]
    set: bool = None


class FinalScore(BaseModel):
    rank: int
    kind: str # 'final'
    adjudicator: int
    link: List[Link]


class Dance(BaseModel):
    name: str
    isGroupDance: bool # what is this?
    scores: List[MarkScore] | List[FinalScore]


class Round(BaseModel):
    name: str
    maxDeviation: Any # what is this?
    dances: List[Dance]


class Participant(BaseModel):

    class Status(str, Enum):
        Present = 'Present'
        Excused = 'Excused'

    id: int
    status: Status
    number: int = None
    basepoints: float = None
    rank: str = None
    competitionId: int = None
    rounds:  List[Round] = None
    coupleId: str = ''
    name: str = ''
    country: str = ''


class Official(BaseModel):
    link: List[Link]
    id: int = Field(validation_alias=AliasChoices('id', 'Id'))
    name: str = Field(validation_alias=AliasChoices('name', 'Name'))
    country: str
    task: str = None
    letter: str = None
    min: int = None
    competitionId: int = None


class Team(BaseModel):
    id: int


class Couple(BaseModel):
    id: int


class Country(BaseModel):
    name: str