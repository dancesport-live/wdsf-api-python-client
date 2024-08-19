import os
import json
from dotenv import load_dotenv

from wdsf_api.client import WdsfApi

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