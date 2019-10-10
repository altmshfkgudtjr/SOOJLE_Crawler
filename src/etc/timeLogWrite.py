from datetime import datetime
from platform import platform
from pymongo import MongoClient

def time_write(start_time, end_time, db, posts_len):
	running_time = end_time - start_time
	start_time = start_time.strftime("%Y-%m-%d %H:%M:%S")
	end_time = end_time.strftime("%Y-%m-%d %H:%M:%S")
	posts_data = db.posts.find().count()

	print(":::: CRAWLER TIME INFO ::::")
	print("START : ", start_time)
	print("END   : ", end_time)
	print("RUN   : ", running_time)
	print("\n\n\n\n")
	if platform().startswith("Windows"):
		f = open("./log/crawler_time.log", 'a')
	else:
		f = open("/home/iml/log/crawler_time.log", 'a')
	f_data = "END   : " + end_time + "\n"
	f_data += "RUN   : " + str(running_time) + "\n"
	f_data += "END_DATA   : " + str(posts_data) + "\n"
	f_data += "CRAWLED_DATA    : " + str(posts_data - posts_len) + "\n\n\n\n\n"
	f.write(f_data)
	f.close()

def time_start_write(start_time, db):
	start_time = start_time.strftime("%Y-%m-%d %H:%M:%S")
	posts_data = db.posts.find().count()
	print(":::: CRAWLER TIME INFO ::::")
	print("START : ", start_time)
	print("NOW_DATA : ", posts_data)
	print("\n\n")
	if platform().startswith("Windows"):
		f = open("./log/crawler_time.log", 'a')
	else:
		f = open("/home/iml/log/crawler_time.log", 'a')
	f_data = "\n\n\n:::: CRAWLER TIME INFO ::::\n"
	f_data += "START : " + start_time + "\n"
	f_data += "NOW_DATA : " + str(posts_data) + "\n"
	f.write(f_data)
	f.close()
	return posts_data