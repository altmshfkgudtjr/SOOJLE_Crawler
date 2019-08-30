from pymongo import MongoClient
from all_login import mongo

def posts_time_sort():
	#soojle 라는 데이터베이스에 접근
	data = mongo()
	client = MongoClient(data[0], int(data[1]))
	db = client['soojle']

	#Date 를 내림차순으로 정렬
	db.posts.find().sort({"date": -1})
	print("\n\n:::: posts SORT DONE! ::::\n\n")