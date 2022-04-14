import json
import csv
import pandas as pd
import json
import random
from korean_name_generator import namer
import glob


def create_ids():
    mask = "[O0]"
    seperators = "- ."
    cell_phone_heads = [
            "010", "011", "016", "017", "018", "019"        
    ]
    local_numbers = [
            "020", "030", "040", "090",
            "050", "0505",
            "060", "070", "080",

            "031", "032", "033",
            "041", "042", "043", "044",    
            "051", "052", "053", "054", "055",
            "061", "062", "063", "064",]
    # four_digits = [
    #       "1566", "1600", "1670",
    #       "1577", "1588", "1899",
    #       "1522", "1544", "1644", "1661",
    #       "1599",
    #       "1688", "1666",
    #       "1855",
    #       "1811", "1877",]
    banks = ['경남', '광주', '국민', '농협', '대구', '부산', '수협', '신한', '우리', '전북', '제주', '중소기업', '카카오뱅크', '케이뱅크', '토스뱅크', '하나', '한국산업', '한국스탠다드차타드']
    insurances = ['ABL생명', 'AIA생명', 'BNP파리바카디프생명', 'DB생명', 'DGB생명', 'IBK연금보험', 'KB생명', 'KDB생명', 'NH농협생명', '교보라이프플래닛', '교보생명', '동양생명', '라이나생명', '메트라이프생명', '미래에셋생명', '삼성생명', '신한라이프(구 신한생명)', '신한라이프(구 오렌지라이프)', '처브라이프', '푸르덴셜생명', '하나생명', '한화생명', '현대라이프생명', '흥국생명', 'AIG손해보험', 'BNP파리바카디프손해보험', 'KB손해보험', 'MG손해보험', 'NH농협손해보험', 'SGI서울보증', 'The - K 손해보험', '동부화재해상보험', '롯데손해보험', '메리츠화재해상보험', '삼성화재해상보험', '악사손해보험', '에이스손해보험', '한화손해보험', '현대해상화재보험', '흥국화재해상보험']
    cards = ['BC바로카드', 'KB국민카드', '롯데카드', '삼성카드', '신한카드', '우리카드', '하나카드', '현대카드', 'BMW파이낸셜코리아', 'KB캐피탈', '아프로캐피탈', '애큐온캐피탈', '폭스바겐 파이낸셜', 'BNK캐피탈', 'JB우리캐피탈', 'NH농협캐피탈', '롯데캐피탈', '메리츠캐피탈', '아주캐피탈', '알씨아이파이낸셜서비스코리아', '에이캐피탈', '하나캐피탈', '한국캐피탈', '현대캐피탈', '현대커머셜']
    NEED_CHECK = "NEED_CHECK"

    def str_random(start, end):
        return str(random.randint(start, end))

    def fit_date_format(date):
        if len(date) < 2:
            return '0' + date
        return date
    def make_random_number(start, random_size):
        result = start
        for i in range(random_size):
            result += str_random(0, 9)
        return result

    def random_phone_head_number():
        # return [random.choice(cell_phone_heads), random.choice(local_numbers), "02", make_random_number("", 4), ""]
        return [random.choice(cell_phone_heads)+ " " + make_random_number("", 4) + " " + 
                make_random_number("", 4), random.choice(cell_phone_heads)+ " " + make_random_number("", 3) + " " + make_random_number("", 4), 
                
                "010" + " " + make_random_number("", 4) + " " + make_random_number("", 4)]


    def random_inum():
        inum = []
        year = str_random(1930, 2022)
        month = fit_date_format(str_random(1, 12))
        day = fit_date_format(str_random(1, 31))
        birth = year + month + day
        inum.append(birth[2:])
        inum.append(birth)
        inum.append(year + '년 ' + month + '월 ' + birth + '일')
        inum.append('뒷자리 ->> ' + str_random(1800000, 4999999))
        return inum

    def make_random_data(task):
        output = []
        if task == 1:
            output.append(random_inum())
        if task == 2:
            for i in range(1, 10):
                output.append(f'{i}   ' + make_random_number('', i))
        elif task == 3:
            output.append(random_phone_head_number())
        elif task == 4:
            output.append(random.choice(banks))
            output.append(random.choice(insurances))
        print(output)

    # for i in range(20):
    #     make_random_data(4)
    for i in range(1, 20):
        make_random_data(i%4+1)


