import json

file_path = 'urls_wikidatawiki_pages_meta_history_download_list.json'

with open(file_path, 'r') as json_file:
    data = json.load(json_file)

def json_save(data, file_path):
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

for id in data.keys():
    data[id]['download_indicator'] = 0
    json_save(data, file_path)