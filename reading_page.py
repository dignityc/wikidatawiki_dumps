import bz2



with bz2.open('wikidatawiki-20240201-pages-meta-current1.xml-p1p441397.bz2', 'rt', encoding='utf-8') as f:
    for _ in range(500):
        line = f.readline()
        print(line.strip())  # 각 라인 출력



from lxml import etree as ET
import bz2
import shutil

xml_file_path = "wikidatawiki-20240201-pages-meta-current1.xml-p1p441397.bz2"
uncompressed_file_path = "uncompressed.xml"

with bz2.open(xml_file_path, "rb") as f_in, open(uncompressed_file_path, "wb") as f_out:
    shutil.copyfileobj(f_in, f_out)

print("File uncompressed successfully:", uncompressed_file_path)


from lxml import etree as ET
uncompressed_file_path = "uncompressed.xml"
# lxml을 사용하여 XML 파일을 파싱
tree = ET.parse(uncompressed_file_path)
root = tree.getroot()

ns_elements = root.findall(".//ns[.='5']")


# 찾은 요소들의 부모 요소를 리스트에 저장
target_parents = [elem.getparent() for elem in target_elements]

# 결과 확인
for parent in target_parents:
    print(ET.tostring(parent, pretty_print=True).decode())


########### Screening
def read_lines(file_path):
    with open(file_path, "r") as f:
        for line in f:
            yield line.strip()
i = 0
for line in read_lines(uncompressed_file_path):
    # 여기서 필요한 작업 수행
    if '<ns>5</ns>' in line:
        print(line)
    else:
        print(line)
    i += 1
    if i == 1000:
        break