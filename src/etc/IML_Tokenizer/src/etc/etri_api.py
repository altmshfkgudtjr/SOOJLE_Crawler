import urllib3
import json
import sys
import pandas as pd
from word_type_dict import *

from iml_stopword import get_han_stopwords, stop_set, single_stop 

# ETRI 형태소 분석
def ETRI_morp_analy(text):
	try:
		accessKey = open("etri_key.txt").read()
	except FileNotFoundError as e:
		print("ERROR: ETRI API를 작동시키기 위해서는 API KEY가 필요합니다.")
		print("KEY를 발급받으신 후, etri_key.txt 파일에 적어서 같은 경로에 놔둬주세요.")
		print("KEY 신청 URL: http://aiopen.etri.re.kr/key_main.php")
		print("개발 가이드 URL: http://aiopen.etri.re.kr/guide_wiseNLU.php")
		sys.exit(1)
	openApiURL = "http://aiopen.etri.re.kr:8000/WiseNLU"
	analysisCode = "wsd_poly"
	requestJson = {
	    "access_key": accessKey,
	    "argument": {
	        "text": text,
	        "analysis_code": analysisCode
	    }
	}
	http = urllib3.PoolManager()
	response = http.request(
	    "POST",
	    openApiURL,
	    headers={"Content-Type": "application/json; charset=UTF-8"},
	    body=json.dumps(requestJson)
	)
	if response.status != 200: print("접속 실패, status_code: ", response.status)
	return json.loads(response.data)

def ETRI_parser(json_data):
	tokens = []
	df = pd.DataFrame(columns = ["text","type","scode","weight"])
	for i,data in enumerate(json_data['return_object']['sentence']):
		data_list = {"text":[],"type":[],"scode":[],"weight":[]}
		for j in data['WSD']:
			if is_valid(j['text'], j['type']):
				data_list['text'].append(j['text'])
				data_list['type'].append(j['type'])
				data_list['scode'].append(j['scode'])
				data_list['weight'].append(j['weight'])
		temp = pd.DataFrame(data_list)
		if len(temp.index) == 0: continue
		df = df.append(temp, ignore_index = True)
		tokens += list(temp['text'])
	return tokens, df
