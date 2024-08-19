# WDSF API Python Client (unofficial)

[![PyPI](https://img.shields.io/pypi/v/wdsf-api)](https://pypi.org/project/wdsf-api/)
[![Documentation Status](https://readthedocs.org/projects/wdsf-api-python-client/badge/?version=latest)](https://wdsf-api-python-client.readthedocs.io/en/latest/?badge=latest)
[![Apache 2.0 License](https://img.shields.io/github/license/dancesport-live/wdsf-api-python-client)](https://apache.org/licenses/LICENSE-2.0)
[![CodeFactor](https://www.codefactor.io/repository/github/dancesport-live/wdsf-api-python-client/badge)](https://www.codefactor.io/repository/github/dancesport-live/wdsf-api-python-client)


This is an unofficial Python client for the public API of the World DanceSport Federation (WDSF).
Original documentation for the API can be found [here](https://github.com/jaykay-design/WDSF-API/).

The client is based on [Uplink](https://uplink.readthedocs.io) and uses [Pydantic](https://docs.pydantic.dev) for (de-)serialization and validation.

**This project is under active development.**
**Breaking changes must be expected for all `0.0.X` versions.**


## Installation and Usage

You can install this library from the [Python Package Index](https://pypi.org/project/wdsf-api/):

    pip install wdsf-api

You can then create a new client and make a request:

```{python}
from wdsf_api.client import WdsfApi

client = WdsfApi(
    environment='production',
    auth=('WDSF_API_USERNAME', 'WDSF_API_PASSWORD')
    )

competition = client.get_competition(competition_id=61243)
```

## Documentation

Coming. Will be published on [Read the Docs](https://wdsf-api-python-client.readthedocs.io/en/latest/).


## License and Disclaimer

The WDSF API Python Client is open source software provided under the [Apache License 2.0](https://apache.org/licenses/LICENSE-2.0).

The project is not affiliated, associated, authorized, endorsed by, or in any way officially connected with the World DanceSport Federation,
or any of its subsidiaries or its affiliates.

The names World DanceSport Federation as well as related names, marks, emblems and images are registered trademarks of their respective owners.