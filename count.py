import pandas as pd



train = pd.read_csv('./train_final.tsv', sep='\t', names=['SEN', 'TAG'])

tag = train['TAG']

# counting number of tokens 
whole_count = 0
address_count = 0

metro = 0
city = 0
addr = 0
brand = 0
detail = 0

for i in range(len(tag)):
    tags = tag[i]
    tag_ = tags.split(' ')
    whole_count += len(tag_)
    

print(whole_count)
