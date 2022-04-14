import csv


# all_input_tokens = [
#     ['서울', '마포구', '월드컵', '##북', '##로', '39', '##6', '누리', '##꿈', '##스', '##퀘어', '비즈니스', '##타', '##워', '6', '##층', '/', '17', '##층', '[SEP]'], 
#     ['서울', '마포구', '상암', '##산', '##로', '##1', '##길', '24', '월드컵', '##파크', '4', '##단지', '102', '##동', '210', '##1', '##호', '[SEP]']]

# preds_list = [['AD_CITY-I', 'AD_CITY-I', 'AD_ADDRESS-I', 'AD_ADDRESS-I', 'AD_ADDRESS-I', 'AD_ADDRESS-I', 'AD_ADDRESS-I', 'AD_DETAIL-I', 'AD_DETAIL-I', 'AD_DETAIL-I', 'AD_DETAIL-I', 'AD_DETAIL-I', 'AD_DETAIL-I', 'AD_DETAIL-I', 'AD_DETAIL-I', 'AD_DETAIL-I', 'AD_DETAIL-I', 'AD_DETAIL-I', 'AD_DETAIL-I'], 
#               ['AD_CITY-I', 'AD_CITY-I', 'AD_ADDRESS-B', 'AD_ADDRESS-I', 'AD_ADDRESS-I', 'AD_DETAIL-I', 'AD_ADDRESS-I', 'AD_DETAIL-I', 'AD_DETAIL-I', 'AD_DETAIL-I', 'AD_DETAIL-I', 'AD_DETAIL-I', 'AD_DETAIL-I', 'AD_DETAIL-I', 'AD_DETAIL-I', 'AD_DETAIL-I', 'AD_DETAIL-I']]


all_input_tokens = [['010', '-', '236', '##9', '-', '47', '##89', '##로', '연락', '##주', '##세요', '.', '[SEP]']]
preds_list = [['ID_PHONE-I', 'ID_PHONE-I', 'ID_PHONE-I', 'ID_PHONE-I', 'ID_PHONE-I', 'ID_PHONE-I', 'ID_PHONE-I', 'O', 'O', 'O', 'O', 'O']]



# len_toks_f = len(all_input_tokens[0]) # 20 
# len_preds_f = len(preds_list[0])  # 19
# len_toks_s = len(all_input_tokens[1]) # 18
# len_preds_s = len(preds_list[1]) #17


# Write to output file
with open('./sample.txt', "w", encoding="utf-8") as f:
    for words, preds in zip(all_input_tokens, preds_list): # 한 문장 
        
        line = ""
        
        word_end = False
        pii_word = ""
        
        for i, (word, pred) in enumerate(zip(words, preds)): # token별
            
            if i < len(preds)-1:
                
                if word_end == True:
                    pii_word = ""
                
                
                after_word = words[i+1]
                after_pred = preds[i+1]
                
                word = word.strip('#').strip()
                
                pii_word += word
                
                # print(pii_word)
                
                # 다음 단어에 #이 포함되어 있다면 이어지는 단어 
                if '#' in after_word:

                    # 뒤 토큰과 한 단어이지만 무의미하므로 따로 쓴다
                    if after_pred == 'O':
                        
                        if pred == 'O':
                            # 둘 다 Other인데 한 단어이다
                            word_end = False
                            
                        else:
                            # 그러면 그냥 혼자 적기
                            line = line + "[{}:{}] ".format(pii_word, pred)
                        
                            word_end = True
                        

                        
                    # 뒤 토큰과 한 단어이고, 유의미해서 같이 적어야 함
                    else: 
                        word_end = False
                        
                else:
                    word_end = True
                    
                    if pred == 'O':
                        line = line + pii_word + " "
                    
                    else:
                        line = line + "[{}:{}] ".format(pii_word, pred)
            
            # 마지막 단어 
            else:
                
                # print(line)
                if '#' in word:

                    word = word.strip('#').strip()
                    
                    if pred == 'O':
                        line = line + word + " "
                        
                    else:
                        pii_word += word
                        line = line + "[{}:{}] ".format(pii_word, pred)
                        
                else:
                    if pred == 'O':
                        line = line + word + " "
                    else:
                        line = line + "[{}:{}] ".format(word, pred) 
        
        
        # line = line.split()
        # print(line)
        
        # []
        # for idx in range(len(line)):
        #     item = line[idx].strip('['']').strip()
            
        #     item_pii = item.split(":")[0]
        #     item_label = item.split(":")[1]
            
            
            
                  
        f.write("{}\n".format(line.strip()))
        