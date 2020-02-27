from pymongo import MongoClient
from url_list import List
from domain_insert import domain_insert



def post_info(db):
	info_input = []
	
	#soojle 라는 데이터베이스에 접근
	
	#존재유무 파악
	collist = db.list_collection_names()
	if 'post_info' in collist:
		print(":::: post_info ALREADY EXISTS! ::::")
		return

	#info_id : db게시판 테이블에서 보여지는 식별자값
	collection = db["post_info"]
	
	#info_id : sj_domain, title_tag : 도메인, login : 0 추가
	collection.insert_one({"info_id": "sj_domain", "title_tag": "도메인/"})
	print(":::: post_info CREATE Complete! ::::")
	
	#url_list 에서 각 게시판의 info, title_tag, login 값을 post_info 테이블에 넣어준다.
	#login은 로그인 유무
	for URL in List:
		collection.insert_one({"info_id": URL['info'], "title_tag": URL['title_tag']})
	print(":::: post_info INSERT Complete! ::::")

	#도메인 sj_domain 테이블 추가 + domain_list 추가
	domain_insert(db)
	print(":::: sj_domain INSERT Complete! ::::")
	
	
	#최신 게시물 저장하는 lastly_post 테이블 생성
	collection = db["lastly_post"]

	if collection.find().count() == 0:
		for URL in List:
			collection.insert_one({"info_id": URL['info'], "title": 0})
		print(":::: lastly_post CREATE Complete! ::::")