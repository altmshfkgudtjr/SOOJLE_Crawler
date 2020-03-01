from datetime import datetime
from platform import platform
from pymongo import MongoClient
from bson.objectid import ObjectId
import copy

def log_write(start_time, end_time, db, BEFORE_DATA):
	# 로그 파일 열기
	if platform().startswith("Windows"):
		f = open("./log/crawler_error.log", 'a')
	else:
		f = open("/home/iml/log/crawler_error.log", 'a')


	# Data 분류
	running_time = end_time - start_time
	posts_data = db.posts.find().count()					# Post Collction 1 포스트 개수
	hidden_posts_data = db.hidden_posts.find().count()		# Post Collction 2 포스트 개수
	all_data = posts_data + hidden_posts_data				# 전체 포스트 개수
	# posts Group By "info"
	classification_to_posts = db.posts.aggregate([
									{"$group": {"_id": "$info", "count": {"$sum": 1}}}
								])
	classification_to_posts = list(classification_to_posts)
	# hidden_posts Group By "info"
	classification_to_hidden = db.hidden_posts.aggregate([
									{"$group": {"_id": "$info", "count": {"$sum": 1}}}
								])
	classification_to_hidden = list(classification_to_hidden)
	classification_all = classification_to_posts + classification_to_hidden
	crawling_classification_all = copy.deepcopy(classification_all)
	for one in crawling_classification_all:
		one['count'] = one['count'] - list(filter(lambda x: one['_id'] == x['_id'], BEFORE_DATA['classification_all']))[0]['count']


	# Shell 출력
	print("END_DATA : ", all_data)
	print("GET_DATA : ", all_data - (BEFORE_DATA['posts_data'] + BEFORE_DATA['hidden_posts_data']))
	print("RUNNING  : ", running_time)
	print("\n\n\n")


	# 파일 입력
	f_data = "----------------------------\n"
	f_data += ":::: CRAWLING SUCCESSFUL ::::\n"
	f.write(f_data)
	f.close()


	# DB 입력
	target = db.crawling_log.find({"date": {"$gte": datetime.strptime(BEFORE_DATA['target'], "%Y-%m-%d")}}).limit(1)
	target = list(target)
	target = target[0]["_id"]
	log = {
		'end_time': end_time,
		'running_time': str(running_time),
		"crawling_data": {
			'all': all_data - BEFORE_DATA['all_data'],
			'posts': posts_data - BEFORE_DATA['posts_data'],
			'hidden_posts': hidden_posts_data - BEFORE_DATA['hidden_posts_data']
		},
		"now_data": {
			'all': all_data,
			'posts': posts_data,
			'hidden_posts': hidden_posts_data
		},
		#"info_crawling": crawling_classification_all,
		"info_crawling": list(filter(lambda x: x['count'] != 0, crawling_classification_all)),
		"info_data": classification_all
	}
	db.crawling_log.update_one({"_id": ObjectId(target)}, {"$set": log})






def log_ready(start_time, db):
	# 로그 파일 열기
	if platform().startswith("Windows"):
		f = open("./log/crawler_error.log", 'a')
	else:
		f = open("/home/iml/log/crawler_error.log", 'a')


	# Data 분류
	start_time = start_time.strftime("%Y-%m-%d")			# 시작시간
	posts_data = db.posts.find().count()					# Post Collction 1 포스트 개수
	hidden_posts_data = db.hidden_posts.find().count()		# Post Collction 2 포스트 개수
	all_data = posts_data + hidden_posts_data				# 전체 포스트 개수
	# posts Group By "info"
	classification_to_posts = db.posts.aggregate([
									{"$group": {"_id": "$info", "count": {"$sum": 1}}}
								])
	classification_to_posts = list(classification_to_posts)
	# hidden_posts Group By "info"
	classification_to_hidden = db.hidden_posts.aggregate([
									{"$group": {"_id": "$info", "count": {"$sum": 1}}}
								])
	classification_to_hidden = list(classification_to_hidden)
	classification_all = classification_to_posts + classification_to_hidden

	
	# Shell 출력
	print(":::: CRAWLER TIME INFO ::::")
	print("TODAY : ", start_time)
	print("NOW_DATA : ", all_data)
	print("\n\n")


	# 파일 입력
	f_data = "\n\n\n:::: CRAWLER ERROR ::::\n"
	f_data += "TODAY : " + start_time + "\n"
	f_data += "----------------------------\n"
	f.write(f_data)
	f.close()


	# DB 입력
	log = {
		"start_time": datetime.now(),
	}
	db.crawling_log.insert_one(log)


	# 반환 데이터
	output = {
		'target': start_time,
		'posts_data': posts_data,
		'hidden_posts_data': hidden_posts_data,
		'all_data': posts_data + hidden_posts_data,
		'classification_all': classification_all
	}
	return output