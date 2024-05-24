import requests

from exceptions import InvalidApiRequestError


NBRB_API_URL = 'https://www.nbrb.by/api/exrates/rates'


def get_currency_rates_by_date(date):
    try:
        response = requests.get(f'{NBRB_API_URL}?ondate={date}&periodicity=0')
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        raise InvalidApiRequestError


def get_currency_rate_by_date_and_code(date, currency_code):
    try:
        response = requests.get(f'{NBRB_API_URL}/{currency_code}?ondate={date}')
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        raise InvalidApiRequestError
