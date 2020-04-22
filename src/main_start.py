"""     2019.02.10		"""
"""   SooJel Project	"""
""" BY *IML *NB *837477 """
# python3 main_start <시작위치:int> <끝위치:int> <제외:list>

import sj_path	#환경변수 지정
from url_list import List
from crawling_select import Crawling	#크롤링 전체
import db_manager
from db_url import init_url_collection
from db_date import init_date_collection
from db_crawler import *
from date_cut import date_init
from datetime import datetime
from info_id import post_info
from posts_cnt import posts_cnt
from tag_info import tag_info
from db_connect import *
from datetime import datetime, timedelta
from timeLogWrite import log_write, log_ready
from error_handler import error_handler, error_logging
from domain_insert import domain_insert

#시작위치 및 끝 위치 입력 설정
ST_NUM = None
END_NUM = None
if len(sys.argv) == 1:
	pass
elif len(sys.argv) == 2:
	ST_NUM = int(sys.argv[1])
elif len(sys.argv) == 3:
	ST_NUM = int(sys.argv[1])
	END_NUM = int(sys.argv[2])
else:
	print(":::: WRONG INPUT ::::\n\n\n")

#프로그램 시작시간
start_time = datetime.now()

#DB 연결
database = connect_db()
db = database[1]
client = database[0]

#url_list에서 List를 URL으로 가져옴
if ST_NUM == None and END_NUM == None:
	URLS = List[:]
elif ST_NUM != None and END_NUM == None:
	URLS = List[ST_NUM:]
elif ST_NUM == None and END_NUM != None:
	URLS = List[:END_NUM]
else:
	URLS = List[ST_NUM:END_NUM]


if __name__ == '__main__':
	print("\n\n")
	print(":::< SooJle Project >:::")
	print("TODAY : ", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "\n\n")


	#post_info 테이블, sj_domain 테이블 생성, lastly_post 테이블 생성
	post_info(db)
	#tag_info 테이블 생성
	tag_info(db)
	#url 테이블 생성
	init_url_collection(db)
	#date 테이블 생성 밎 dictionary화
	init_date_collection(db)
	#date 생성
	date_init(db)
	#crawler 관리 테이블 생성
	init_crawler_collection(db)
	#Post_Info 전역변수생성
	db_manager.get_post_infoes(db)
	#도메인 생성
	domain_insert(db)


	#크롤러 관리자 갱신==========================
	CRAWLER_MANAGER = get_crawler_manager(db)
	#===========================================


	#현재 크롤링 가능 여부 확인
	if Can_crawling(db):
		print("\n\nCrawling Start!\n\n")
		CRAWLER_MANAGER['crawling'] = True
		CRAWLER_MANAGER['start_time'] = start_time
		update_crawler_manager(db, CRAWLER_MANAGER)
		#시작시간 Logging
		BEFORE_DATA = log_ready(start_time, db)
		# 가능한 info 가져오기
		INFO_LIST = get_crawler_timeinfo(db)

		for URL in URLS:	#List에서 하나의 요소 = URL
			if not (URL['info'] in INFO_LIST):
				print('URL parsing Skip! : ' + str(URL["url"]))
				print('-----------------------------------------------------------------------------------------------------------------\n')
				continue
			try:
				print('URL parsing Start! : ' + str(URL["url"]))
				Crawling(URL, db)
				print('-----------------------------------------------------------------------------------------------------------------\n')
			except Exception as e:
				error_handler(e, URL, URL["url"], db)
				continue

		print(":::: Posts in Boards Count ::::")
		posts_cnt(db)															# 모든 게시물 빈도 출력

		print("\n\nCrawling End!\n\n")

		#프로그램 종료시간
		end_time = datetime.now()
		try:
			log_write(start_time, end_time, db, BEFORE_DATA)
		except:
			error_logging(e, '', '', db)

		#크롤러 관리자 갱신==========================
		CRAWLER_MANAGER['crawling'] = False
		CRAWLER_MANAGER['end_time'] = end_time
		update_crawler_manager(db, CRAWLER_MANAGER)
		#===========================================
	else:
		print("\n\nNow Crawling!\n\n")


	#DB 연결해제
	disconnect_db(client)