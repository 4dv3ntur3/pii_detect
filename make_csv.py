import argparse
import json
import csv

data = []

def writedata(aaa, f):
    a = len(aaa.split(' ')) - 1
    f.writerow([aaa, 'O '*a + 'O'])

def main(args):
    file_path = args.target_file
    output_file = args.output_path
    params = args.param
    
    if len(params) > 4:
        exit()
    
    with open(file_path, 'r', encoding="UTF-8") as json_file, open(output_file, 'w', newline = '', encoding="UTF-8") as output:
        json_data = json.load(json_file)
        
        f = csv.writer(output, delimiter='\t')
        
        for datalow in json_data:
            if datalow[params[0]]:
                writedata(datalow[params[0]], f)
            elif datalow[params[1]]:
                writedata(datalow[params[1]], f)
            elif datalow[params[2]]:
                writedata(datalow[params[2]], f)
            elif datalow[params[3]]:
                writedata(datalow[params[3]], f)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-TF", "--target_file", type=str, help="원하는 json파일을 넣어주세요.")
    parser.add_argument("-OP", "--output_path", type=str, help="원하는 output경로를 작성하세요.")
    parser.add_argument("-P", "--param", nargs="+", help="필요한 파라미터들을 부여해주세요. 최대 4개")
    
    args = parser.parse_args()
    
    main(args)