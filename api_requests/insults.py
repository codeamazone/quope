import requests
import json

response = requests.get(
    "https://evilinsult.com/generate_insult.php?lang=en&type=json")
print(response.status_code)
print(response.json())
