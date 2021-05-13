import requests
import json
import sqlite3

country = "Spain"
leagues = []
url_league = f"https://v3.football.api-sports.io/leagues?country={country}"
headers = {
    'x-rapidapi-key': 'eee4420166452f446cbf18c105c6b4e0',
    'x-rapidapi-host': 'v3.football.api-sports.io'
}

league_id = requests.get(url_league, headers=headers).text
league_id = json.loads(league_id)

file = open('leagues.json', 'w')
file.write(str(league_id))
file.close()

for i in range(len(league_id['response'])):
    leagues.append(league_id['response'][i]['league']['name'])

conn = sqlite3.connect('my_database.sqlite')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE leagues
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(70));''')

for league in leagues:
    cursor.execute('INSERT INTO leagues (name) VALUES (?)', (league,))

conn.close()

print(leagues)
