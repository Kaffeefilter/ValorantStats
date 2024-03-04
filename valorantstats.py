import requests
import json

resp = requests.get('https://api.henrikdev.xyz/valorant/v1/account/Pfannkuchen/80085?force=true')
account = resp.json()
resp = requests.get('https://api.henrikdev.xyz/valorant/v1/by-puuid/lifetime/matches/eu/'+account['data']['puuid'])
#print(resp.status_code)
if resp.status_code == 200:
    lifetime = resp.json()
    print(len(lifetime['data']))
    with open("data.json", "w") as json_file:
        json.dump(lifetime, json_file, sort_keys=True, indent=4)

resp = requests.get('https://api.henrikdev.xyz/valorant/v1/by-puuid/lifetime/matches/eu/'+account['data']['puuid']+'?mode=competitive')
comp = resp.json()
resp = requests.get('https://api.henrikdev.xyz/valorant/v1/by-puuid/lifetime/matches/eu/'+account['data']['puuid']+'?mode=unrated')
unrated = resp.json()
print(len(comp['data']))
print(len(unrated['data']))

if __name__ == '__main__':
    pass