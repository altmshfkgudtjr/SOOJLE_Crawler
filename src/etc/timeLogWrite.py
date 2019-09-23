from datetime import datetime
from platform import platform

def time_write(start_time, end_time):
	running_time = end_time - start_time
	start_time = start_time.strftime("%Y-%m-%d %H:%M:%S")
	end_time = end_time.strftime("%Y-%m-%d %H:%M:%S")

	print(":::: CRAWLER TIME INFO ::::")
	print("START : ", start_time)
	print("END   : ", end_time)
	print("RUN   : ", running_time)
	print("\n\n\n\n")
	if platform().startswith("Windows"):
		f = open("/home/iml/log/crawler_time.log", 'a')
	else:
		f = open("crawler_time.log", 'a')
	f_data = ":::: CRAWLER TIME INFO ::::\n"
	f_data += "START : " + start_time + "\n"
	f_data += "END   : " + end_time + "\n"
	f_data += "RUN   : " + running_time + "\n\n\n\n"
	f.write(f_data)
	f.close()