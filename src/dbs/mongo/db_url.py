from url_list import List
from pymongo import MongoClient

def init_url_collection(db):
	#soojle 라는 데이터베이스에 접근

	if db.url.find().count() == 0:
		for component in List:
			query = {
				"url": component['url'],
				"info": component['info'],
				"title_tag": component['title_tag'],
				"login": component['login']
			}
			if "post_url" in component:
				query["post_url"] = component['post_url']
			db.url.insert_one(query)
	print(":::: url CREATE Complete! ::::")