import pandas as pd

a = pd.read_csv('./data/ner_dataset_original.tsv', delimiter='\t', encoding='utf-8', header=None)

# print(a.describe)

print(a)
cut = a[16418:]

cut.to_csv('./ner_20220701.tsv', sep='\t', encoding='utf-8', header=False,)


