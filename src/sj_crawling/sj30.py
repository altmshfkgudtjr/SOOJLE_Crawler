from bs4 import BeautifulSoup
from url_list import List
from post_wash import post_wash
import datetime
import tag
import daum
from driver_agent import chromedriver
from date_cut import date_cut
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from img_size import img_size
from date_cut import date_cut
from datetime import datetime
from db_manager import push_lastly_post



#게시판 page_url 을 받으면, 그 페이지의 포스트 url 들을 반환
def Parsing_list_url(URL, page_url, lastly_post):
	List = []
	domain = Domain_check(URL['url'])
	end_date = date_cut(URL['info'])
	lastly_num = 0		#한번만 실행하기위한 조건변수
	#lastly_post = get_lastly_post(URL)	#lastly_post 가져온다

	#만약 driver이 켜져있으면 끄고, 없으면 그냥 진행
	try:
		driver.quit()
	except:
		pass

	driver = chromedriver()
	#다음 로그인함수
	driver = daum.login(driver)

	#페이지 구조 변경 예외
	if URL['info'] == "sj30_sejongstation_news":
		data = (driver, List)
		return data
		
	driver.get(page_url)
	try:
		WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, "td.headcate")))
	except:
		data = (driver, List)
		return data
	num = 1
	while 1:
		cnt = 0
		if URL['info'].split("_")[2] == 'qna':
			query = '//*[@id="primaryContent"]/table/tbody/tr[2]/td[2]/div[3]/div/a[' + str(num) + ']'
		else:
			query = '//*[@id="primaryContent"]/table/tbody/tr[2]/td[2]/div[2]/div/a[' + str(num) + ']'
		driver.find_element_by_xpath(query).click()
		WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, "td.headcate")))
		html = driver.page_source
		bs = BeautifulSoup(html, 'html.parser')
		posts = bs.find("table", {"class": "bbsList"}).find("tbody").findAll("tr")

		for post in posts:
			if post.find("td", {"class": "num"}).find("img") != None:
				continue
			title = post.find("td", {"class": "subject"}).find("a").text.strip()
			date = post.find("td", {"class": "date"}).text.strip()
			if date.find(":") != -1:
				now = datetime.now().strftime("%Y-%m-%d")
				date = now + " 00:00:00"
			else:
				date = "20" + date + " 00:00:00"
				date = str(datetime.strptime(date, "%Y.%m.%d %H:%M:%S"))

			if date + title == lastly_post:		#이전 최근 글을 만나면, cnt = 0, break 를 함으로서 만나기 전까지의 List를 보낸다.
				cnt = 0
				lastly_num = 1
				break
			elif end_date <= date:
				url = post.find("td", {"class": "subject"}).find("a")['href']
				url = domain + url
				List.append(url)
				cnt += 1


		#항상 첫번째페이지의 공지를 제외한 첫번째글이 lastly_post가 되도록 지정해줌
		if lastly_num == 1 or lastly_post == '0':
			for post in posts:
				if post.find("td", {"class": "num"}).find("img") != None:
					continue
				title = post.find("td", {"class": "subject"}).find("a").text.strip()
				date = post.find("td", {"class": "date"}).text.strip()
				if date.find(":") != -1:
					now = datetime.now().strftime("%Y-%m-%d")
					date = now + " 00:00:00"
				else:
					date = "20" + date + " 00:00:00"
					date = str(datetime.strptime(date, "%Y.%m.%d %H:%M:%S"))
				lastly_post = date + title
				push_lastly_post(URL, lastly_post)
				break

		if cnt == 0:	#날짜가 전부 옛날이면 break
			break
		else:			#page를 넘기기 위해 필요한 num이 7이면 7그대로 고정
			if num == 7:
				pass
			else:
				num += 1

	data = (driver, List)
	return data



#포스트 url을 받으면, 그 포스트의 정보를 dictionary 형태로 반환
def Parsing_post_data(driver, post_url, URL):
	return_data = []
	post_data = {}
	domain = Domain_check(URL['url'])

	driver.get(post_url)

	if URL['info'].split("_")[2] == 'qna':
		WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.protectTable")))
	else:
		WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, "table#protectTable")))
	html = driver.page_source
	bs = BeautifulSoup(html, 'html.parser')
	
	title = bs.find("div", {"class": "subject"}).find("span", {"class": "b"}).text.strip()
	author = bs.find("div", {"class": "article_writer"}).find("a").text.strip()
	date = bs.find("div", {"class": "article_writer"}).find("span", {"class": "p11 ls0"}).text.strip()
	date = date + ":00"
	date = str(datetime.strptime(date, "%Y.%m.%d. %H:%M:%S"))
	post = bs.find("div", {"id": "user_contents"}).text.strip()
	post = post_wash(post)		#post 의 공백을 전부 제거하기 위함
	#세종대역은 포스트글이 시작할 때, 항상 112글자의 코드가 같이 긁힌다. 그러니 제외해주자.
	post = post[67:].strip()	#post글을 3000자 까지 읽기위한 작업
	tag_done = tag.tagging(URL, title)
	if bs.find("div", {"id": "user_contents"}).find("img") is None:
		img = 3
	else:
		img = bs.find("div", {"id": "user_contents"}).find("img")['src']		#게시글의 첫번째 이미지를 가져옴.
		if 1000 <= len(img):
			img = 3
		else:
			if img.startswith("http://") or img.startswith("https://"):		# img가 내부링크인지 외부 링크인지 판단.
				pass
			elif img.startswith("//"):
				img = "http:" + img
			else:
				img = domain + img
	if img != 3:
		if img_size(img):
			pass
		else:
			img = 3		

	#post_data = {'title': ,'author': ,'date': ,'post': ,'tag':[],'fav_cnt':0,'view':0} 같은 형식
	post_data['title'] = title.upper()
	post_data['author'] = author.upper()
	post_data['date'] = date
	post_data['post'] = post.lower()
	post_data['tag'] = tag_done 	# 태그1/태그2/태그3/태그4/.../ 같은 형식의 태그string이 들어간다.
	post_data['img'] = img
	post_data['url'] = post_url

	return_data.append(post_data)
	return_data.append(title)
	return_data.append(date)
	return return_data



#url을 받으면 Page를 변환시켜서, 변환된 url 반환
def Change_page(url, page):
	url_done = url + str(page)

	return url_done


#입력된 url의 도메인 url 반환
def Domain_check(url):
	domain = url.split('/')[0] + '//' + url.split('/')[2]	#도메인 url 추출

	return domain