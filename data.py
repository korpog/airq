import requests
import csv
import os

# set API key from OpenAQ as your env variable
env_var = os.getenv("API_VAR")
API_KEY = env_var
api_call="https://api.openaq.org/v2/measurements?location_id=6386&parameter=o3&parameter=so2&parameter=no2&parameter=pm25&parameter=pm10&date_from=2023-07-01T02:00:00+02:00&date_to=2023-07-31T02:00:00+02:00&limit=3"

res = requests.get(api_call, headers={"X-API-Key": API_KEY})
results = res.json()['results']

with open("wokalna.csv", "w") as f:
    w = csv.DictWriter(f, results[0].keys())
    w.writeheader()
    w.writerows(results)