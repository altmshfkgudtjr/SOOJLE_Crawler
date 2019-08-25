import MySQLdb
import connect_db
from url_list import List



#현재 서버의 테이블의 게시글 수를 출력해주는 함수
def posts_cnt():
	all_cnt = 0
	connect = connect_db.db()
	cur = connect.cursor()
	
	query = "SELECT count(*) FROM posts"
	cur.execute(query)
	connect.commit()
	posts = cur.fetchone()

	print("\nAll Posts Count :::: ", posts[0])
	'''
	for num in List:
		info = num['info']
	
		query = "SELECT title FROM posts"
		cur.execute(query)
		connect.commit()
		posts = cur.fetchall()
	
		post_cnt = len(posts)
		
		percent = int(round(post_cnt/all_cnt, 3)*100)


		info_out = info + " ============================================================================================="
		print("\n",info_out[:40], end = " ")
		print("Count :::: ", post_cnt)
		num = round(post_cnt/all_cnt, 3)*100
		num = int(num * 10)
		num = round(num/10, 1)
		print(num, "%")
		for i in range(percent):
			print("■", end = " ")
	'''