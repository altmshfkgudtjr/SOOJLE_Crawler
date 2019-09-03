from pymongo import MongoClient
from all_login import mongo
from date_cut import date_cut_dict_before
from datetime import datetime, timedelta

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
now_minus = datetime.now() + timedelta(days = -1)
now_minus = now_minus.strftime("%Y-%m-%d %H:%M:%S")

def init_date_collection():
	data = mongo()
	client = MongoClient(data[0], int(data[1]))
	db = client['soojle']

	if db.date.find().count() == 0:
		for date_one in date_cut_dict_before.items():
			query = {
				"crawler": date_one[0],
				"date_exp": date_one[1]
			}
			db.date.insert_one(query)
	print(":::: date CREATE Complete! ::::")