from dotenv import dotenv_values
import requests
import json
from pathlib import Path
from datetime import datetime


config = dotenv_values(".env")
API_KEY = config['API_KEY']
TOKEN = config['TOKEN']
BOARD_ID = config['BOARD_ID']
OUTPUT_DIR = config['OUTPUT_DIR']
OUTPUT_FILEPREFIX = config['OUTPUT_FILEPREFIX']

url = f'https://api.trello.com/1/boards/{BOARD_ID}?key={API_KEY}&token={TOKEN}&fields=all&actions=all&action_fields=all&actions_limit=1000&cards=all&card_fields=all&card_attachments=true&labels=all&lists=all&list_fields=all&members=all&member_fields=all&checklists=all&checklist_fields=all&organization=false&card_pluginData=true&customFields=true&memberships=all&pluginData=true&organization_pluginData=true&myPrefs=true&tags=true'

response = requests.get(url)

if response.status_code == 200:
    board_data = response.json()
    #print(board_data)
else:
    # TODO: status code != 200 -> raise exception
    print(f"Fehler beim Abrufen des Boards. Statuscode: {response.status_code}")
    
actions_url = f'https://api.trello.com/1/boards/{BOARD_ID}/actions?key={API_KEY}&token={TOKEN}&filter=commentCard&limit=1000'
actions_response = requests.get(actions_url)
actions = actions_response.json()
board_data['actions'].extend(actions)

datetime_string = datetime.now().strftime('%Y%m%d%H%M')
outfile = Path(OUTPUT_DIR) / f'{OUTPUT_FILEPREFIX}{datetime_string}.json'
with open(outfile, 'w') as f:
    json.dump(board_data, f, indent=4)
