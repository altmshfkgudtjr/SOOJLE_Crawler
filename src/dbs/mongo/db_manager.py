from pymongo import MongoClient
from time_convert import datetime_to_mongo
from time_convert import mongo_to_datetime
import filtering
from url_list import List
from datetime import datetime
import hashlib
from tknizer import *


#md5 해쉬
enc = hashlib.md5()

#공모전 ~까지를 위한 collum 생성
contest_list = ["campuspick", "detizen", "jobkorea", "jobsolution", "thinkgood"]
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def collection_indexing(db):
	#콜렉션 인덱싱 작업
	db.posts.createIndex({"hashed":1})
	db.posts.createIndex({"date":1})
	db.posts.createIndex({"end_date":1})


def init_db(db):
	#soojle 라는 데이터베이스에 접근
	print()

def get_lastly_post(URL, db):
	#soojle 라는 데이터베이스에 접근

	table_name = URL['info']
	document = db.lastly_post.find_one({"info_id": table_name})
	lastly_post_title = document['title']

	return lastly_post_title

def push_lastly_post(URL, lastly_post_title, db):
	#soojle 라는 데이터베이스에 접근

	table_name = URL['info']
	db.lastly_post.update_one({"info_id": table_name}, {'$set': {"title": lastly_post_title}})
	print("\n\n:::: lastly_post INSERT Complete! ::::\n\n")


def db_manager(URL, post_data_prepare, db):
	add_cnt = 0
	#table_name = URL['info']
	table_name = "posts"
	temp = []
	
	#soojle 라는 데이터베이스에 접근

	#게시판에 맞는 테이블 없으면 생성
	##### post_id: 게시물 식별값, title: 제목, author: 작성자, date: 작성일, post: 게시물내용, img: OpenGraph용 url #####
	##### tag: 태그, info: 게시판 정보, fav_cnt: 좋아요개수, view: view 개수										 #####
	#post_data_prepare 을 필터링 check를 해준다.
	for post in post_data_prepare:
		if filtering.filter_public(post['title'] + post['post']):
			print("Unhealty Post ---- ", post['title'])
		elif URL['info'].split('_')[0] == 'sj20' or  URL['info'].split('-')[0] == 'sj34':
			if filtering.filter_hardcore(post['title'] + post['post']):
				print("Harmful Post ---- ", post['title'])
			else:
				temp.append(post)
		else:
			temp.append(post)
	post_data_prepare = temp

	#post_data_prepare 에 값이 없으면 return
	post_data_prepare_len = len(post_data_prepare)
	if post_data_prepare_len == 0:
		return add_cnt

	#한 페이지에 title 이 중복되는 것이 있으면 걸러주는 함수
	post_data_prepare = sameposts_set(post_data_prepare)

	#입력 포스트를 DB포스트들과 title을 비교하여서 중복되지 않으면 add_cnt++, 중복되면 same_cnt++
	for post_one in post_data_prepare:
		#prepare 게시물이 db 게시물과 비교해서 중복되면 same_cnt ++
		hash_before = post_one['title'] + post_one['post']
		hash_done = hashlib.md5(hash_before.encode('utf-8')).hexdigest()
		if db.posts.find_one({"hashed": hash_done}) != None:
			continue
		else:
			post_one["title"] = post_one["title"][:200]
			post_one["hashed"] = hash_done
			post_one["date"] = datetime_to_mongo(post_one['date'])
			post_one["post"] = post_one["post"]#[:200]
			if URL['info'].split("_")[1] != 'everytime':
				post_one["info"] = URL['info'].split("_")[1] + "_" + URL['info'].split("_")[2]
			post_one["view"] = 0
			post_one["fav_cnt"] = 0
			post_one["title_token"] = post_one["title"].split(" ")
			post_one["token"] = get_tk(post_one["title"] + post_one["post"])
			post_one["login"] = URL["login"]
			post_one["learn"] = 0
			del post_one["author"]
			if URL['info'].split("_")[1] in contest_list:
				post_one["end_date"] = post_one['date']
				post_one["date"] = datetime_to_mongo(now)
			db.posts.insert_one(post_one)
			add_cnt += 1
	return add_cnt

#'info' 의 테이블에 있는 포스트의 개수 반환하는 함수
def get_table_posts(URL, db):
	#soojle 라는 데이터베이스에 접근

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
