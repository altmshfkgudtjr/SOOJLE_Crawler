from bs4 import BeautifulSoup
from url_parser import URLparser
from db_manager import db_manager
from selenium import webdriver
from post_wash import post_wash
import datetime
import tag
import everytime
import time
from driver_agent import chromedriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from img_size import img_size



#게시판 page_url 을 받으면, 그 페이지의 포스트 url 들을 반환
def Parsing_list_url(main_url, page_url, driver):
	List = []
	domain = main_url

	driver.get(page_url)

	WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.article")))
	html = driver.page_source
	bs = BeautifulSoup(html, 'html.parser')
	
	posts = bs.find("div", {"class": 'wrap articles'}).findAll("article")
	if len(posts) == 1:		#게시물이 아무것도 없는 경우
		pass
	else:
		for post in posts:
			url = post.find("a")['href']
			url = domain + url
			List.append(url)

	data = (driver, List)

	return data



#포스트 url을 받으면, 그 포스트의 정보를 dictionary 형태로 반환
def Parsing_post_data(driver, post_url, URL, board_tag):
	return_data = []
	post_data = {}
	domain = Domain_check(URL['url'])
	

	driver.get(post_url)

	try:
		WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, "time.large"))) #time.large를 발견하면 에이작스 로딩이 완료됬다는 가정
	except:
		try:
			WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, "time.large")))
		except:
			return return_data;
	html = driver.page_source
	bs = BeautifulSoup(html, 'html.parser')
	
	if URL['info'].split("_")[2] == 'free' or URL['info'].split("_")[2] == 'notice' or URL['info'].split("_")[2] == 'jobinfo' or URL['info'].split("_")[2] == 'promotion'\
or URL['info'].split("_")[2] == 'club' or URL['info'].split("_")[2] == 'trade':
		title = bs.find("h2", {"class": "large"}).text.strip()
	else:
		title = "!@#$soojle-notitle" + bs.find("p", {'class': "large"}).text.strip()
		if len(title) >= 300:
			title = title[:299]

	author = "0"
	date = bs.find("time").text.strip()
	date = everytime_time(date)
	post = bs.find("p", {'class': "large"}).text.strip()
	post = post_wash(post)		#post 의 공백을 전부 제거하기 위함
	post = post[:3000]	#post글을 3000자 까지 읽기위한 작업
	tag_done = tag.tagging(URL, title) + "/" + board_tag.replace(" ", "")
	if bs.find("figure", {"class": "attach"}) is not None:
		try:
			img = bs.find("figure", {"class": "attach"}).find("img")['src']		#게시글의 첫번째 이미지를 가져옴.
			if 1000 <= len(img):
				img = 5
			else:
				if img.startswith("http://") or img.startswith("https://"):		# img가 내부링크인지 외부 링크인지 판단.
					pass
				elif img.startswith("//"):
					img = "http:" + img
				else:
					img = domain + img
		except:
			img = 5
	else:
		img = 5
	if img != 5:
		if img_size(img):
			pass
		else:
			img = 5
		

	#post_data = {'title': ,'author': ,'date': ,'post': ,'tag':[],'fav_cnt':0,'view':0} 같은 형식
	post_data['title'] = title.upper()
	post_data['author'] = author.upper()
	post_data['date'] = date
	post_data['post'] = post.upper()
	post_data['tag'] = tag_done 	# 태그1/태그2/태그3/태그4/.../ 같은 형식의 태그string이 들어간다.
	post_data['img'] = img
	post_data['url'] = post_url

	return_data.append(post_data)
	return_data.append(title)
	return_data.append(date)
	return return_data



#url을 받으면 Page를 변환시켜서, 변환된 url 반환
def Change_page(url, page):
	url_done = url + '/p/' + str(page)

	return url_done


#입력된 url의 도메인 url 반환
def Domain_check(url):
	domain = url.split('/')[0] + '//' + url.split('/')[2]	#도메인 url 추출

	return domain