def rand_idx(df):
    idx = random.randrange(0, len(df))
    return idx

def create_address():
    
    '''
    도로명주소 | 시+구+동 생성기
    '''
    src_dir = './data/fake_data_generating_src/'
    postal_path = src_dir + '통계청_나라통계_우편번호_20211110.csv' # 시+구+동+아파트
    admin_path = src_dir + 'zipdoro.csv' # 도로명주소 

    postal_code = pd.read_csv(postal_path, delimiter=',', encoding='cp949')
    admin_address = pd.read_csv(admin_path, delimiter=',', encoding='cp949', names=['CODE', 'ADDR'])
    
    admin_shuffle = admin_address['ADDR'].reset_index(drop=True)
    aidx = rand_idx(admin_shuffle)
    doro = admin_shuffle[aidx]
    
    postal_shuffle = postal_code.sample(frac=1).reset_index(drop=True)
    pidx = rand_idx(postal_shuffle)
    
    apart_name = postal_shuffle['리건물이름'].dropna().reset_index(drop=True)
    nidx = rand_idx(apart_name)
    
    postal_building = postal_shuffle['동호'].dropna().reset_index(drop=True)
    bidx = rand_idx(postal_building)
    
    apt_name = apart_name[nidx]
    apt_building = postal_building[bidx]
    apt_room = random.randrange(101, 5000)
    address = postal_shuffle.drop(['우편번호', '우편번호순서'], axis=1).iloc[bidx]
    print("동&지번 주소: "+address['전체주소'], "\n건물 이름: "+apt_name, "\n도로명 주소: "+doro, "\n"+str(apt_building)+"동 " +str(apt_room)+"호\n\n")
    
def create_names():
    male_name = namer.generate(True)
    female_name = namer.generate(False)
    
    names = []
    for i in range(5):
        male_name = namer.generate(True)
        female_name = namer.generate(False)
        names.append(male_name)
        names.append(female_name)
        
    return names
        
    # print("\n 이름: " , names)

def create_stores():
    
    # 각 지역의 상호명 파일 합쳐서 한 csv로 만드는 전처리 
    # filepath = './store_names/*'
    # file_list = glob.glob(filepath)
    # file_list_csv = [file for file in file_list if file.endswith(".csv")]
    # print(file_list_csv)
    
    # store_df = pd.DataFrame()
    # for i in range(len(file_list_csv)):
    #     file = file_list_csv[i]
    #     store = pd.read_csv(file, delimiter=",", encoding='utf-8', low_memory=False)
    #     store = store['상호명']
    #     store_df = pd.concat([store_df, store], sort=False)
    
    # store_df.to_csv('./store_names_whole.csv', sep=',')
    
    src_dir = './data/fake_data_generating_src/'
    filepath = src_dir+'store_names_whole.csv'
    stores = pd.read_csv(filepath, delimiter=',', encoding='utf-8').reset_index(drop=True)
    sidx = rand_idx(stores)
    s_name = stores.iloc[sidx]
    print("\n상호명: ", s_name)
    
    
def create_shopping():
    
    shop_list = ["지에스홈쇼핑", "GS홈쇼핑", "엔에스홈쇼핑", "NS홈쇼핑", "씨제이오쇼핑", "CJ오쇼핑", "현대홈쇼핑", "홈앤쇼핑", "공영홈쇼핑", "롯데홈쇼핑"]
    sidx = rand_idx(shop_list)
    name = create_names()
    print(shop_list[sidx] + " " + name[sidx] + "입니다.")
    print(shop_list[sidx] + "입니다")
    


def main():

    create_address()
    create_ids()
    create_stores()
    create_shopping()
    
    names = create_names()
    print(names)
    


if __name__ == "__main__":
    main()