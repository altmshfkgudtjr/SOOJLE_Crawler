from all_login import mongo
from pymongo import MongoClient



#DB 및 Database 연결
def connect_db():
	#soojle 라는 데이터베이스에 접근
	data = mongo()
	client = MongoClient(data[0], int(data[1]))
	db = client['soojle']

	return (client, db)

#DB 연결 해제
def disconnect_db(client):
	client.close()