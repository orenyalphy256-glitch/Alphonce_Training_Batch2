# Bravo_day24_requests_adv.py
import requests

url = "https://httpbin.org/get"
params = {"q": "python", "page": 1}
headers = {"User-Agent": "my-app/0.0.1"}

r = requests.get(url, params=params, headers=headers, timeout=10)
print("URL requested:", r.url)
print("Status code:", r.status_code)
print("Response keys:", list(r.json().keys()))