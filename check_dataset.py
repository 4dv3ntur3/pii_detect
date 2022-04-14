
import pandas as pd

'''
아무래도 덮어쓰고 업로드하고 하면서 잘 돌아가던 train, test 파일들이 깨진 듯...
다시 제작

'''

from utils import split_train_test, replace_tag

# train_whole = pd.read_csv('./whole_with_o_tags/train.tsv', sep='\t', names=['SEN', 'TAG'])
# test_whole = pd.read_csv('./whole_with_o_tags/test.tsv', sep='\t', names=['SEN', 'TAG'])

# train_addr = pd.read_csv('./address_only/train.tsv', sep='\t', names=['SEN', 'TAG'])
# test_addr = pd.read_csv('./address_only/test.tsv', sep='\t', names=['SEN', 'TAG'])

# t = pd.read_csv('./data/model_train_data/data_added_20220322_train.tsv', sep='\t', names=['SEN', 'TAG'])
# te = pd.read_csv('./data/model_train_data/data_added_20220322_test.tsv', sep='\t', names=['SEN', 'TAG'])
# b = pd.read_csv('./data/model_train_data/data_added_20220322_before_split.tsv', sep='\t', names=['SEN', 'TAG'])



output_path = './ner_for_train_origin_with_Os.tsv'
whole = pd.read_csv(output_path, delimiter='\t', names=['SEN', 'TAG'])

# replace_tag(whole, output_path=output_path)



train_path = './ner_for_train_origin_train_with_o.tsv'
test_path = './ner_for_train_origin_test_with_o.tsv'




split_train_test(whole, train_path=train_path, test_path=test_path)




