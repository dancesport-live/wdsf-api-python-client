import unittest
import os

from wdsf_api.client import WdsfApi
from wdsf_api.schema import *

class TestWdsfApi(unittest.TestCase):

    def setUp(self) -> None:

        self.client = WdsfApi(
            'production',
            auth=(os.getenv('WDSF_API_USERNAME'), os.getenv('WDSF_API_PASSWORD'))
            )
    
    def test_get_competitions(self):
        data = self.client.get_competitions()
        self.assertIsInstance(data, list)

    def test_get_competitions_filtered(self):
        filters = {
            'from': '2024/08/01',
            'to': '2024/08/31',
            'modifiedsince': '2024/08/13T00:00:00',
            'worldranking': True,
            'division': 'General',
            'status': 'Closed',
            'location': 'Stuttgart'
        }
        data = self.client.get_competitions(**filters)
        print(data)
        self.assertIsInstance(data, list)

    def test_get_competition(self):
        # response, data = self.client.get_competition('61155') # BDF 2024 Sen I
        data = self.client.get_competition('61243') # GOC 2024 Sen I
        self.assertIsInstance(data, Competition)

    def test_get_participants(self):
        data = self.client.get_participants('61243') # GOC 2024 Sen I
        self.assertIsInstance(data, list)

    def test_get_participant(self):
        data = self.client.get_participant('2223702') # Niels Hoppe - Reenste Seidenberg @ GOC 2024 Sen I
        self.assertIsInstance(data, Participant)
    
    def test_get_officials(self):
        data = self.client.get_participants('61243') # GOC 2024 Sen I
        self.assertIsInstance(data, list)

    def test_get_official(self):
        data = self.client.get_official('298565') # Jeffrey Van Meerkerk
        self.assertIsInstance(data, Official)

    def test_get_couples(self):
        data = self.client.get_couples()
        self.assertIsInstance(data, list)

    def test_get_couple(self):
        data = self.client.get_couple('coupleID')
        self.fail('Test incomplete.')

    def test_get_teams(self):
        data = self.client.get_teams()
        self.assertIsInstance(data, list)
    
    def test_get_team(self):
        data = self.client.get_team('teamID')
        self.fail('Test incomplete.')

    def test_get_persons(self):
        data = self.client.get_persons()
        self.assertIsInstance(data, list)

    def test_get_person(self):
        data = self.client.get_person('10069226') # Niels Hoppe
        self.assertIsInstance(data, Person)

    def test_get_ranking(self):
        data = self.client.get_ranking()
        self.fail('Test incomplete.')

    def test_get_countries(self):
        data = self.client.get_countries()
        self.assertIsInstance(data, list)

    def test_get_age(self):
        data = self.client.get_age()
        self.fail('Test incomplete.')

    def test_check_for_competition(self):
        data = self.client.check_for_competition('MIN1', 'MIN2', 'competitionId')
        self.fail('Test incomplete.')