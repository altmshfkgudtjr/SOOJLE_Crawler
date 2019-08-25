from url_list import List
from post_wash import post_wash
import datetime
from date_cut import date_cut_dict
import tag
from img_size import img_size



#게시판 n페이지를 받으면, 그 페이지의 포스트 url 리스트 반환
def Parsing_list_url(URL, bs):
	List = []
	domain = Domain_check(URL['url'])

	posts = bs.find("tbody").findAll("tr")
	for post in posts:
		url = post.find("a")['href']
		url = domain + url
		List.append(url)

	return List



#포스트 url을 받으면, 그 포스트의 정보를 dictionary 형태로 반환
def Parsing_post_data(bs, post_url, URL):
	return_data = []
	post_data = {}
	domain = Domain_check(URL['url'])

	title = bs.find("div", {"class": "originalContent"}).find("div", {"class": "title"}).text.strip()
	author = bs.find("div", {"class": "originalContent"}).find("div", {"class": "userInfo"}).text.strip()
	if author.find("관리자") != -1:
		author = "0"
	date = bs.find("div", {"class": "originalContent"}).find("div", {"class": "dateAndCount"}).find("strong").text.strip()
	date = date + " 00:00:00"
	date = str(datetime.datetime.strptime(date, "%Y.%m.%d %H:%M:%S"))
	post = bs.find("div", {"class": "contentBody"}).find("div").text.strip()
	post = post_wash(post)		#post 의 공백을 전부 제거하기 위함
	post = post[:3000]	#post글을 3000자 까지 읽기위한 작업
	if bs.find("div", {"class": "contentBody"}).find("img") is None:
		img = 1
	else:
		img = bs.find("div", {"class": "contentBody"}).find("img")['src']		#게시글의 첫번째 이미지를 가져옴.
		if 1000 <= len(img):
			img = 1
		else:
			if img.startswith("http://") or img.startswith("https://"):		# img가 내부링크인지 외부 링크인지 판단.
				pass
			elif img.startswith("//"):
				img = "http:" + img
			else:
				img = domain + img
	if img != 1:
		if img_size(img):
			pass
		else:
			img = 1
	tag_done = tag.tagging(URL, title)

	#post_data = {'title': ,'author': ,'date': ,'post': ,'tag':[], img:1, 'view':0} 같은 형식
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
	url_done = url + str(page)

	return url_done


#입력된 url의 도메인 url 반환 :::: sj10 에 한해서 /bbs/ 까지 뽑힘
def Domain_check(url):
	domain = url.split('/')[0] + '//' + url.split('/')[2] + '/' + url.split('/')[3] + '/'	#도메인 url 추출

	return domain