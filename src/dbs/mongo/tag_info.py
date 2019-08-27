from pymongo import MongoClient
from all_login import mongo
from tagname_list import tag_names
from tagname_list import List
from tagname_list import tag_names_board
from tagname_list import List_board



def tag_info():
	#soojle 라는 데이터베이스에 접근
	data = mongo()
	client = MongoClient(data[0], int(data[1]))
	db = client["soojle"]

	#만약 tag_info 라는 테이블이 있으면 DROP
	db.tag_info.drop()

	#tag_info 라는 게시물을 생성해준다.
	collection = db["tag_info"]
	print(":::: tag_info CREATE Complete! ::::")

	#public_tag 일 경우에는 tagname_list.py 와 연동되서 자동 업데이트
	for tag_name in tag_names:
		string = List[tag_name][1] + "/"
		tag_done = string.split("/")
		tag_done.pop()
		collection.insert_one({"tag_id": tag_name, "tag_string": tag_done})
	
	#board_tag 일 경우, tag.py 에 갱신을 할 경우, tagname_list.py 에도 갱신을 해줘서, tag_info가 정상적으로 될 수 있도록 한다
	for tag_name in tag_names_board:
		#public 이랑 board 랑 태그명이 겹칠경우, string을 합쳐라
		if tag_name in tag_names:
			string = List[tag_name][1] + "/" + List_board[tag_name][1] + "/"
			tag_done = string.split("/")
			tag_done.pop()
			collection.update_one({"tag_id": tag_name}, {"$set": {"tag_string": tag_done}})
		#겹치지 않을 경우에는, 그냥 board만 넣어라
		else:
			string = List_board[tag_name][1] + "/"
			tag_done = string.split("/")
			tag_done.pop()
			collection.insert_one({"tag_id": tag_name, "tag_string": tag_done})

	print(":::: tag_info INSERT Complete! ::::")