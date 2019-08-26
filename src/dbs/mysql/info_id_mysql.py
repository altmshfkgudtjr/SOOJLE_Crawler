"""#############################################"""
"""			 	   ※주의사항※					"""
"""		 꼭 DATABASE 생성 후, 실행시킬 것			"""
"""#############################################"""
import MySQLdb
from url_list import List
from domain_insert import domain_insert
import connect_db


def post_info():
	info_input = []
	
	#soojle 라는 데이터베이스에 접근
	connect = connect_db.db()
	cur = connect.cursor()
	
	#post_info 테이블이 존재하면 DROP TABLE
	query = "DROP TABLE IF EXISTS post_info"
	cur.execute(query)
	connect.commit()
	
	
	
	#그리고 다시 새로 만든다.
	#info_id : db게시판 테이블에서 보여지는 식별자값
	query = "CREATE TABLE post_info (info_id VARCHAR(50) NOT NULL,\
									title_tag VARCHAR(30) NOT NULL,\
									PRIMARY KEY(info_id)\
									) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4"
	cur.execute(query)
	connect.commit()
	
	
	#info_id : sj_domain, title_tag : 도메인, login : 0 추가
	query = "INSERT INTO post_info (info_id, title_tag) VALUES (%s, %s)"
	cur.execute(query, ("sj_domain", "도메인/"))
	connect.commit()
	print(":::: post_info CREATE Complete! ::::")
	
	#url_list 에서 각 게시판의 info, title_tag, login 값을 post_info 테이블에 넣어준다.
	#login은 로그인 유무
	for URL in List:
		query = "INSERT INTO post_info (info_id, title_tag) VALUES (%s, %s)"
		cur.execute(query, (URL['info'], URL['title_tag']))
	connect.commit()
	print(":::: post_info INSERT Complete! ::::")

	#도메인 sj_domain 테이블 추가 + domain_list 추가
	domain_insert()
	print(":::: sj_domain INSERT Complete! ::::")
	
	
	#최신 게시물 저장하는 lastly_post 테이블 생성
	query = "CREATE TABLE IF NOT EXISTS lastly_post (info_id VARCHAR(50) NOT NULL,\
													title VARCHAR(300) DEFAULT 0,\
													PRIMARY KEY(info_id)\
													) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4"
	cur.execute(query)
	connect.commit()
	for URL in List:
		query = "INSERT INTO lastly_post (info_id) SELECT %s FROM DUAL WHERE NOT EXISTS\
				(SELECT info_id FROM lastly_post WHERE info_id=%s)"
		cur.execute(query, (URL['info'], URL['info']))
	connect.commit()
	print(":::: lastly_post CREATE Complete! ::::")


	connect.close()	