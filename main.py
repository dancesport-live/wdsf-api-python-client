import os
from dotenv import load_dotenv

from wdsf_api.client import Client

if __name__ == '__main__':
    load_dotenv()
    client = Client(
        os.getenv('WDSF_API_USERNAME'),
        os.getenv('WDSF_API_PASSWORD'),
        raise_for_status=True,
        )
    # response = client.get('official', params={ 'competitionId': '61243' })
    # response = client.get('participant/2223702')
    response, data = client.get_participant('2196135')
    print(response.text)