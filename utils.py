import pandas as pd
import csv

# from check_dataset import anomal_check
#이 파일을 가지고 check_dataset에서 import를 하니 circular 에러가 뜨지 

'''
여태 만든 코드들 취합? 
import해서 main에서 불러다 쓸 수 있게... 
(추후 작업)
'''


def replace_tag(df, output_path):
    
    df = pd.read_csv(df, sep='\t', encoding='utf-8', names=['SEN', 'TAG'])
    
    with open(output_path, 'w', newline='', encoding='utf-8') as output:
        
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
            
def anomal_check(df):
    counter = 0
    for i in range(len(df)):
        row = df.iloc[i]
        sen = row['SEN']
        tag = row['TAG']
        
        sen_ = sen.split(' ')
        tag_ = tag.split(' ')
        
        if len(sen_) == len(tag_):
            continue
        else:
            print(sen_)
            print(tag_)
            counter += 1
    
    print(counter)
    print("=============")


def split_train_test(df, train_path, test_path):
    
    df = df.sample(frac=1).reset_index(drop=True)  # shuffling하고 index reset
    train_len = int(len(df)*0.8)

    total_train = df[:train_len]
    total_test = df[train_len:]
    
    print("total file anomal check...")
    anomal_check(df)

    print("total: " + str(len(df)))
    print("train: " + str(len(total_train)))
    print("test: " + str(len(total_test)))

    total_train.to_csv(train_path, sep='\t', na_rep='NaN', index=False, header=False)
    total_test.to_csv(test_path, sep='\t', na_rep='NaN', index=False, header=False)
    
def assert_num_toks(df):
    df = pd.read_csv(df, sep='\t', encoding='utf-8', names=['SEN', 'TAG'])

    for rows in range(len(df)):
        row = df.iloc[rows] # df[rows]는 안 됨... 이건 column명으로 
        sen = row['SEN'].strip() # 앞이나 뒤에 공백이 있으면 그 공백도 들어감...
        tag = row['TAG'].strip()
        
        sens = sen.split(' ')
        tags = tag.split(' ')
        
        sen_len = len(sens)
        tag_len = len(tags)
        
        if (sen_len != tag_len):
            
            print(sen)
            print(tag)
            print(sen_len)
            print(tag_len)
    
    print("complete!")
    
def main():
    # path = './data/model_train_data/only_address/data_added_20220322_before_split.tsv'
    # output = './address_only_with_o.tsv'
    
    # replace_tag(path, output)
    
    # temp = pd.read_csv(output, sep='\t', encoding='utf-8', names=['SEN', 'TAG'])
    # split_train_test(temp, './train.tsv', './test.tsv')

    # label_add = []
    # label_wholee = []
    
    # with open('./label.txt', 'r', encoding='utf-8') as label_ad, open('./label_whole.txt', 'r', encoding='utf-8') as label_whole:
        
    #     while True:
    #         line_ad = label_ad.readline()
    #         line_whole = label_whole.readline()
            
    #         label_add.append(line_ad)
    #         label_wholee.append(line_whole)
            
    #         if (not line_ad) and (not line_whole): break
            
    #     print(label_wholee)
    #     print(label_add)
        
    #     # for i in range(len(label_wholee)):
    #     #     if i != 0:
    #     #         if i % 2 == 1:
    #     #             print(label_wholee[i])
                
    #     for j in range(len(label_add)):
    #         if j != 0:
    #             if j % 2 == 1:
    #                 print(label_add[j])
    
    

    # label_ids = []
    # word_tokens = ["400", "##2", "##호", "##요", "."]
    # tags = ["AD_I"]
    # slot_label = 4
    
    # if slot_label == 0 or slot_label == 1:
    #     next_label = slot_label
    # else:
    #     if slot_label % 2 == 0:
    #         next_label = slot_label + 1 
    #     elif slot_label % 2 == 1:
    #         next_label = slot_label

    # label_ids.extend([int(slot_label)] + [next_label] * (len(word_tokens) - 1))
                

    # print(label_ids)
    path = 'C:\\Users\\ejpark\\Desktop\\I_want_PII_NER\\res\\AD_METRO_applied.tsv'
    # assert_num_toks(path)
    
    # a = 'a b c'
    # a = a.strip("a""c").strip()
    # print(a)
    # print(len(a))

    assert_num_toks(path)
    
        
if __name__ == "__main__":
    main()