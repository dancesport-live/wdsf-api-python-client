from dataclasses import dataclass
import datetime
from typing import List

@dataclass
class Competition:
    id: int = None
    name: str = ''
    location: str = ''
    country: str = ''
    type: str = ''
    date: datetime.datetime = None
    age: str = ''
    discipline: str = ''
    # danceform: str
    division: str = ''
    status: str = ''
    coefficient: float = 0.0
    lastModifiedDate: datetime.datetime = None
    eventId: int = None
    groupId: int = None

@dataclass
class License:
    type: str
    status: str
    division: str
    # disciplines: [str]
    expiresOn: datetime.date

@dataclass
class Person:
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

@dataclass
class Participant:
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

@dataclass
class Official:
    id: int = None
    name: str = ''
    country: str = ''
    task: str = ''
    letter: str = ''
    min: int = None
    competitionId: int = None

@dataclass
class Team:
    id: int = None

@dataclass
class Couple:
    id: int = None