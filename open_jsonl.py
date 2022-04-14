import json
import jsonlines

'''
predict에 사용할 문서 데이터 처리를 위한 파일
*.jsonl 
    -json line
    -json 내부에 한 줄씩 json을 저장할 수 있는 구조화된 데이터 형식 

'''
output_file = './ou'
data = []
with jsonlines.open('./lawdoc.jsonl') as f, open(output_file, 'w', encoding='utf-8', newline='') as output:
    
    for line in f:
        article = line['article_original']
        # print(article)
        article = ' '.join(article)
        # print(article)
        data.append(article)

# with open(output_file, 'w', encoding='utf-8', newline='') as output:
          
