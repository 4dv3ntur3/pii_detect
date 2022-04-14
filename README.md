# pii_detect

#### pii를 포함한 dataset을 전처리하기 위한 코드

#### 사용 순서
1. make_csv.py로 json에서 필요한 대화 데이터만 추출해서 한 행씩 + O tags
2. 이후 비식별화된 부분 채우기 및 자동 태깅은 적절하게 필요 코드 사용 

##### 코드
+ check_pattern_used_option_with_counter_ver.py
상담 데이터셋에서 카드번호 (ㅇㅇㅇㅇ ㅇㅇㅇㅇ ㅇㅇㅇㅇ ㅇㅇㅇㅇ)가 등장하는 패턴을 찾고, 비식별화 처리된 부분을 랜덤 데이터로 대체

+ create_address.py
  + 데이터셋에서 비식별화된 부분을 대체하기 위해 랜덤한 도로명주소, 옛날 방식의 주소, 아파트명, 가게 이름, 동호수 등을 생성
  + 필요한 데이터
    + 상호명) store_names_whole.tsv: 지역별 소상공인시장진흥공단_상가(상권)를 전부 로드 -> 이름만 drop -> concat한 것
    + 도로명주소) zipdoro.tsv: 우편번호별 도로명주소 데이터
    + 옛날 방식 주소+아파트명+동호수) 통계청_나라통계_우편번호_20211100.tsv

+ random_data.ipynb
  + 전화번호, 주민번호, 지역번호 등의 숫자 데이터를 랜덤으로 생성하는 코드 

+ creae_fake_data.py
  + create_address와 random_data를 합쳐서 각종 개인정보를 한 번에 랜덤으로 생성하도록 만든 것

+ make_csv.py, test.py
  + json으로 되어 있던 상담 데이터셋의 원천 라벨 데이터에서 필요한 상담사 질문/답변, 고객 질문/답변 만을 추출해 tsv 형태로 만들도록 한 코드 (original)
  + 띄어쓰기 기준 단어의 개수대로 우선 Other tag를 붙여 놓도록 전처리함 (태깅할 때 해당 단어의 Other tag만 바꿔서 쓰면 되도록.)

+ preprocess_tsv.py
  + make_csv에서 문장에 있는 중복 공백이 제거되지 않은 상태로 Other tag를 붙이거나 하는 문제 -> 띄어쓰기 단위로 문장을 나눴을 때 tag들의 개수 안 맞는 문제 개선
  + 중복 공백 제거 후 Other tag 붙임

+ python_dataclass_output_check_for_electra_tuning.py
  + ELECTRA 모델 튜닝을 위해서 return type인 ELECTRAOutput class를 분석하다가 python의 dataclasses의 반환형을 튜플화할 수 있는지 확인하기 위해 테스트

+ tsv_concat.py
  + 그동안 작업한 tsv 파일 [SENTENCES, TAG] column 맞추고 row 단위로 concat하기 위한 코드 (취합을 위한 전처리)

+ fill_all_Others_except_address.py
  + 내가 맡고 있는 주소 태그(AD_ADDRESS, AD_DETAIL)를 제외한 나머지 태그들은 전부 Other tag 처리해서 학습시키기 위한 코드
