import MySQLdb
import all_login



#MySQL 로그인 정보
login_data = all_login.mysql()
mysqlid = login_data[0]
mysqlpw = login_data[1]

#MySQL 서버에 로그인하고 연결하는 작업
def server():
	connect = MySQLdb.connect(host='localhost', user=mysqlid, password=mysqlpw,charset='utf8mb4')
	return connect
#MySQL 서버에 로그인하고 DB와 연결하는 작업
def db():
	connect = MySQLdb.connect(host='localhost', user=mysqlid, password=mysqlpw, db='soojle', charset='utf8mb4')

	return connect