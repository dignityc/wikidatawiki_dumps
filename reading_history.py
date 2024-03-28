import py7zr
from lxml import etree as ET

"""
file_path = "wikidatawiki-20240201-pages-meta-history1.xml-p1p154.7z"

# Step 1: Extract the .7z file
with py7zr.SevenZipFile(file_path, mode='r') as z:
    z.extractall(path="extracted")
"""

xml_file_path = "extracted/wikidatawiki-20240201-pages-meta-history1.xml-p1p154"
start_line = 10000
end_line = 30000

with open(xml_file_path, "r") as f:
    for i, line in enumerate(f):
        if start_line <= i < end_line:
            print(line.strip())
        elif i >= end_line:
            break

