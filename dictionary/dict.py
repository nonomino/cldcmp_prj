import sys
import requests

API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"

if len(sys.argv) < 2:
    print("Usage: dict.py <word>")
    sys.exit(1)

word = sys.argv[1]
response = requests.get(API_URL + word)

if response.status_code == 200:
    data = response.json()
    meanings = data[0]["meanings"]
    for meaning in meanings:
        print(f"{meaning['partOfSpeech']}: {meaning['definitions'][0]['definition']}")
else:
    print("Word not found.")

