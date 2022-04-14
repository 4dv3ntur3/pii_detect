import json
import csv





file_path = 'C:\\Users\\ejpark\\Desktop\\pii_detect\\민원(콜센터) 질의-응답 데이터_text\\Training\\쇼핑\\민원(콜센터) 질의응답_K쇼핑_결제_Training.json'
output_file = './'

data = []

with open(file_path, encoding="utf-8") as json_file, open(output_file, 'w', newline = '', encoding='utf-8') as output:
    json_data = json.load(json_file)
    
    f = csv.writer(output)
    f.writerow(['고객질문(요청)', '상담사질문(요청)', '고객답변', '상담사답변'])
    for datalow in json_data:        
        f.writerow([datalow['고객질문(요청)'], datalow['상담사질문(요청)'], datalow['고객답변'], datalow['상담사답변']])