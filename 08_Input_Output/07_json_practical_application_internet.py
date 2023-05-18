import json
import requests

url = "https://www.ncdc.noaa.gov/cag/global/time-series/globe/land_ocean/1/7/1880-2021/data.json"

response = requests.get(url=url)

if response.status_code == 200:
    data = response.json()
    print(json.dumps(data, indent=4, sort_keys=False))
else:
    print("Error:", response.status_code)
