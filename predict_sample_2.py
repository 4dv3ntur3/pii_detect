import csv


all_input_tokens = [
    ['서울', '마포구', '월드컵', '##북', '##로', '39', '##6', '누리', '##꿈', '##스', '##퀘어', '비즈니스', '##타', '##워', '6', '##층', '/', '17', '##층', '[SEP]'], 
    ['서울', '마포구', '상암', '##산', '##로', '##1', '##길', '24', '월드컵', '##파크', '4', '##단지', '102', '##동', '210', '##1', '##호', '[SEP]']]

preds_list = [['AD_CITY-I', 'AD_CITY-I', 'AD_ADDRESS-I', 'AD_ADDRESS-I', 'AD_ADDRESS-I', 'AD_ADDRESS-I', 'AD_ADDRESS-I', 'AD_DETAIL-I', 'AD_DETAIL-I', 'AD_DETAIL-I', 'AD_DETAIL-I', 'AD_DETAIL-I', 'AD_DETAIL-I', 'AD_DETAIL-I', 'AD_DETAIL-I', 'AD_DETAIL-I', 'AD_DETAIL-I', 'AD_DETAIL-I', 'AD_DETAIL-I'], 
              ['AD_CITY-I', 'AD_CITY-I', 'AD_ADDRESS-B', 'AD_ADDRESS-I', 'AD_ADDRESS-I', 'AD_DETAIL-I', 'AD_ADDRESS-I', 'AD_DETAIL-I', 'AD_DETAIL-I', 'AD_DETAIL-I', 'AD_DETAIL-I', 'AD_DETAIL-I', 'AD_DETAIL-I', 'AD_DETAIL-I', 'AD_DETAIL-I', 'AD_DETAIL-I', 'AD_DETAIL-I']]


all_input_tokens = [['010', '-', '236', '##9', '-', '47', '##89', '##로', '연락', '##주', '##세요', '.', '[SEP]']]
preds_list = [['ID_PHONE-I', 'ID_PHONE-I', 'ID_PHONE-I', 'ID_PHONE-I', 'ID_PHONE-I', 'ID_PHONE-I', 'ID_PHONE-I', 'O', 'O', 'O', 'O', 'O']]



# len_toks_f = len(all_input_tokens[0]) # 20 
# len_preds_f = len(preds_list[0])  # 19
# len_toks_s = len(all_input_tokens[1]) # 18
# len_preds_s = len(preds_list[1]) #17


# Write to output file
with open('./sample.txt', "w", encoding="utf-8") as f:
    for words, preds in zip(all_input_tokens, preds_list):
        
        line = ""
        labels = []
        words = []
        
        ahead_tag = ""
        ahead_sen = ""
        pii_word = ""
        
        for i, (word, pred) in enumerate(zip(words, preds)):
            
            # 단어에 #이 있으면 이전 라벨과 비교한다 
            # word: 이전 토큰의 라벨과 동일하면 pii_word에 합치고, 아니라면 합치지 않는다 
            # label: pii_word에 들어오는 가장 첫 토큰의 라벨로 한다. 

            if '#' in word:
                
                if pred == ahead_tag:
                    pii_word += word
                    
                else:
                    line = line + word + " "
                    pii = ""
                    
                    
            else:
                if pred == ahead_tag:
                    pii_word += word
                    
                else:
                    line = line + word + " "
                    pii = ""
                    
        
        
        
            ahead_sen = word
            ahead_tag = pred
            
                  
        f.write("{}\n".format(line.strip()))
        