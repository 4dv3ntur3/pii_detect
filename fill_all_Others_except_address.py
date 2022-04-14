from dataclasses import replace
import pandas as pd
import csv

# 내가 만든 python file의 함수 
from check_dataset import anomal_check

origin = pd.read_csv('C:\\Users\\ejpark\\Desktop\\pii_detect\\data\\model_train_data\\ner_for_train_origin.tsv', sep='\t', names=['SEN', 'TAG'])

'''
print(len(origin)) # 5594
anomal_check(origin) # 0 -> ok!
'''

path = 'C:\\Users\\ejpark\\Desktop\\pii_detect\\all_other_except_address.tsv'



# test = pd.read_csv(path, sep='\t', names=['SEN', 'TAG'])
# anomal_check(test)

def replace_tag(df):
    
    with open(path, 'w', newline='', encoding='utf-8') as output:
        
        f = csv.writer(output, delimiter='\t')

        for i in range(len(df)):
            row = df.iloc[i]
            
            sen = row['SEN']
            tag = row['TAG']
            tag_ = tag.split(' ')
            
            temp_tag = []
            tag_list = ['AD_ADDRESS-B', 'AD_ADDRESS-I', 'AD_DETAIL-B', 'AD_DETAIL-I']
            
            for i in range(len(tag_)):
                t = tag_[i]
                
                if t in tag_list:
                    pass
                
                else:
                    t = 'O'
                    
                temp_tag.append(t)
                
            new_tag = ' '.join(temp_tag)
            f.writerow([sen, new_tag])
            

'''
역대급 멍청이짓..
함수로 정의해 놓고 함수 호출을 안 했네 
'''
# replace_tag(origin)

# result = pd.read_csv(path, sep='\t', names=['SEN', 'TAG'])

# anomal_check(result) # 0 



result = pd.read_csv(path, sep='\t', names=['SEN', 'TAG'])
train_path = './whole_with_o_tags_train.tsv'
test_path = './whole_with_o_tags_test.tsv'

def split(df):
    train_len = int(len(df)*0.8)

    total_train = df[:train_len]
    total_test = df[train_len:]
    
    print(len(total_test)) # 1119 
    print(len(total_train)) # 4475
    

    total_train.to_csv(train_path, sep='\t', na_rep='NaN', index=False, header=False)
    total_test.to_csv(test_path, sep='\t', na_rep='NaN', index=False, header=False)
    
def main():
    split(result)
    
if __name__ == '__main__':
    main()