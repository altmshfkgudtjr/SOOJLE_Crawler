import sys
sys.path.insert(0,'/home/iml/')
sys.path.insert(0,'/home/iml/SOOJLE/')
sys.path.insert(0,'/home/iml/SOOJLE_Crawler/src/')
sys.path.insert(0,'/home/iml/SJ_Auth')
sys.path.insert(0,'/home/iml/SJ_AI/src')
sys.path.insert(0,'/home/iml/IML_Tokenizer/src/')
sys.path.insert(0,'../../IML_Tokenizer/src/')
from all_login import mongo
from pymongo import MongoClient
from db_info import *
from platform import platform


#DB 및 Database 연결
def connect_db():
	#soojle 라는 데이터베이스에 접근
	data = mongo()
	if platform().startswith("Windows"):
		client = MongoClient(data[0], int(data[1]))
	else:
		client = MongoClient('mongodb://%s:%s@%s' %(MONGODB_ID, MONGODB_PW, MONGODB_HOST))
	db = client['soojle']

	return (client, db)

#DB 연결 해제
def disconnect_db(client):
	client.close()
