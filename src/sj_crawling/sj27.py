from bs4 import BeautifulSoup
from selenium import webdriver
from url_list import List
from post_wash import post_wash
import datetime
import tag
import campuspick
from driver_agent import chromedriver
from date_cut import date_cut
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time



#게시판 page_url 을 받으면, 그 페이지의 포스트 url 들을 반환
def Parsing_list_url(URL, page_url):
	List = []
	domain = Domain_check(URL['url'])

	#만약 driver이 켜져있으면 끄고, 없으면 그냥 진행
	try:
		driver.quit()
	except:
		pass

	driver = chromedriver()
	#캠퍼스픽 로그인함수
	driver = campuspick.login(driver)

	List.append(page_url)
	

	data = (driver, List)

	return data



#포스트 url을 받으면, 그 포스트의 정보를 dictionary 형태로 반환
def Parsing_post_data(driver, post_url, URL, lastly_post):
	post_data_prepare = []
	domain = Domain_check(URL['url'])
	end_date = date_cut(URL['info'])
	now_num = 0
	repeat_num = 0
	#driver.get(post_url)
	#WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, "p.badges"))) #div.header을 발견하면 에이작스 로딩이 완료됬다는 가정

	#비교를 하기위해서 make
	last_posts = [0]
	while 1:
		driver.get(post_url)
		WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, "p.badges"))) #div.header을 발견하면 에이작스 로딩이 완료됬다는 가정


		for i in range(repeat_num):
			driver.find_element_by_tag_name("body").send_keys(Keys.END)
			time.sleep(0.5)

		html = driver.page_source
		bs = BeautifulSoup(html, 'html.parser')

		posts = bs.find("div", {"class": 'list'}).findAll("a", {"class": "item"})
		#더이상 내릴 수 없으면 break
		if len(last_posts) == len(posts):
			break
		else:
			last_posts = posts


		for post in posts[now_num:]:
			post_data = {}
			url = post['href']
			url = domain + url

			try:
				driver.get(url)
			except:				
				data = (post_data_prepare, lastly_post)
				return data
			try:
				WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, "p.text"))) #a.item을 발견하면 에이작스 로딩이 완료됬다는 가정
			except:
				data = (post_data_prepare, lastly_post)
				return data
			html_post = driver.page_source
			bs_post = BeautifulSoup(html_post, 'html.parser')

			title = bs_post.find("article").find("h1").text.strip()
			author = bs_post.find("p", {"class": "profile"}).text.strip()
			date =  bs_post.find("p", {"class": "info"}).find("span").text.strip()
			if date.find("오늘") != -1:
				date = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
			elif len(date.split("/")) != 3:
				now_year = datetime.datetime.now().strftime("%Y")
				date = now_year + "/" + date + ":00"
				date = str(datetime.datetime.strptime(date, "%Y/%m/%d %H:%M:%S"))
			else:
				date = "20" + date + ":00"
				date = str(datetime.datetime.strptime(date, "%Y/%m/%d %H:%M:%S"))
			
			phrase = bs_post.find("p", {'class': "text"}).text.strip()
			phrase = post_wash(phrase)		#post 의 공백을 전부 제거하기 위함
			tag_done = tag.tagging(URL, title)
			img = 8

			post_data['title'] = title.upper()
			post_data['author'] = author.upper()
			post_data['date'] = date
			post_data['post'] = phrase.lower()
			post_data['tag'] = tag_done
			post_data['img'] = img
			post_data['url'] = url

			print(date, "::::", title)

			if (date < end_date) or (title.upper() == lastly_post):
				break
			else:
				post_data_prepare.append(post_data)

		now_num = len(posts)
		repeat_num += 1
		if (date <= end_date) or (title.upper() == lastly_post):
			break
	if len(post_data_prepare) == 0:
		lastly_post = None
	else:
		lastly_post = post_data_prepare[0]['title']
	data = (post_data_prepare, lastly_post)
	return data



#url을 받으면 url 그대로 반환해준다. => Page number이 필요하지 않는 url
def Change_page(url, page):

	return url


#입력된 url의 도메인 url 반환
def Domain_check(url):
	domain = url.split('/')[0] + '//' + url.split('/')[2]	#도메인 url 추출

	return domain