from bs4 import BeautifulSoup
from url_parser import URLparser
from url_parser import URLparser_EUCKR
from url_parser import URLparser_UTF8
from db_manager import db_manager
from db_manager import get_lastly_post
from db_manager import push_lastly_post
from date_cut import date_cut
from datetime import datetime
import time
import sj1, sj2, sj3, sj4, sj5, sj6, sj7, sj8, sj9, sj10, sj11, sj12, sj13, sj14, sj15, sj16, sj17, sj18,\
 sj19, sj20, sj21, sj23, sj24, sj25, sj26, sj27, sj28, sj29, sj30, sj31, sj32, sj33, sj34, sj35



def Crawling(URL):
	info_name = URL['info'].split('_')
	crawling_name = info_name[0]	#게시판 크롤링 선택
	page = 1
	main_url = URL['url']	#게시판 url 추출 : 페이지 바꾸는 데에 사용
	page_url = eval(crawling_name + '.Change_page(main_url, page)')	#현재 페이지 포스트 url 반환
	end_date = date_cut(URL['info'])	# end_date 추출
	if crawling_name == 'sj23' or crawling_name == 'sj26' or crawling_name == 'sj27' or crawling_name == 'sj28' or crawling_name == 'sj36':
		lastly_post = get_lastly_post(URL)
	elif crawling_name == 'sj34':	# 동적 게시판 예외
		sj34.everytime_all_board(URL, end_date)
		return

	#현재 크롤링하는 게시판 info 출력
	print("Target : ", URL['info'])

	flag = False
	while True:
		try:
			print("\npage_url :::: ", page_url)	#현재 url 출력
			print("Page : ", page)				#현재 페이지 출력
			#driver_page 생성---------------------------
			if crawling_name == 'sj10':
				driver_page = URLparser_EUCKR(page_url)
			elif crawling_name == 'sj12':
				driver_page = URLparser_UTF8(page_url)
			else:
				driver_page = URLparser(page_url)
			#-------------------------------------------
			#Selenium을 쓰는 경우----------------------------------------------------------------------------------------------
			if crawling_name == 'sj23' or crawling_name == 'sj26' or crawling_name == 'sj27' or crawling_name == 'sj28' or crawling_name == 'sj36'\
			 or crawling_name == 'sj29' or crawling_name == 'sj30':
				data = eval(crawling_name + '.Parsing_list_url(URL, page_url)')
				driver = data[0]
				post_urls = data[1]
			#Requests를 쓰는 경우----------------------------------------------------------------------------------------------
			else:
				#로그인을 하는 경우-------------------------------------------------------------------------------
				if URL['login'] == '1':
					post_urls = eval(crawling_name + '.Parsing_list_url(URL, page_url)')
				#로그인을 하지않는 경우---------------------------------------------------------------------------
				else:
					if driver_page is None:		#Connect Failed 이면 break
						break
					else:
						#parsing 형태--------------------------------------------------
						if crawling_name == 'sj10':
							bs_page = BeautifulSoup(driver_page, 'lxml')
						else:
							bs_page = BeautifulSoup(driver_page, 'html.parser')
						#--------------------------------------------------------------
					post_urls = eval(crawling_name + '.Parsing_list_url(URL, bs_page)')
				#-----------------------------------------------------------------------------------------------
			#-----------------------------------------------------------------------------------------------------------------
			#get_post_data 형식 : [게시글정보dictionary, title, date]-------------------------------------------------------------------------------------------------------
			#date 규격은 "0000-00-00 00:00:00"
			post_data_prepare = []
			for post_url in post_urls:
				#Selenium인 경우--------------------------------------------------------------------------------------------------------------------
				if crawling_name == 'sj29' or crawling_name == 'sj30':#------------------게시판 규격인 경우
					get_post_data = eval(crawling_name + '.Parsing_post_data(driver, post_url, URL)')
				#---------------------------------------------------------------------------------------------------게시판 규격이 아닌 경우
				elif crawling_name == 'sj23' or crawling_name == 'sj26' or crawling_name == 'sj27' or crawling_name == 'sj28' or crawling_name == 'sj36':
					data = eval(crawling_name + '.Parsing_post_data(driver, post_url, URL, lastly_post)')
					post_data_prepare = data[0]
					lastly_post = data[1]
					if lastly_post is None:
						pass
					else:
						push_lastly_post(URL, lastly_post)
				#Requests인 경우--------------------------------------------------------------------------------------------------------------------
				else:
					#driver_post 생성--------------------------------
					if (crawling_name == 'sj21') or (crawling_name == 'sj4') or (crawling_name == 'sj5') or (crawling_name == 'sj8') or (crawling_name == 'sj16'): #---driver_post가 필요없는 경우
						pass
					elif crawling_name == 'sj10' or crawling_name == 'sj33':
						driver_post = URLparser_EUCKR(post_url)
					elif crawling_name == 'sj12':
						driver_post = URLparser_UTF8(post_url)
					else:
						driver_post = URLparser(post_url)
					#------------------------------------------------
					#-----------------------------------------------------------------------------------------------위키백과 구조
					if crawling_name == 'sj21':
						get_post_data = eval(crawling_name + '.Parsing_post_data(post_url, URL)')
					#-----------------------------------------------------------------------------------------------게시판 규격이 아닌 구조
					elif (crawling_name == 'sj4') or (crawling_name == 'sj5') or (crawling_name == 'sj8') or (crawling_name == 'sj16'):
						post_data_prepare = eval(crawling_name + '.Parsing_post_data(post_url, URL)')
						break
					#-----------------------------------------------------------------------------------------------게시판 규격인 구조
					else:
						if driver_post is None:		#Connect Failed 이면 continue
							continue
						else:
							#parsing 형태-------------------------------------------
							if crawling_name == 'sj10':
								bs_post = BeautifulSoup(driver_post, 'lxml')
							elif crawling_name == 'sj12':
								bs_post = driver_post
							else:
								bs_post = BeautifulSoup(driver_post, 'html.parser')
							#-------------------------------------------------------
						get_post_data = eval(crawling_name + '.Parsing_post_data(bs_post, post_url, URL)')
				#-----------------------------------------------------------------------------------------------------------------------------------
				
				#post_data_prepare이 이미 완성된 경우-----------------------------------------------------------------------
				if crawling_name == 'sj4' or crawling_name == 'sj5' or crawling_name == 'sj8' or crawling_name == 'sj16'\
				 or crawling_name == 'sj23' or crawling_name == 'sj26' or crawling_name == 'sj27' or crawling_name == 'sj28' or crawling_name == 'sj36':
					pass
				#post_data_prepare이 완성되지 않은 경우---------------------------------------------------------------------
				else:
					title = get_post_data[1]
					date = get_post_data[2]
		
					print(date, "::::", title)	#현재 크롤링한 포스트의 date, title 출력
		
					#게시물의 날짜가 end_date 보다 옛날 글이면 continue, 최신 글이면 append
					if str(date) <= end_date:
						continue
					else:
						post_data_prepare.append(get_post_data[0])
			#----------------------------------------------------------------------------------------------------------
			#--------------------------------------------------------------------------------------------------------------------------------------------------------------
			add_cnt = db_manager(URL, post_data_prepare)
			print("add_OK : ", add_cnt)	#DB에 저장된 게시글 수 출력
		
			#dirver 종료 [Selenium 을 사용했을 시]
			if crawling_name == 'sj23' or crawling_name == 'sj26' or crawling_name == 'sj27' or crawling_name == 'sj28' or crawling_name == 'sj36'\
			 or crawling_name == 'sj29' or crawling_name == 'sj30':
				driver.quit()
			
			#DB에 추가된 게시글이 0 이면 break, 아니면 다음페이지
			if add_cnt == 0:
				break
			else:
				page += 1
				page_url = eval(crawling_name + '.Change_page(main_url, page)')
		except Exception as e:
			log_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			log_info = URL['info']
			log_url = page_url
			print("[ERROR]=====================================================================")
			print(log_time, " :: ", log_info, "\nURL :: ", log_url)
			print(type(e), "\n", e, "\n\n\n\n")
			f = open("log.txt", 'a')
			f_data = "[ERROR]=====================================================================\n"
			f_data = f_data + log_time + " :: " + log_info + "\nURL :: " + log_url + "\n"
			f_data = f_data + str(type(e)) + "\n" + str(e) + "\n\n"
			f.write(f_data)
			f.close()
			time.sleep(2)
			if flag is False:
				flag = True
				continue
			else:
				break