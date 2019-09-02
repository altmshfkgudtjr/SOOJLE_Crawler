from url_list import List
from pymongo import MongoClient
from all_login import mongo


def init_url_collection():
	data = mongo()
	client = MongoClient(data[0], int(data[1]))
	db = client['soojle']

	if db.url.find().count() == 0:
		for component in List:
			print("1")
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

'''
{'url': "http://udream.sejong.ac.kr/Community/Notice/NoticeList.aspx?rp=",\
	'post_url': "https://udream.sejong.ac.kr/Community/Notice/NoticeView.aspx?nnum=",\
	'info': "sj2_udream_notice",\
	'title_tag' : "취업&진로/", 'login' : "1"},\
'''