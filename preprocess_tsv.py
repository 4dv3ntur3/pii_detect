import json
import csv
import pandas as pd
import json


path = './tsv_without_O_tag/shopping_주문_training.tsv'
output_file = './shopping_주문_training_with_o_tag.tsv'


# csv__ = pd.read_csv(output_file, delimiter='\t', encoding='utf-8', names=['SENTENCE', 'TAG'])

# print(csv__.head())

'''
문장 데이터만 추출한 tsv 파일 전처리
문장 내 중복 공백 제거, 시작과 끝 부분의 공백 제거 후 O 태그 사전에 붙이기 -> 추후 필요한 자리의 태그만 수정해서 사용할 수 있도록 
'''

csv__ = pd.read_csv(path, delimiter='\t', engine='python', encoding='utf-8', names=['SENTENCE'])

def writedata(aaa, f):
    aaa = aaa.strip()
    aaa = ' '.join(aaa.split()) # 다중 공백 제거 
    a = len(aaa.split(' ')) - 1 # O 길이
    f.writerow([aaa, 'O '*a + 'O'])
    # f.writerow([aaa]) # O 태그 없이 그냥 문장만 추출

with open(output_file, 'w', newline='', encoding='utf-8') as output:
    
    lines = csv__['SENTENCE']
  
    f = csv.writer(output, delimiter='\t')
    
    for line in lines:
        if line:
            writedata(line, f)
            
            
            
            
            

'''
# 토큰


'''

# file_path = 'C:\\Users\\ejpark\\Desktop\\pii_detect\\민원(콜센터) 질의-응답 데이터_text\\Training\\쇼핑\\민원(콜센터) 질의응답_K쇼핑_결제_Training.json'
# output_file = './shopping_pay_training.tsv'

# data = []

# with open(file_path, encoding="utf-8") as json_file, open(output_file, 'w', newline = '', encoding='utf-8') as output:
#     json_data = json.load(json_file)
    
#     f = csv.writer(output)
#     f.writerow(['고객질문(요청)', '상담사질문(요청)', '고객답변', '상담사답변'])
#     for datalow in json_data:        
#         f.writerow([datalow['고객질문(요청)'], datalow['상담사질문(요청)'], datalow['고객답변'], datalow['상담사답변']])