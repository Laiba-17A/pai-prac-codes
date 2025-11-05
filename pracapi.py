
import requests

BASE_URL = "https://api.cricapi.com/v1/matches?apikey=c26f8213-c725-4ccc-b671-c2a1cc413a06&offset=0"

response = requests.get(BASE_URL)

if response.status_code == 200:
    data = response.json()
    for match in data.get('data', [])[:5]:  #limit to first 5 matches
        name=match.get('name','unknown match')
        status=match.get('status','no status available')
        print(f"Match: {name}, Status: {status}")

else:
    print(f"Error: Unable to fetch data, status code {response.status_code}")

#save data to a file
with open('matches_data.json', 'w') as f:
    import json
    json.dump(data, f, indent=4)