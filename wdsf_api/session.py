import requests

class Session(requests.Session):

    def __init__(self, *args, **kwargs) -> None:
        
        super(Session, self).__init__(*args, **kwargs)

        self.headers.update({
            'User-Agent': 'WDSF API Python Client',
            'Content-Type': 'application/vnd.worlddancesport.couples+xml',
            'Accept': 'application/xml',
            # 'X-OnBehalfOd': '',
        })

    def init_basic_auth(self, username, password):
        self.auth = (username, password)