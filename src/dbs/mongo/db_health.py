from pymongo import MongoClient

# 현재 Crawling Site 가 접속이 가능한지 유무 판단해서 true or false 추가
def url_health_check(target_url, db):
	#soojle 라는 데이터베이스에 접근

	target_id = None
	db_url_list = db.url.find({}, {"url":1})
	for db_url in db_url_list:
		if db_url["url"] in target_url:
			target_id = db_url["_id"]
			break
	target_obj = db.posts.find({"_id": target_id})
	if "stay_cnt" in target_obj:
		target_cnt = target_obj["stay_cnt"]
		if target_cnt > 0:
			db.posts.update_one({"_id": target_id}, {"$set", {"stay_cnt": target_cnt - 1}})
		else:
			db.posts.update_one({"_id": target_id}, {"$set", {"crawling": False, "stay_cnt": 10}})
	print()
	db.posts.update_one({"_id": target_id}, {"$set": {"crawling": False, "stay_cnt": 10}})
	print("\n:::: THIS URL CAN NOT CRAWLED! ::::\n")

# 만약 stay_cnt 가 0 인 것이 있으면 이제부터 긁을 것
def url_health_change(db):
	#soojle 라는 데이터베이스에 접근

	db_url_list = db.url.find({}, {"crawling":1, "stay_cnt":1})
	for db_url in db_url_list:
		if "crawling" not in db_url:
			continue
		elif db_url['crawling'] == False and db_url['stay_cnt'] == 0:
			target_id = db_url['_id']
			db.posts.update_one({"_id": target_id}, {"crawling": True})
	print(":::: URL HEALTH CHECK Complete! ::::")