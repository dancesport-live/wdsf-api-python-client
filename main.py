import os
import json
from dotenv import load_dotenv

from wdsf_api.client import WdsfApi
from wdsf_api.schema import Competition

if __name__ == '__main__':
    load_dotenv()
    client = WdsfApi(
        'production',
        auth=(os.getenv('WDSF_API_USERNAME'), os.getenv('WDSF_API_PASSWORD'))
        )
    # data = client.get_competition(competition_id=61243)
    # data = client.get_officials(competition_id=61243)
    # data = client.get_participant(participant_id=2223702)
    # print(data)
    with open('data/competition.json') as file:
        data = json.loads(file.read())
        comp = Competition(**data)
        print(comp)