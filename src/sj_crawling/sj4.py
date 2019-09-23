from bs4 import BeautifulSoup
from url_list import List
from post_wash import post_wash
import datetime
from date_cut import date_cut_dict
import tag
import udream


#게시판 page_url 을 받으면, 그 페이지의 url 반환
def Parsing_list_url(URL, page_url):
	List = []
	
	List.append(page_url)

	return List



def Parsing_post_data(post_url, URL):
	post_data_prepare = []
	end_date = date_cut_dict['sj4']		# end_date 추출


	#udream 로그인하는 함수
	s = udream.login()
	
	page = s.get(post_url).text
	bs = BeautifulSoup(page, "html.parser")

	posts = bs.find("tbody").findAll("tr")	#tr묶음
	for post in posts:
		#[title, author, post1, post2, date] 형태
		post_infoes = post.findAll("td")	#td 묶음

		post_data = {}
		title = post_infoes[0].text
		author = post_infoes[0].find("div").text
		if author.find("관리자") != -1:
			author = "0"
		date = post_infoes[4].text + " 00:00:00"
		date = str(datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S"))
		post = post_infoes[1].text + post_infoes[2].text + post_infoes[3].text + "~" + post_infoes[4].text
		post = post_wash(post)
		tag_done = tag.tagging(URL, title)
		post = post[:200]
		img = 1
		url = post_infoes[5].find("a")["href"]

		post_data['title'] = title.upper()
		post_data['author'] = author.upper()
		db_date = post_infoes[3].text + " 00:00:00"
		post_data['date'] = str(datetime.datetime.strptime(db_date, "%Y-%m-%d %H:%M:%S"))
		post_data['post'] = post.upper()
		post_data['tag'] = tag_done		# 태그1/태그2/태그3/태그4/.../ 같은 형식의 태그string이 들어간다.
		post_data['img'] = img
		post_data['url'] = url

		print(date, "::::", title)

		#게시물의 날짜가 end_date 보다 옛날 글이면 continue, 최신 글이면 append
		if str(date) <= end_date:
			continue
		else:
			post_data_prepare.append(post_data)
	s.close()
			
	return post_data_prepare



#url을 받으면 Page를 변환시켜서, 변환된 url 반환
def Change_page(url, page):
	url_done = url + str(page)

	return url_done


#입력된 url의 도메인 url 반환
def Domain_check(url):
	domain = url.split('/')[0] + '//' + url.split('/')[2]	#도메인 url 추출

	return domain