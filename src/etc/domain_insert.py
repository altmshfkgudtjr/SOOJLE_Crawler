import MySQLdb
from domain_list import List
import connect_db

def domain_insert():
	#soojle 라는 데이터베이스에 접근
	connect = connect_db.db()
	cur = connect.cursor()

	#sj_domain 테이블이 존재하면 DROP TABLE
	query = "DROP TABLE IF EXISTS sj_domain"
	cur.execute(query)
	connect.commit()

	#sj_domain 테이블 생성
	query = "CREATE TABLE IF NOT EXISTS sj_domain (post_id MEDIUMINT(9) UNSIGNED NOT NULL AUTO_INCREMENT,\
													title VARCHAR(100) NOT NULL,\
													author VARCHAR(20) DEFAULT 0,\
													date INT(11) NOT NULL,\
													post VARCHAR(3000) NOT NULL,\
													img VARCHAR(500) NOT NULL,\
													url VARCHAR(500) NOT NULL,\
													tag VARCHAR(100) NOT NULL,\
													view MEDIUMINT(9) UNSIGNED DEFAULT 0,\
													login TINYINT(1) UNSIGNED NOT NULL,\
													PRIMARY KEY(post_id),\
													INDEX IDX_sj_domain (date DESC)\
													) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4"
	cur.execute(query)
	connect.commit()

	#sj_domain 리스트 값 INSERT
	for domain in List:
		query = "INSERT INTO sj_domain (post_id, title, date, post, img, url, tag, login) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
		cur.execute(query, (domain['post_id'], domain['title'], domain['date'], domain['post'], domain['img'], domain['url'], domain['title_tag'], 0))
	connect.commit()

	connect.close()