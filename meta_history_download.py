import json
import requests
import os
from tqdm import tqdm

file_path = 'urls_wikidatawiki_pages_meta_history_download_list.json'

with open(file_path, 'r') as json_file:
    data = json.load(json_file)

def json_save(data, file_path):
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)


def download_progress(response, file_size, file, chunk_size=1024):
    progress_bar = tqdm(total=file_size, unit='B', unit_scale=True)
    for chunk in response.iter_content(chunk_size=chunk_size):
        if chunk:
            file.write(chunk)
            progress_bar.update(len(chunk))
    progress_bar.close()

for id in data.keys():
    if data[id]['download_indicator'] != 1:
        download_url = f"https://dumps.wikimedia.org/wikidatawiki/20240201/{data[id]['name']}"
        download_location = f"Wikidatawiki_dumps/meta_history/downloaded/{data[id]['name']}"
        response = requests.get(download_url, stream=True)
        file_size = int(response.headers.get('content-length', 0))
        with open(download_location, 'wb') as file:
            download_progress(response, file_size, file)
        data[id]['download_indicator'] = 1
        print(f'id:{id}, download completion!')
        json_save(data, file_path)
    else:
        print(f'id:{id}, already downloaded')
    