#현재 시간 계산하는 함수
def everytime_time(text):
	if text == "방금":																	#방금 형태
		date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	elif text.find("분 전") != -1:														#n분 전 형태
		text_minutes = text.split("분")[0]
		date = datetime.datetime.now() - datetime.timedelta(minutes = int(text_minutes))
		date = date.strftime("%Y-%m-%d %H:%M:%S")
	elif len(text.split("/")) == 3:														#18/12/31 00:00 형태
		year = text.split("/")[0]
		month = text.split("/")[1]
		day = text.split("/")[2]
		date = "20" + year + "-" + month + "-" + day + ":00"
	else:																				#12/31 00:00 형태
		now_year = datetime.datetime.now().strftime("%Y")
		date = now_year + "/" + text + ":00"
		year = date.split("/")[0]
		month = date.split("/")[1]
		day = date.split("/")[2]
		date = year + "-" + month + "-" + day

	return date

def everytime_all_board(URL, end_date):
	main_url = URL['url']
	board_search_url = "https://everytime.kr/community/search?keyword="
	board_search_word = ['게시판', '갤러리']
	board_list = []
	# driver 연결
	driver = chromedriver()
	driver = everytime.login(driver)

	WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.article")))
	html = driver.page_source
	bs = BeautifulSoup(html, 'html.parser')

	# 에브리타임 상단 동적 게시판 긁기
	board_group_list = bs.find("div", {"id": "submenu"}).findAll('div', {"class": "group"})
	for board_group in board_group_list:
		board_li_list = board_group.find("ul").findAll("li")
		for board_li in board_li_list:
			board_li_dic = {}
			board_li_dic['tag'] = board_li.find("a").text
			board_li_dic['url'] = main_url + board_li.find("a")['href']
			if (board_li_dic['tag'].find("찾기") != -1):
				continue
			board_list.append(board_li_dic)
	# 에브리타임 추가 동적 게시판 긁기
	for search_word in board_search_word:
		board_search_url_done = board_search_url + search_word
		driver.get(board_search_url_done)
		WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.result")))
		html = driver.page_source
		bs = BeautifulSoup(html, 'html.parser')
		board_a_list = bs.find("div", {"class": "searchresults"}).findAll('a')
		for board_a in board_a_list:
			board_li_dic = {}
			board_li_dic['tag'] = board_a.find("h3").text
			board_li_dic['url'] = main_url + board_a.get('href')
			board_list.append(board_li_dic)
	
		# 동적 게시판들 반복문
		for board in board_list:
			page = 1
			board_url = board['url']
			page_url = Change_page(board_url, page)	#현재 페이지 포스트 url 반환
			print("\nTarget : ", URL['info'], " :: ", board['tag'])
	
			flag = False
			# 페이지 반복문
			while True:
				print("page_url :::: ", page_url)	#현재 url 출력
				print("Page : ", page)				#현재 페이지 출력
	
				data = Parsing_list_url(main_url, page_url, driver)
				driver = data[0]
				post_urls = data[1]
				# everytime 고질병 문제 고려, 재시도
				if len(post_urls) == 0:
					time.sleep(2)
					data = Parsing_list_url(main_url, page_url, driver)
					driver = data[0]
					post_urls = data[1]
	
				post_data_prepare = []
				# 포스트 반복문
				for post_url in post_urls:
					get_post_data = Parsing_post_data(driver, post_url, URL, board['tag'])
	
					title = get_post_data[1]
					date = get_post_data[2]
		
					print(date, "::::", title)	#현재 크롤링한 포스트의 date, title 출력
		
					#게시물의 날짜가 end_date 보다 옛날 글이면 continue, 최신 글이면 append
					if str(date) <= end_date:
						continue
					else:
						post_data_prepare.append(get_post_data[0])
	
				add_cnt = db_manager(URL, post_data_prepare)
				print("add_OK : ", add_cnt)	#DB에 저장된 게시글 수 출력
	
				#DB에 추가된 게시글이 0 이면 break, 아니면 다음페이지
				if add_cnt == 0:
					break
				else:
					page += 1
					page_url = Change_page(board_url, page)