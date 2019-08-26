from pymongo import MongoClient
from all_login import mongo
from domain_list import List

def domain_insert():
	#soojle 라는 데이터베이스에 접근
	data = mongo()
	client = MongoClient(data[0], int(data[1]))
	db = client["soojle"]

	#sj_domain 테이블이 존재하면 DROP TABLE
	db.sj_domain.drop()

	#sj_domain 테이블 생성
	collection_domain = db["sj_domain"]

	#sj_domain 리스트 값 INSERT
	for domain in List:
		collection_domain.insert_one({"post_id":domain['post_id'], "title":domain['title'], "date":domain['date'], "post":domain['post'], "img":domain['img'], "url":domain['url'], "tag":domain['title_tag'], "login": 0, "view": 0})