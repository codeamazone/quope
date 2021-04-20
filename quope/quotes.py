import requests
import json


def get_quote():
    resp = requests.get(
        'http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en')
    try:
        # resp.status_code == 200:
        quote = resp.json()['quoteText']
        return quote
    except Exception:
        return 'Something went wrong'


if __name__ == '__main__':
    print(get_quote())
