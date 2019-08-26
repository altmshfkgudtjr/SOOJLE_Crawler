from pymongo import MongoClient
from url_list import List
from domain_insert import domain_insert


def post_info():
	info_input = []
	
	#soojle 라는 데이터베이스에 접근
	client = MongoClient()
	client = MongoClient('localhost', 27017)
	db = client["soojle"]
	
	#post_info 테이블이 존재하면 DROP TABLE
	db.post_info.drop()
	
	#그리고 다시 새로 만든다.
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
	domain_insert()
	print(":::: sj_domain INSERT Complete! ::::")
	
	
	#최신 게시물 저장하는 lastly_post 테이블 생성
	collection = db["lastly_post"]
	for URL in List:
		collection.insert_one({"info_id": URL['info']})
	print(":::: lastly_post CREATE Complete! ::::")