from url_list import List
from bs4 import BeautifulSoup
from url_parser import URLparser
from post_wash import post_wash
import datetime
from date_cut import date_cut_dict
import tag
from img_size import img_size



#게시판 n페이지를 받으면, 그 페이지의 포스트 url 리스트 반환
def Parsing_list_url(URL, bs):
	List = []
	domain = Domain_check(URL['url'])

	posts = bs.find("ul", {"class": "idx"}).findAll("a")
	for post in posts:
		url = post['href']
		url = domain + url
		title = post.text.strip()
		if url.find("idx=") != -1:
			pass
		else:
			List.append(url+"$$"+title)

	return List



#포스트 url을 받으면, 그 포스트의 정보를 dictionary 형태로 반환
def Parsing_post_data(post_url, URL):
	return_data = []
	post_data = {}
	domain = Domain_check(URL['url'])
	title = post_url.split("$$")[1]
	post_url = post_url.split("$$")[0]

	driver_post = URLparser(post_url)
	bs = BeautifulSoup(driver_post, 'html.parser')
	
	title = "세종대백과 :: " + title
	author = "0"
	date =  "2019-01-01 12:00:00"
	date = str(datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S"))
	post = bs.find("div", {"class": "page group"}).text.strip()
	post = post_wash(post)		#post 의 공백을 전부 제거하기 위함
	post = post.split("//<![CDATA")[0]
	if bs.find("div", {"class": "page group"}).find("img") is None:
		img = 0
	else:
		try:
			img = bs.find("div", {"class": "page group"}).find("img")['src']		#게시글의 첫번째 이미지를 가져옴.
			if 1000 <= len(img):
				img = 0
			else:
				if img.startswith("http://") or img.startswith("https://"):		# img가 내부링크인지 외부 링크인지 판단.
					pass
				elif img.startswith("//"):
					img = "http:" + img
				else:
					img = domain + img
		except:
			img = 0
	if img != 0:
		if img_size(img):
			pass
		else:
			img = 0
	tag_done = tag.tagging(URL, title)

	#post_data = {'title': ,'author': ,'date': ,'post': ,'tag':[], img:1, 'view':0} 같은 형식
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

	return url


#입력된 url의 도메인 url 반환 :::: sj10 에 한해서 /bbs/ 까지 뽑힘
def Domain_check(url):
	domain = url.split('/')[0] + '//' + url.split('/')[2]	#도메인 url 추출

	return domain