import unittest
import pathlib

from wdsf_api.parser import Parser
from wdsf_api.types import Competition, Person


class TestWithDataFile(unittest.TestCase):

    def setUp(self) -> None:
        path = pathlib.Path(__file__).parent.parent.joinpath(self.DATA_FILE)
        self.testFile = open(path)

    def tearDown(self) -> None:
        self.testFile.close()


class TestParserPerson(TestWithDataFile):

    DATA_FILE = 'data/person.xml'

    def test_parse_person(self):
        person = Parser.parse_person(self.testFile.read())
        self.assertIsInstance(person, Person)


class TestParserCompetition(TestWithDataFile):

    DATA_FILE = 'data/competition.xml'

    def test_parse_competition(self):
        competition = Parser.parse_competition(self.testFile.read())
        self.assertIsInstance(competition, Competition)