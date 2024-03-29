import json
import requests
from tqdm import tqdm
import argparse

parser = argparse.ArgumentParser(description='Starting point for download threads')

parser.add_argument('st_idx', type=int, help='index of starting id of download list')
args = parser.parse_args()

st_idx = args.st_idx

file_path = 'urls_wikidatawiki_pages_meta_history_download_list.json'

with open(file_path, 'r') as json_file:
    data = json.load(json_file)

def download_progress(response, file_size, file, chunk_size=1024):
    progress_bar = tqdm(total=file_size, unit='B', unit_scale=True)
    for chunk in response.iter_content(chunk_size=chunk_size):
        if chunk:
            file.write(chunk)
            progress_bar.update(len(chunk))
    progress_bar.close()

for id in list(data.keys())[st_idx:]:
    if data[id]['download_indicator'] != 1:
        download_url = f"https://dumps.wikimedia.org/wikidatawiki/20240201/{data[id]['name']}"
        download_location = f"meta_history/downloaded/{data[id]['name']}"
        response = requests.get(download_url, stream=True)
        file_size = int(response.headers.get('content-length', 0))
        with open(download_location, 'wb') as file:
            download_progress(response, file_size, file)
        data[id]['download_indicator'] = 1
        print(f'id:{id}, download completion!')
    else:
        print(f'id:{id}, already downloaded')
    