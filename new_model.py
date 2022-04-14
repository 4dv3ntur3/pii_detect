
'''
지금 이렇게 들어가고 있으니 

model = ElectraForSequenceClassification.from_pretrained("google/electra-small-discriminator", num_labels=num_labels)

'''

# v1, v2의 경우 약 14G Corpus (2.6B tokens)를 사용했습니다. (뉴스, 위키, 나무위키)
# v3의 경우 약 20G의 모두의 말뭉치를 추가적으로 사용했습니다. (신문, 문어, 구어, 메신저, 웹)
# 기존 (v1)
# discriminator = ElectraforPreTraining.from_pretrained("monologg/koelectra-base-discriminator")

# 


discriminator = ElectraForPreTraining.from_pretrained("monologg/koelectra-base-v3-discriminator")
+ 여기에 그냥 classifier 붙여서 모델 구조 만들자......



