import json
import csv
import pandas as pd
import json
import random



def create_address():
    
    '''
    도로명주소 | 시+구+동 생성기
    '''
    
    postal_path = './통계청_나라통계_우편번호_20211110.csv' # 시+구+동+아파트
    admin_path = './zipdoro.csv' # 도로명주소 

    postal_code = pd.read_csv(postal_path, delimiter=',', encoding='cp949')
    admin_address = pd.read_csv(admin_path, delimiter=',', encoding='cp949', names=['CODE', 'ADDR'])
    
    admin_shuffle = admin_address['ADDR'].reset_index(drop=True)
    aidx = random.randrange(0, len(admin_shuffle))
    doro = admin_shuffle[aidx]
    
    postal_shuffle = postal_code.sample(frac=1).reset_index(drop=True)
    pidx = random.randrange(0, len(postal_shuffle))
    
    postal_building = postal_shuffle['동호'].dropna().reset_index(drop=True)
    idx = random.randrange(0, len(postal_building))
    apt_building = postal_building[idx]
    apt_room = random.randrange(101, 5000)
    address = postal_shuffle.drop(['우편번호', '우편번호순서'], axis=1).iloc[idx]
    print("동&지번 주소: "+address['전체주소'], "\n도로명 주소: "+doro, "\n"+str(apt_building)+"동 " +str(apt_room)+"호")
    

def main():
    create_address()

if __name__ == "__main__":
    main()