# 한글파일 pdf 변환 후 pdf txt파일 변환

import re
from pathlib import Path
import hanja
import pandas as pd
import os
import shutil
import win32com.client as win32
import pdfplumber
from glob import glob

# set arguments
# path will be set as this directory if it's not defined


# import win32com.client as win32 에서 에러가 났다면 아래 코드를 실행하세요.
# pip install pywin32
# pip install --upgrade pywin32==225


# set folder path
input_dir = os.path.join(os.getcwd(), 'raw_files', 'pdf_raw')
output_dir = os.path.join(input_dir, 'text')
new_pdf = os.path.join(input_dir, 'new_pdf')


def allfile(input_dir):
    file_list = []
    path_list = []
    for (root, directories, files) in os.walk(input_dir):
        for file in files:
            if file[-4:] == '.pdf' or file[-4:] == '.hwp':
                file_path = os.path.join(root, file)
                path_list.append(file_path)
                ori_file_path = file_path.split('\\')[-1]
                file_list.append(ori_file_path)
    return path_list, file_list


def hwp2pdf(file_path_list, file_name_list):
    hwp = win32.gencache.EnsureDispatch("HWPFrame.HwpObject")  # 한글프로그램 실행
    # 보안모듈 적용(파일 열고닫을 때 팝업이 안나타남)
    hwp.RegisterModule("FilePathCheckDLL", "FilePathCheckerModule")
    hwp.XHwpWindows.Item(0).Visible = True  # 한글 백그라운드 한글 보이게
    for i, path in enumerate(file_path_list):
        if path[-4:] == '.hwp':
            new_path = os.path.join(new_pdf, file_name_list[i][:-4]+".pdf")
            hwp.Open(path)
            hwp.HAction.GetDefault(
                "FileSaveAsPdf", hwp.HParameterSet.HFileOpenSave.HSet)  # 파일 저장 액션의 파라미터를
            # 저장할 파일 경로 및 이름.pdf 확장자명을 꼭 pdf로 적어주어야 함.
            hwp.HParameterSet.HFileOpenSave.filename = f'{new_path}'
            hwp.HParameterSet.HFileOpenSave.Format = "PDF"  # 파일 확장자 pdf
            hwp.HParameterSet.HFileOpenSave.Attributes = 16384
            hwp.HAction.Execute(
                "FileSaveAsPdf", hwp.HParameterSet.HFileOpenSave.HSet)


if __name__ == "__main__":

    # if not os.path.exists(output_dir):
    #    os.mkdir(output_dir)

    if not os.path.exists(new_pdf):
        os.mkdir(new_pdf)

    # changeFileName()
    file_path_list, file_name_list = allfile(input_dir)

    hwp2pdf(file_path_list, file_name_list)
    file_path_list, file_name_list = allfile(input_dir)
    # text(file_path_list,file_name_list)
    # prep(output_dir)

    print("전체 파일개수 : ", len(os.listdir(new_pdf)))
