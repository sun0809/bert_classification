# 한글파일 -> 텍스트 파일로 만드는 문서 
# 파일 실행 전 반드시 hwp5txt.exe와 hwp파일이 함께 있는 폴더로 이동 후 실행 
from pathlib import Path

import pandas as pd
import os




PATH = 'C:/Users/coms/Desktop/04.07/'
folder_name = 'ori_Folder/'
data_folder = f'{PATH}{folder_name}'


exefile = 'hwp5txt'

def convert_to_txt(data_folder,exefile):

    file_list = os.listdir(data_folder)
    for i in file_list:
        if i[-3:] == 'hwp':
            hwp_filename  = i
            txt_filename = i[:-4]+ ".txt"
            output = '--output ' + '"' + txt_filename + '"'
            result = '"' + hwp_filename + '"'
            print(exefile + " " + output + " " + result)
            os.system(exefile + " " + output + " " + result)


def preprocessing(data_folder):   

    file_list = os.listdir(data_folder) 
    for i in file_list:
        if i[-3:] == 'txt':
            report = i
            dt = pd.read_csv(f"{data_folder}{report}", sep='\t',header=None)
            dt1 = [i for i in dt[0]  if i not in ['<표>','<그림>']]
            str = ' '
            dt2 = str.join(dt1)
            text = dt2.replace('□',"").replace('-',"").replace('○',"").replace('*',"").replace('※',"")
            text = text.replace('      ', ' ')
            text = text.replace('     ', ' ')
            text = text.replace('   ', ' ')
            text = text.replace('  ', ' ')
            text_file = open(f"{data_folder}{report}", "w", encoding='utf-8')
            text_file.write(text)
            text_file.close()
            print(f"{data_folder}{report}","완료")


if __name__ == "__main__":
    convert_to_txt(data_folder,exefile)  
    preprocessing(data_folder)

