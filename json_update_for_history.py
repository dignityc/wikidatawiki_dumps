import json

with open('urls_wikidatawiki_pages_meta_history_download_list.json', 'r') as file:
    json_data = json.load(file)

text_df = []
for i in range(1,5):
    with open(f'download_log-{i}.out', 'r') as file:
        for line in file: 
            if 'id:' in line.strip():
                text_df.append(line.strip())

for t in text_df:
    json_data[t.split(',')[0].split(':')[1]]['download_indicator'] = 1

with open('urls_wikidatawiki_pages_meta_history_download_list.json', 'w') as file:
    json.dump(json_data, file)