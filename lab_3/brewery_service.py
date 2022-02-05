from argparse import ArgumentParser
from brewery import Brewery
from requests import get

parser = ArgumentParser()
parser.add_argument('--city', nargs='?', default='empty')
args = parser.parse_args()

url = 'https://api.openbrewerydb.org/breweries'
default_params = {'per_page': '20'}


def get_breweries() -> list[Brewery]:
    response = get(url, get_params())
    return [Brewery(**b) for b in response.json()]


def get_params() -> dict[str, str]:
    params = default_params
    if args.city != 'empty':
        params['by_city'] = args.city
    return params


# ex 7 & 8
[print(b) for b in get_breweries()]
