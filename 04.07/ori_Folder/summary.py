#폴더안의 모든 txt파일 요약하기 

import torch
from transformers import PreTrainedTokenizerFast
from transformers import BartForConditionalGeneration
import os
from tqdm import tqdm



PATH = 'C:/Users/coms/Desktop/04.07/'
folder_name = 'ori_Folder/'
data_folder = f'{PATH}{folder_name}'
file_list = os.listdir(data_folder)


tokenizer = PreTrainedTokenizerFast.from_pretrained('digit82/kobart-summarization')
model = BartForConditionalGeneration.from_pretrained('digit82/kobart-summarization')



def summ(text):

    raw_input_ids = tokenizer.encode(text)
    input_ids = [tokenizer.bos_token_id] + raw_input_ids + [tokenizer.eos_token_id]

    summary_ids = model.generate(torch.tensor([input_ids]),  num_beams=4,  max_length=512,  eos_token_id=1)
    return tokenizer.decode(summary_ids.squeeze().tolist(), skip_special_tokens=True)


def full_summ(text):
    
    for _ in range(4):
        text_all = ''
        rep = divmod(len(text),1000)
       # if rep[0] == 0:
        #    break
        for i in tqdm(range(rep[0])):
            start = i
            fin = i+1000

            div_text = text[start:fin]
            div_sum_text = summ(div_text)
            text_all+=div_sum_text
            if i == rep[0]-1:
                div_text = text[fin:fin+rep[1]]
                div_sum_text = summ(div_text)
                text_all+=div_sum_text
        text = text_all
        if (len(text)/1000) <2:
            break
    return text




def apply_full_summ():

    print('파일명                       글자수')
    for i in file_list:
        if i[-3:] == 'txt':
            report = i
            text_file_r = open(f"{data_folder}{report}", "r", encoding='utf-8')
            text_list = []
            for k in text_file_r:
                text_list.append(k)
            text = text_list[0]
            print("=========================================")
            print(report,len(text))
            

            result = full_summ(text)
            text_file_w = open(f"{data_folder}{report}", "w", encoding='utf-8')
            text_file_w.write(result)
            text_file_w.close()
            print(f"{data_folder}{report}","완료")
            print(report,len(result))
            print("=========================================")


apply_full_summ()
