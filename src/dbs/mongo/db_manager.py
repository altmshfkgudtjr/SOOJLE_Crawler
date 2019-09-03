from pymongo import MongoClient
from all_login import mongo
from time_convert import datetime_to_unixtime
from time_convert import unixtime_to_datetime
from time_convert import datetime_to_mongo
from time_convert import mongo_to_datetime
import filtering
from url_list import List
from datetime import datetime
import hashlib

#md5 해쉬
enc = hashlib.md5()

#공모전 ~까지를 위한 collum 생성
contest_list = ["campuspick", "detizen", "jobkorea"]
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def init_db():
	#DB 없으면 생성
	data = mongo()
	client = MongoClient(data[0], int(data[1]))
	db = client['soojle']


def get_lastly_post(URL):
	#soojle 라는 데이터베이스에 접근
	data = mongo()
	client = MongoClient(data[0], int(data[1]))
	db = client['soojle']

	table_name = URL['info']
	document = db.lastly_post.find_one({"info_id": table_name})
	lastly_post_title = document['title']

	return lastly_post_title

def push_lastly_post(URL, lastly_post_title):
	#soojle 라는 데이터베이스에 접근
	data = mongo()
	client = MongoClient(data[0], int(data[1]))
	db = client['soojle']

	table_name = URL['info']
	db.lastly_post.update_one({"info_id": table_name}, {'$set': {"title": lastly_post_title}})
	print("\n\n:::: lastly_post INSERT Complete! ::::\n\n")


def db_manager(URL, post_data_prepare):
	add_cnt = 0
	#table_name = URL['info']
	table_name = "posts"
	posts_db = []
	temp = []
	
	#soojle 라는 데이터베이스에 접근
	data = mongo()
	client = MongoClient(data[0], int(data[1]))
	db = client['soojle']

	#게시판에 맞는 테이블 없으면 생성
	##### post_id: 게시물 식별값, title: 제목, author: 작성자, date: 작성일, post: 게시물내용, img: OpenGraph용 url #####
	##### tag: 태그, info: 게시판 정보, fav_cnt: 좋아요개수, view: view 개수										 #####
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
	posts_db = db.posts.find({}, {"_id": 0,"title": 1})
	posts_db_len = db.posts.find().count()					#db에 박힌 포스트의 개수

	#posts_db에 게시물이 아무 것도 없으면 맨 처음 포스트를 넣어준다.
	hash_before = post_data_prepare[0]['title'] + post_data_prepare[0]['author'] + post_data_prepare[0]['post']
	if posts_db_len == 0:
		query = {
					"hashed" : hashlib.md5(hash_before.encode('utf-8')).hexdigest(),
					"title" : post_data_prepare[0]['title'],
					"author": post_data_prepare[0]['author'],
					"date" : datetime_to_mongo(post_data_prepare[0]['date']),
					"post" : post_data_prepare[0]['post'],
					"img" : post_data_prepare[0]['img'],
					"url" : post_data_prepare[0]['url'],
					"tag" : post_data_prepare[0]['tag'],
					"login" : URL['login'],
					"info" : URL['info'].split("_")[1],
					"view" : 0,
					"fav_cnt": 0
				}
		if URL['info'].split("_")[1] in contest_list:
			query["date"] = datetime_to_mongo(now)
			query["end_date"] = datetime_to_mongo(post_data_prepare[0]['date'])
		db.posts.insert_one(query)
		add_cnt += 1
		posts_db_len += 1

	posts_db = []
	#게시판에서 title, date, post_id 값만 다 추출해서 posts_db 라는 리스트에 저장
	documents = db.posts.find({}, {"title": 1, "date": 1})
	for document in documents:
		title_data = document["title"]
		date_data = mongo_to_datetime(document["date"])
		post_id_data = document["_id"]
		data_done = (title_data, date_data, post_id_data)
		posts_db.append(data_done)

	posts_db_len = db.posts.find().count()					#db에 박힌 포스트의 개수
	post_data_prepare_len = len(post_data_prepare)	#준비된 포스트의 개수

	#입력 포스트를 DB포스트들과 title을 비교하여서 중복되지 않으면 add_cnt++, 중복되면 same_cnt++
	for i in range(post_data_prepare_len):
		same_cnt = 0	#중복되는 카운트
		for j in range(posts_db_len):
			#prepare 게시물이 db 게시물과 비교해서 중복되면 same_cnt ++
			hash_before = post_data_prepare[i]['title'] + post_data_prepare[0]['author'] + post_data_prepare[i]['post']
			hash_done = hashlib.md5(hash_before.encode('utf-8')).hexdigest()
			if (db.posts.find({"hashed": hash_done}).count() >= 1):
				same_cnt += 1
				break
			else:
				continue
		if same_cnt == 0:	#중복되지 않으면 추가
			hash_before = post_data_prepare[i]['title'] + post_data_prepare[i]['post']
			query = {
					"hashed" : hash_done,
					"title" : post_data_prepare[i]['title'],
					"author": post_data_prepare[i]['author'],
					"date" : datetime_to_mongo(post_data_prepare[i]['date']),
					"post" : post_data_prepare[i]['post'],
					"img" : post_data_prepare[i]['img'],
					"url" : post_data_prepare[i]['url'],
					"tag" : post_data_prepare[i]['tag'],
					"login" : URL['login'],
					"info" : URL['info'].split("_")[1],
					"view" : 0,
					"fav_cnt": 0
				}
			if URL['info'].split("_")[1] in contest_list:
				query["date"] = datetime_to_mongo(now)
				query["end_date"] = datetime_to_mongo(post_data_prepare[i]['date'])
			db.posts.insert_one(query)
			add_cnt += 1
	return add_cnt

#'info' 의 테이블에 있는 포스트의 개수 반환하는 함수
def get_table_posts(URL):
	#soojle 라는 데이터베이스에 접근
	data = mongo()
	client = MongoClient(data[0], int(data[1]))
	db = client['soojle']

	posts_num = db.posts.find().count()

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