from pymongo import MongoClient
from date_cut import date_cut_dict_before
from datetime import datetime, timedelta

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
now_minus = datetime.now() + timedelta(days = -1)
now_minus = now_minus.strftime("%Y-%m-%d %H:%M:%S")

def init_date_collection(db):
	if db.date.find().count() == 0:
		for date_one in date_cut_dict_before.items():
			query = {
				"crawler": date_one[0],
				"date_exp": date_one[1]
			}
			db.date.insert_one(query)
	print(":::: date CREATE Complete! ::::")