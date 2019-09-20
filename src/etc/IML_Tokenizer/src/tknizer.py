from iml_data import *
from konlpy.tag import Komoran
from nltk.corpus import stopwords
import re
import pandas as pd
import sys

komoran = Komoran(max_heap_size= 1024 * 6)

def preprocess(doc, length):
	emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)
	doc = re.sub('\s'," ", doc)
	doc = doc.lower()
	doc = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', ' ', doc)
	doc = emoji_pattern.sub(r'', doc)
	doc = re.compile('[^ ㄱ-ㅣ가-힣|a-z]+').sub('', doc)
	return [doc[i:i+length] for i in range(0, len(doc), length)]

def is_valid(data, m_type):
	h_s_set = h_stopwords
	e_s_set = set(stopwords.words('english'))
	if len(data) <= 1 or data in h_s_set:
		return False
	if m_type == "SL" and (data in e_s_set or len(data) <= 2):
		return False
	if data in stop_set:
		return False
	if any(i in single_stop for i in data):
		return False
	if m_type not in ["SH", "SL"] and data != re.compile('[^ ㄱ-ㅣ가-힣|a-z]+').sub('', data):
		return False
	if len(data) >= 15:
		return False
	sign_list = sign_dict.values()
	if m_type in sign_list:
		return True
	return False

def konlpy_morp_analy(text):
	#print("docs_length:",len(text))
	try:
		result = komoran.pos(text)
		return result
	except:
		return []

def konlpy_parser(m_list):
	tokens = []
	df = pd.DataFrame(columns = ["text", "type"])
	for data,m_type in m_list:
		if is_valid(data, m_type):
			tokens += [data]
	return tokens

# def ETRI_make_tokens(doc, idx = None):
# 	doc = preprocess(doc, 10_000)
# 	tokens = []
# 	for doc_ in doc:
# 		temp, _ = ETRI_parser(ETRI_morp_analy(doc_))
# 		tokens += temp
# 	return tokens

def get_tk(doc):
	doc = preprocess(doc, 3_000)
	tokens = []
	for doc_ in doc:
		temp = konlpy_parser(konlpy_morp_analy(doc_))
		tokens += temp
	return tokens