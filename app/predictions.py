import requests
import pandas as pd
from urllib.parse import urlencode
from io import BytesIO
import random
from datetime import datetime
import config

table = None
time = None


def fetch_table() -> pd.DataFrame:
  base_url = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?'
  final_url = base_url + urlencode(dict(public_key=config.file_url))
  response = requests.get(final_url)
  download_url = response.json()['href']
  download_response = requests.get(download_url)
  return pd.read_excel(BytesIO(download_response.content))


def get_predictions_list() -> list[str]:
  global table
  global time
  now = datetime.now()
  if time is None or abs(time - now) >= config.update_interval:
    table = fetch_table()
    time = datetime.now()
  return table[table.columns[0]].to_list()


def fetch_random_prediction() -> str:
  return random.choice(get_predictions_list())
