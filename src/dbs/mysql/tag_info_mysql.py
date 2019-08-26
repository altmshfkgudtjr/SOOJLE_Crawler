import MySQLdb
import connect_db
from tagname_list import tag_names
from tagname_list import List
from tagname_list import tag_names_board
from tagname_list import List_board



def tag_info():
	#soojle 라는 데이터베이스에 접근
	connect = connect_db.db()
	cur = connect.cursor()

	#만약 tag_info 라는 테이블이 있으면 DROP
	query = "DROP TABLE IF EXISTS tag_info"
	cur.execute(query)
	connect.commit()

	#tag_info 라는 게시물을 생성해준다.
	query = 'CREATE TABLE tag_info (tag_id VARCHAR(20) NOT NULL,\
									tag_string VARCHAR(1000) DEFAULT "",\
									PRIMARY KEY(tag_id)\
									) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4'
	cur.execute(query)
	connect.commit()
	print(":::: tag_info CREATE Complete! ::::")

	#public_tag 일 경우에는 tagname_list.py 와 연동되서 자동 업데이트
	for tag_name in tag_names:
		string = List[tag_name][1] + "/"
		query = "INSERT INTO tag_info (tag_id, tag_string) VALUES (%s, %s)"
		cur.execute(query, (tag_name, string))
	connect.commit()
	
	#board_tag 일 경우, tag.py 에 갱신을 할 경우, tagname_list.py 에도 갱신을 해줘서, tag_info가 정상적으로 될 수 있도록 한다
	for tag_name in tag_names_board:
		#public 이랑 board 랑 태그명이 겹칠경우, string을 합쳐라
		if tag_name in tag_names:
			string = List[tag_name][1] + "/" + List_board[tag_name][1] + "/"
			query = "UPDATE tag_info SET tag_string = %s WHERE tag_id = %s"
			cur.execute(query, (string, tag_name))
		#겹치지 않을 경우에는, 그냥 board만 넣어라
		else:
			string = List_board[tag_name][1] + "/"
			query = "INSERT INTO tag_info (tag_id, tag_string) VALUES (%s, %s)"
			cur.execute(query, (tag_name, string))
	connect.commit()

	print(":::: tag_info INSERT Complete! ::::")