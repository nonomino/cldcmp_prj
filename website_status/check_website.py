import sys
import requests

if len(sys.argv) < 2:
    print("Usage: check_website.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    response = requests.get(url, timeout=5)
    status = "UP" if response.status_code == 200 else f"DOWN ({response.status_code})"
except requests.exceptions.RequestException:
    status = "DOWN (Error)"

print(f"{url} is {status} now.")
