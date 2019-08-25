import datetime
import time



#datetime 타입을 unixtime 타입으로 convert
def datetime_to_unixtime(before_time):
	dtime = datetime.datetime.strptime(before_time, "%Y-%m-%d %H:%M:%S")
	after_time = int(time.mktime(dtime.timetuple()))
	
	return after_time

#unixtime 타입을 datetime 타입으로 convert
def unixtime_to_datetime(before_time):
	after_time = datetime.datetime.fromtimestamp(before_time).strftime("%Y-%m-%d %H:%M:%S")
	
	return after_time