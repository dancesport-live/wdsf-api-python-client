import unittest
import os

from wdsf_api.client import Client
from wdsf_api.types import Competition, Official, Participant, Person

class TestClient(unittest.TestCase):

    def setUp(self) -> None:

        self.client = Client(
            os.getenv('WDSF_API_USERNAME'),
            os.getenv('WDSF_API_PASSWORD'),
            raise_for_status=True
            )
    
    def test_get_competitions(self):
        response, data = self.client.get_competitions()
        self.fail('Test incomplete.')

    def test_get_competition(self):
        # response, data = self.client.get_competition('61155') # BDF 2024 Sen I
        response, data = self.client.get_competition('61243') # GOC 2024 Sen I
        self.assertIsInstance(data, Competition)

    def test_get_participants(self):
        response, data = self.client.get_participants('61243') # GOC 2024 Sen I
        self.fail('Test incomplete.')

    def test_get_participant(self):
        _, data = self.client.get_participant('2223702') # Niels Hoppe - Reenste Seidenberg @ GOC 2024 Sen I
        self.assertIsInstance(data, Participant)
    
    def test_get_officials(self):
        response, data = self.client.get_participants('61243') # GOC 2024 Sen I
        self.fail('Test incomplete.')

    def test_get_official(self):
        _, data = self.client.get_official('298565') # Jeffrey Van Meerkerk
        self.assertIsInstance(data, Official)

    def test_get_couples(self):
        self.fail('Not implemented.')

    def test_get_couple(self):
        self.fail('Not implemented.')

    def test_get_teams(self):
        self.fail('Not implemented.')
    
    def test_get_team(self):
        self.fail('Not implemented.')

    def test_get_persons(self):
        self.fail('Not implemented.')

    def test_get_person(self):
        response, data = self.client.get_person('10069226') # Niels Hoppe
        self.assertIsInstance(data, Person)