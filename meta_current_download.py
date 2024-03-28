import json

file_path = "Wikidatawiki_dumps/urls_wikidatawiki_pages_meta_history_download_list.txt"

with open(file_path, 'r') as file:
    lines = file.readlines()

json_data = {}
for idx, line in enumerate(lines):
    name= line.strip().split(' ')[0]
    json_data[str(idx)] = {"name": name, "download_indicator": 0}


output_json_file = "Wikidatawiki_dumps/urls_wikidatawiki_pages_meta_history_download_list.json"
with open(output_json_file, 'w') as json_file:
    json.dump(json_data, json_file, indent=4)

print(f"JSON 파일이 생성되었습니다: {output_json_file}")
