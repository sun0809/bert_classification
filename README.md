##### 🚂kc-bert를 사용한 자연어 문장분류 모델입니다.  
##### 🚕'BERT와 GPT로 배우는 자연어 처리' 교재의 코드를 참고하여 제작하였습니다.
##### BERT와 GPT로 배우는 자연어 처리' 교재의 깃허브주소: https://github.com/ratsgo/nlpbook.git
###### 현재 모델 저장 후 inference를 확인하는 부분은 코드생성 중입니다. 
---
```
사용한 pre-train모델과 tokenizer : beomi/kcbert-base
사용환경  cuda_version: 11.2 / Driver Version: 512.15 / cuDDN: 8.1.0
```
>🌏폴더 설명
>```
>kcbert: bert모델을 만들고,inference를 실행합니다.  
>ori_Folder: 한글파일을 txt파일로 변환하고 1000자~2000자 사이로 요약합니다.   
>docc_Folder: Docanno를 통해 라벨링한 .json 파일을 모델 훈련에 필요한 형태인 [라벨, 텍스트] 형식의 텍스트 파일로 변환합니다.  
>```

--------
###### 🪐ke-bert 폴더의 .py파일과 클래스 설명 
> ```
>kcbert-classification폴더
>>arguments.py : 모델 훈련에 필요한 인자값을 담고 있습니다. (모델 저장 위치, 프리트레인 모델, epoch 등등)  
>>corpus.py  
>> * NSMC Corpus : 데이터의 라벨과 텍스트를 구분하여 저장합니다. 필요한 라벨들을 저장합니다.   
>> * _convert_examples_to_classification_features : 문장을 토큰화하여 [input_ids, attention_mask, token_type_ids, label]로 저장합니다.   
>> * ClassificationDataset(Dataset) : 데이터를 train/validation/test의 형태에 맞게 저장합니다.  
>```
>```
>task.py: 모델실행에 필요한 optimizer와 scheduler 값을 설정합니다.  
>```
>```
>metrics.py: 테스트 결과의 정확도를 계산합니다.  
>```
>```
>trainer.py: pytorch.lightening을 사용한 모델실행코드를 담고 있습니다.  
>```
>```
>utils.py: logger, seed 등 모델 훈련시 필요한 설정값을 담고있습니다.  
>```
>```
>main.py: 실제 모델 훈련과 모델 저장을 실행하는 코드입니다.  
>```
>```
>inference.py -> inference를 실행하기 위한 코드입니다.  
-------

##### ☁ 실행방법
1. ```kcbert\ratsnlp\ratsnlp\nlpbook```로 이동하여```python main.py``` 파일을 실행합니다. -> 모델훈련 후 저장  
2.  cmd창에 ```>pip install --user --pre pyhwp```를 실행하여 pre pyhwp 를 다운받습니다. 
3. ```hwp5txt.exe```응용프로그램을 한글파일이 있는 폴더 아래에 둡니다.  
4. 해당폴더로 이동하여 다음 코드를 실행합니다.  
```python hwp2txt.py```  
5. 문장을 짧게 요약하는 코드를 실행합니다.
```python summary.py```  
6. 요약한 문장을 Doccano를 사용하여 labeling 합니다. 
7. Doccano에서 파일을 Json형태로 export 합니다. 
8. ```docc_Folder```에 .Json파일을 넣은 후 아래의 코드를 실행합니다. 
```python DOCC_jsonToTxt.py```
9. ```inference.py```를 실행하여 라벨링한 파일의 결과를 확인합니다.  
 --------
 
 ##### ✈ model dataset 변경 방법  
 >dataset 위치:  ```kcbert\result\Korpora\data``` 아래에 ```ratings_test.txt```, ```ratings_train.txt```로 존재  
 >dataset_example: label,sentence  
 >```1,한일진공 美 생명과학업체 지분 1.99% 취득 ```  
 
 >label 개수 위치 변경: ```kcbert\ratsnlp\ratsnlp\nlpbook\classification\corpus.py line.52```
 
 
 
