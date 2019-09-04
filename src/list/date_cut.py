from datetime import datetime, timedelta
from pymongo import MongoClient
from all_login import mongo

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
now_minus = datetime.now() + timedelta(days = -1)
now_minus = now_minus.strftime("%Y-%m-%d %H:%M:%S")


date_cut_dict = {}

date_cut_dict_before = {
	"sj1": "2019-08-01 00:00:00",\
	"sj1_main_FAQ": "2006-01-01 00:00:00",\
	"sj2": "2019-08-01 00:00:00",\
	#마감날짜 기준이므로 항상 현재까지만 긁는다.
	"sj3": now,\
	#마감날짜 기준이므로 항상 현재까지만 긁는다.
	"sj4": now,\
	"sj5": "2019-08-01 00:00:00",\
	"sj6": "2019-08-01 00:00:00",\
	"sj7": "2019-08-01 00:00:00",\
	"sj8": "2019-08-01 00:00:00",\
	"sj9": "2019-08-01 00:00:00",\
	"sj10": "2019-08-01 00:00:00",\
	"sj11": "2019-08-01 00:00:00",\
	"sj12": "2019-08-01 00:00:00",\
	"sj13": "2019-08-01 00:00:00",\
	"sj14": "2019-08-01 00:00:00",\
	"sj15": "2019-08-01 00:00:00",\
	"sj16": "2019-08-01 00:00:00",\
	"sj17": "2019-08-01 00:00:00",\
	"sj18": "2019-08-01 00:00:00",\
	"sj19": "2019-08-01 00:00:00",\
	"sj20": "2019-08-01 00:00:00",\
	"sj21": "2019-08-01 00:00:00",\
	"sj23": "2019-08-04 00:00:00",\
	"sj24": "2019-08-01 00:00:00",\
	#마감날짜 기준이므로 항상 현재까지만 긁는다.
	"sj25": now,\
	"sj26": now_minus,\
	"sj27": "2019-08-01 00:00:00",\
	"sj28": now_minus,\
	"sj29": "2019-08-01 00:00:00",\
	"sj30": "2019-08-01 00:00:00",\
	"sj31":	now,\
	"sj32": "2019-08-01 00:00:00",\
	"sj33": "2019-08-01 00:00:00",\
	"sj34": "2019-08-01 00:00:00",\
	"sj35": now,\
	"sj36": "2019-08-01 00:00:00",\
	"sj37": now,\
	"sj38": "2017-08-01 00:00:00"\
}

def date_init():
	data = mongo()
	client = MongoClient(data[0], int(data[1]))
	db = client['soojle']

	date_db = db.date.find()
	for date_one in date_db:
		date_cut_dict[date_one['crawler']] = date_one['date_exp']



def date_cut(info):
	if info.split("_")[2].find("FAQ") != -1:		#FAQ이므로 전체긁기를 위해 예외처리
		end_date = date_cut_dict['sj1_main_FAQ']
	else:
		name = info.split("_")[0]
		end_date = date_cut_dict[name]

	return end_date