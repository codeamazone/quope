import requests
import json
import os

from dotenv import load_dotenv


load_dotenv()


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


url = "https://quotes-inspirational-quotes-motivational-quotes.p.rapidapi.com/quote"

querystring = {"token": "ipworld.info"}

headers = {
    'x-rapidapi-key': os.getenv('x-rapidapi-key'),
    'x-rapidapi-host': "quotes-inspirational-quotes-motivational-quotes.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
response2 = requests.get(f'{url}/?token=ipworld.info', headers=headers)

print(response.text)
print(response2.text)

jprint(response.json())
