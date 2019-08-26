from pymongo import MongoClient
from time_convert import datetime_to_unixtime
from time_convert import unixtime_to_datetime
import filtering
from url_list import List

def init_db():
	#DB 없으면 생성
	client = MongoClient()
	client = MongoClient('localhost', 27017)
	db = client['soojle']


def get_lastly_post(URL):
	#soojle 라는 데이터베이스에 접근
	connect = connect_db.db()
	cur = connect.cursor()

	table_name = URL['info']
	query = "SELECT title FROM " + "lastly_post" + " WHERE info_id=%s"
	cur.execute(query, (table_name,))
	connect.commit()
	data = cur.fetchall()
	lastly_post_title = data[0][0]

	return lastly_post_title

def push_lastly_post(URL, lastly_post_title):
	#soojle 라는 데이터베이스에 접근
	connect = connect_db.db()
	cur = connect.cursor()

	table_name = URL['info']
	query = "UPDATE " + "lastly_post" + " SET title=%s WHERE info_id=%s"
	cur.execute(query, (lastly_post_title, table_name))
	connect.commit()
	print("\n\n:::: lastly_post INSERT Complete! ::::\n\n")


def db_manager(URL, post_data_prepare):
	add_cnt = 0
	#table_name = URL['info']
	table_name = "posts"
	posts_db = []
	temp = []
	
	#soojle 라는 데이터베이스에 접근
	connect = connect_db.db()
	cur = connect.cursor()

	#게시판에 맞는 테이블 없으면 생성
	##### post_id: 게시물 식별값, title: 제목, author: 작성자, date: 작성일, post: 게시물내용, img: OpenGraph용 url #####
	##### tag: 태그, info: 게시판 정보, fav_cnt: 좋아요개수, view: view 개수										 #####
	query = "CREATE TABLE IF NOT EXISTS " + table_name + " (post_id MEDIUMINT(9) UNSIGNED NOT NULL AUTO_INCREMENT,\
															title VARCHAR(300) NOT NULL,\
															author VARCHAR(50) NOT NULL,\
															date INT(11) NOT NULL,\
															post VARCHAR(3000) NOT NULL,\
															img VARCHAR(1000) NOT NULL,\
															url VARCHAR(500) NOT NULL,\
															tag VARCHAR(100) NOT NULL,\
															view MEDIUMINT(9) UNSIGNED DEFAULT 0,\
															fav_cnt MEDIUMINT(9) UNSIGNED DEFAULT 0,\
															login TINYINT(1) UNSIGNED NOT NULL,\
															PRIMARY KEY(post_id),\
															INDEX IDX_" + table_name +" (date DESC)\
															) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4"
	cur.execute(query)
	connect.commit()


	#post_data_prepare 을 필터링 check를 해준다.
	for post in post_data_prepare:
		if filtering.filter_public(post['title'] + post['post']):
			print("Unhealty Post ---- ", post['title'])
		elif URL['info'].split('_')[0] == 'sj20' or  URL['info'].split('-')[0] == 'sj22':
			if filtering.filter_hardcore(post['title'] + post['post']):
				print("Harmful Post ---- ", post['title'])
		else:
			temp.append(post)
	post_data_prepare = temp

	#post_data_prepare 에 값이 없으면 return
	post_data_prepare_len = len(post_data_prepare)
	if post_data_prepare_len == 0:
		return add_cnt

	#한 페이지에 title 이 중복되는 것이 있으면 걸러주는 함수
	post_data_prepare = sameposts_set(post_data_prepare)


	#게시판에서 title 값만 다 추출해서 posts_db 라는 리스트에 저장
	query = "SELECT title FROM " + table_name
	cur.execute(query)
	connect.commit()
	datas = cur.fetchall()
	for data in datas:
		posts_db.append(data[0])

	posts_db_len = len(posts_db)					#db에 박힌 포스트의 개수

	#posts_db에 게시물이 아무 것도 없으면 맨 처음 포스트를 넣어준다.
	if posts_db_len == 0:
		query = "INSERT INTO " + table_name + " (title, author, date, post, img, url, tag, login) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
		cur.execute(query, (post_data_prepare[0]['title'],\
							post_data_prepare[0]['author'],\
							datetime_to_unixtime(post_data_prepare[0]['date']),\
							post_data_prepare[0]['post'],\
							post_data_prepare[0]['img'],\
							post_data_prepare[0]['url'],\
							post_data_prepare[0]['tag'],\
							URL['login']))
		connect.commit()
		add_cnt += 1
		posts_db_len += 1

	posts_db = []
	#게시판에서 title, date, post_id 값만 다 추출해서 posts_db 라는 리스트에 저장
	query = "SELECT title, date, post_id FROM " + table_name
	cur.execute(query)
	connect.commit()
	datas = cur.fetchall()
	for data in datas:
		title_data = data[0]
		date_data = unixtime_to_datetime(data[1])
		post_id_data = data[2]
		data_done = (title_data, date_data, post_id_data)
		posts_db.append(data_done)

	posts_db_len = len(posts_db)					#db에 박힌 포스트의 개수
	post_data_prepare_len = len(post_data_prepare)	#준비된 포스트의 개수

	#입력 포스트를 DB포스트들과 title을 비교하여서 중복되면 최신글일 경우 UPDATE 하고 add_cnt++, 또는 중복되지 않으면 add_cnt++, 아무것도 해당안되면 same_cnt++
	for i in range(post_data_prepare_len):
		same_cnt = 0	#중복되는 카운트
		for j in range(posts_db_len):
			#prepare 게시물이 db 게시물과 title 이 같고, date 가 최신버전이면 UPDATE
			if (post_data_prepare[i]['title'] == posts_db[j][0]) and (post_data_prepare[i]['date'] > str(posts_db[j][1])):
				query = "UPDATE " + table_name + " SET author=%s, date=%s, post=%s, img=%s, url=%s, tag=%s WHERE post_id=%s"
				cur.execute(query, (post_data_prepare[i]['author'],\
									datetime_to_unixtime(post_data_prepare[i]['date']),\
									post_data_prepare[i]['post'],\
									post_data_prepare[i]['img'],\
									post_data_prepare[i]['url'],\
									post_data_prepare[i]['tag'],\
									posts_db[j][2]))
				connect.commit()
				add_cnt += 1
				same_cnt += 1	#INSERT INTO 되는것을 막기위한 row
				break
			#prepare 게시물이 db 게시물과 title 이 같고, date 가 같거나 옛날버전이면 same_cnt++
			elif (post_data_prepare[i]['title'] == posts_db[j][0]) and (post_data_prepare[i]['date'] <= str(posts_db[j][1])):
				same_cnt += 1
				break
			else:
				continue
		if same_cnt == 0:	#중복되지 않으면 추가
			query = "INSERT INTO " + table_name + " (title, author, date, post, img, url, tag, login) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
			cur.execute(query, (post_data_prepare[i]['title'],\
								post_data_prepare[i]['author'],\
								datetime_to_unixtime(post_data_prepare[i]['date']),\
								post_data_prepare[i]['post'],\
								post_data_prepare[i]['img'],\
								post_data_prepare[i]['url'],\
								post_data_prepare[i]['tag'],\
								URL['login']))
			connect.commit()
			add_cnt += 1

	connect.close()
	return add_cnt

#'info' 의 테이블에 있는 포스트의 개수 반환하는 함수
def get_table_posts(URL):
	#soojle 라는 데이터베이스에 접근
	connect = connect_db.db()
	cur = connect.cursor()

	query = "SELECT post_id FROM " + URL['info']
	cur.execute(query)
	connect.commit()
	post_ids = cur.fetchall()
	posts_num = len(post_ids)

	return posts_num


#한 페이지 안에서 같은 post_data 제거 함수
def sameposts_set(post_data_prepare):
	clear_posts = []
	before_num = len(post_data_prepare)

	#첫번째 post 데이터 넣어주기
	clear_posts.append(post_data_prepare[0])

	for i in range(before_num):
		after_num = len(clear_posts)
		same_cnt = 0
		for j in range(after_num):
			if post_data_prepare[i]['title'] == clear_posts[j]['title']:
				same_cnt += 1
			else:
				continue
		if same_cnt == 0:
			clear_posts.append(post_data_prepare[i])

	return clear_posts