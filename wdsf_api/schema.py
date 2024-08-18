import datetime
from enum import Enum
from typing import List

from pydantic import BaseModel, ConfigDict, HttpUrl


class Link(BaseModel):
    href: HttpUrl
    rel: str
    type: str = None


class Competition(BaseModel):
    # model_config = ConfigDict(extra='ignore')

    class Status(str, Enum):
        PreRegistration = 'PreRegistration'
        Registering = 'Registering'
        RegistrationClosed = 'RegistrationClosed'
        Processing = 'Processing'
        Closed = 'Closed'
        Canceled = 'Canceled'

    id: int
    name: str = ''
    location: str = ''
    country: str = ''
    type: str = ''
    date: datetime.datetime = None
    age: str = ''
    discipline: str = ''
    # danceform: str
    division: str = ''
    status: Status = None
    coefficient: float = None
    lastModifiedDate: datetime.datetime = None
    eventId: int = None
    groupId: int = None
    link: List[Link] | None


class License(BaseModel):

    class Status(str, Enum):
        Active = 'Active'

    type: str
    status: Status
    division: str
    # disciplines: [str]
    expiresOn: datetime.date


class Person(BaseModel):
    id: int = None
    name: str = ''
    surname: str = ''
    sex: str = ''
    nationality: str = ''
    country: str = ''
    ageGroup: str = ''
    yearOfBirth: int = None
    nationalReference: str = ''
    licenses: List[License] = None


class Participant(BaseModel):
    id: int = None
    number: int = None
    status: str = ''
    basepoints: float = None
    rank: str = None
    competitionId: int = None
    # rounds: ?
    coupleId: str = ''
    name: str = ''
    country: str = ''


class Official(BaseModel):
    id: int = None
    name: str = ''
    country: str = ''
    task: str = ''
    letter: str = ''
    min: int = None
    competitionId: int = None


class Team(BaseModel):
    id: int = None


class Couple(BaseModel):
    id: int = None


class Country(BaseModel):
    name: str