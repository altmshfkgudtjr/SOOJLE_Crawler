from pymongo import MongoClient
from domain_list import List
from tknizer import *


def domain_insert(db):
	#soojle 라는 데이터베이스에 접근

	#sj_domain 테이블이 존재하면 DROP TABLE
	db.sj_domain.drop()

	#sj_domain 테이블 생성
	collection_domain = db["sj_domain"]

	#sj_domain 리스트 값 INSERT
	for domain in List:
		query = {
					"post_id":domain['post_id'],
					"title":domain['title'],
					"date":(domain['date']),
					"post":domain['post'],
					"img":domain['img'],
					"url":domain['url'],
					"tag":domain['title_tag'],
					"login": 0,
					"view": 0,
					"title_token": domain['title'].split(" "),
					"token": get_tk(domain['title'] + domain['post'])
				}
		collection_domain.insert_one(query)