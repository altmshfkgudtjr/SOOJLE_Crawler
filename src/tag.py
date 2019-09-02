from tagname_list import tag_names
from tagname_list import List


#태그 문자열들을 리스트화 시키기
def tag_listing(tag_list):
	tag_done = []
	for tag in tag_list:
		tag_done.append(tag)
	return tag_done

#태그 리스트들을 "태그1/태그2/태그3/.../" 이런 형식으로 만들어주는 함수
def tag_attach(tag_list):
	tag_list_len = len(tag_list)
	tag_done = ''
	for num in range(tag_list_len):
		tag_done = tag_done + tag_list[num] + "/"
	#몽고디비용 태그 리스트화
	tag_done = tag_listing(tag_list)
	return tag_done


#tag_list 에서 중복값 제거해주기
def set_tag(tag_list):
	tag_list = list(set(tag_list))
	return tag_list


#title에서 비교받을 문자 앞뒤 1칸씩 비교하여, 영어문장인지 아닌지 검사하는 함수
def real_word(text, word):
	strlen = int(len(word))
	text = text + " "
	word_num = int(text.find(word))
	alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	ck = 0
	if word_num == 0:
		title = text[0:strlen+1]
	else:
		title = text[word_num-1:word_num+strlen+1]

	for i in title:
		if i in alp:
			ck += 1
	return ck


#tagging 메인 함수
def tagging(URL, title):
	tag_list = []
	info = URL['info'].split('_')
	#title_tag = URL['title_tag'].split("/")
	title_tag = URL['title_tag']
	#소문자를 전부 대문자화 시켜준다
	title = title.upper()


	#세종대 main 사이트
	if info[0] == 'sj1':
		tag_main(info, title, tag_list, title_tag)
	#세종대 udream 사이트 + 데티즌 공모전 + 잡코리아
	elif (info[0]=='sj2') or (info[0]=='sj3') or (info[0]=='sj4') or (info[0]=='sj5') or info[0] == 'sj35' or info[0] == 'sj36' or info[0] == 'sj37':
		tag_udream(info, title, tag_list, title_tag)
	#세종대 학술정보원 사이트
	elif info[0] == 'sj6':
		tag_library(info, title, tag_list, title_tag)
	#세종대 홍보원 사이트
	elif info[0] == 'sj7' or info[0] == 'sj8':
		tag_promotion(info, title, tag_list, title_tag)
	#세종대 학과사이트
	elif info[0] == 'sj9' or info[0] == 'sj10' or info[0] == 'sj11' or info[0] == 'sj12' or info[0] == 'sj13' or info[0] == 'sj14':
		tag_major(info, title, tag_list, title_tag)
	#세종대 대양휴머니티칼리지
	elif info[0] == 'sj15':
		tag_classic(info, title, tag_list, title_tag)
	#네이버카페
	elif info[0] == 'sj16':
		tag_naver(info, title, tag_list, title_tag)
	#학생생활상담소
	elif info[0] == 'sj17':
		tag_mind(info, title, tag_list , title_tag)
	#SKBS
	elif info[0] == 'sj18':
		tag_skbs(info, title, tag_list, title_tag)
	#총학생회
	elif info[0] == 'sj19':
		tag_chong(info, title, tag_list, title_tag)
	#디시 : 세종대갤러리
	elif info[0] == 'sj20':
		tag_dc(info, title, tag_list, title_tag)
	#세종위키백과
	elif info[0] == 'sj21':
		tag_wiki(info, title, tag_list, title_tag)
	#세종대 에브리타임
	elif info[0] == 'sj22':
		tag_everytime(info, title, tag_list ,title_tag)
	#세종대 에브리타임 책방
	elif info[0] == 'sj23':
		tag_everytime_book(info, title, tag_list ,title_tag)
	#세종알리
	elif info[0] == 'sj24':
		tag_sejong_allie(info, title, tag_list, title_tag)
	#씽굿
	elif info[0] == 'sj25':
		tag_thinkgood_info(info, title, tag_list, title_tag)
	#캠퍼스픽
	elif info[0] == 'sj26' or info[0] == 'sj28':
		tag_campuspick(info, title, tag_list, title_tag)
	#캠퍼스픽 스터디
	elif info[0] == 'sj27':
		tag_campuspick_study(info, title, tag_list, title_tag)
	#행복기숙사
	elif info[0] == 'sj29':
		tag_sejong_dormitory(info, title, tag_list, title_tag)
	#세종대역
	elif info[0] == 'sj30':
		tag_sejong_station(info, title, tag_list, title_tag)
	#두드림
	elif info[0] == 'sj31' or info[0] == 'sj32':
		tag_sejong_dodream(info, title, tag_list, title_tag)
	#전자도서관
	elif info[0] == 'sj33':
		tag_sejong_mobilelibrary(info, title, tag_list ,title_tag)
	#에브리타임
	elif info[0] == 'sj34':
		tag_everytime(info, title, tag_list ,title_tag)


	#태그들을 하나의 문자열로 만든 string 반환
	#tag_list = set_tag(tag_list)
	#tag_done = tag_attach(tag_list)
	tag_done = set_tag(tag_list)

	return tag_done




#세종대 메인사이트 tagging 함수
def tag_main(info, title, tag_list, title_tag):
	title = title.upper() # 모든 title 은 대문자로 만들어준다.
	
	for titletag in title_tag:
		if titletag == "":
			break
		else:
			tag_list.append(titletag)

	#공지사항을 만들기위해서 중요태그를 달아준다
	if info[2] == 'student':
		if title.find("신청") != -1 or title.find("안내") != -1 or title.find("공지") != -1:
			tag_list.append("중요")

	if title.find("입학") != -1:
		tag_list.append("입학")
	
	tagging_public(title, tag_list)






#세종대 학생경력개발시스템 tagging 함수
def tag_udream(info, title, tag_list, title_tag):
	for titletag in title_tag:
		if titletag == "":
			break
		else:
			tag_list.append(titletag)
	
	#학생경력개발시스템 사이트만의 tagging
	if title.find("경력") != -1:
		tag_list.append("경력")
	if title.find("신입") != -1:
		tag_list.append("신입")
	if title.find("기획") != -1 or title.find("설계") != -1 or (real_word(title, "PM") == 2):
		tag_list.append("기획")
	if title.find("회계") != -1 or title.find("경리") != -1:
		tag_list.append("회계")
	if title.find("엔지니어") != -1 or title.find("ENGINEER") != -1 or title.find("캐드") != -1 or (real_word(title, "CAD") == 3) or title.find("기술부") != -1\
	 or title.find("기술자") != -1 or title.find("H/W") != -1 or (real_word(title, "HW") == 2) or title.find("정비") != -1 or title.find("조립") != -1\
	  or title.find("용접") != -1 or title.find("조작") != -1 or title.find("전기공") != -1 or title.find("세공") != -1 or title.find("승강기") != -1\
	   or title.find("엘리베이터") != -1:
		tag_list.append("기술직")
	if title.find("치과") != -1 or title.find("치료사") != -1 or title.find("보건") != -1 or title.find("의료") != -1 or title.find("의원") != -1\
	 or title.find("간호사") != -1 or title.find("한의사") != -1 or title.find("제약") != -1 or title.find("병원") != -1 or title.find("한약") != -1\
	  or ((title.find("약사") != -1) and (title.find("약사신문") == -1)) or ((title.find("약물") != -1) and (title.find("기계") == -1))\
	   or ((title.find("의약품") != -1) and (title.find("기계") == -1)):
		tag_list.append("의료직")
	if title.find("교사") != -1 or title.find("강사") != -1:
		tag_list.append("교직")
	if title.find("영업") != -1 or title.find("마케팅") != -1 or title.find("세일즈맨"):
		tag_list.append("마케팅")
	if title.find("일식") != -1 or title.find("중식") != -1 or title.find("한식") != -1 or title.find("조리사") != -1 or title.find("주방") != -1:
		tag_list.append("조리직")
	if title.find("상담사") != -1 or title.find("상담가") != -1 or title.find("상담원") != -1 or title.find("콜센터") != -1 or title.find("미용실") != -1\
	 or title.find("미용사") != -1 or title.find("관리사") != -1 or title.find("배달") != -1 or title.find("계산원") != -1\
	  or title.find("진행원") != -1 or title.find("택배") != -1 or title.find("관리인") != -1:
		tag_list.append("서비스직")
	if title.find("해외") != -1 or title.find("미국") != -1 or title.find("일본") != -1 or title.find("중국") != -1 or title.find("독일") != -1\
	 or title.find("삿포로") != -1 or title.find("중화권") != -1 or title.find("영어권") != -1 or title.find("SJ GLOVAL JOBS") != -1:
		tag_list.append("해외")
	if title.find("연수") != -1:
		tag_list.append("공모전&대외활동")

	tagging_public(title, tag_list)





#세종대 학술정보원 tagging 함수
def tag_library(info, title, tag_list, title_tag):
	for titletag in title_tag:
		if titletag == "":
			break
		else:
			tag_list.append(titletag)

	tagging_public(title, tag_list)





#세종대 홍보원 tagging 함수
def tag_promotion(info, title, tag_list, title_tag):
	for titletag in title_tag:
		if titletag == "":
			break
		else:
			tag_list.append(titletag)

	tagging_public(title, tag_list)





#세종대 학과사이트 tagging 함수
def tag_major(info, title, tag_list, title_tag):
	for titletag in title_tag:
		if titletag == "":
			break
		else:
			tag_list.append(titletag)

	if title.find("입학") != -1:
		tag_list.append("입학")

	tagging_public(title, tag_list)





#세종대 대양휴머니티칼리지 tagging 함수
def tag_classic(info, title, tag_list, title_tag):
	for titletag in title_tag:
		if titletag == "":
			break
		else:
			tag_list.append(titletag)

	if title.find("입학") != -1:
		tag_list.append("입학")
	if title.find("창의학기") != -1:
		tag_list.append("창의학기제")
	if title.find("SHP") != -1:
		tag_list.append("SHP")

	tagging_public(title, tag_list)





#네이버카페 tagging 함수
def tag_naver(info, title, tag_list, title_tag):
	for titletag in title_tag:
		if titletag == "":
			break
		else:
			tag_list.append(titletag)

	tagging_public(title, tag_list)





#학생생활상담소 tagging 함수
def tag_mind(info, title, tag_list, title_tag):
	for titletag in title_tag:
		if titletag == "":
			break
		else:
			tag_list.append(titletag)

	tagging_public(title, tag_list)





#SKBS tagging 함수
def tag_skbs(info, title, tag_list, title_tag):
	for titletag in title_tag:
		if titletag == "":
			break
		else:
			tag_list.append(titletag)

	tagging_public(title, tag_list)





#총학생회 tagging 함수
def tag_chong(info ,title, tag_list ,title_tag):
	 for titletag in title_tag:
	 	if titletag == "":
	 		break
	 	else:
	 		tag_list.append(titletag)
	 if title.find("야식"):
	 	tag_list.append("중요")
	 if title.find("공청회"):
	 	tag_list.append("공청회")
	 if title.find("스터디룸"):
	 	tag_list.append("중요")
	 if title.find("대동제"):
	 	tag_list.append("중요")

	 tagging_public(title, tag_list)





#디시인사이드 : 세종대갤러리 tagging 함수
def tag_dc(info, title, tag_list ,title_tag):
	for titletag in title_tag:
		if titletag == "":
			break
		else:
			tag_list.append(titletag)

	tagging_public(title, tag_list)





#세종위키백과 tagging 함수
def tag_wiki(info, title, tag_list ,title_tag):
	for titletag in title_tag:
		if titletag == "":
			break
		else:
			tag_list.append(titletag)

	tagging_public(title, tag_list)





#세종대 에브리타임 tagging 함수
def tag_everytime(info, title, tag_list ,title_tag):
	for titletag in title_tag:
		if titletag == "":
			break
		else:
			tag_list.append(titletag)

	tagging_public(title, tag_list)





#세종대 에브리타임 tagging 함수
def tag_everytime_book(info, title, tag_list ,title_tag):
	for titletag in title_tag:
		if titletag == "":
			break
		else:
			tag_list.append(titletag)






#세종알리 tagging 함수
def tag_sejong_allie(info, title, tag_list ,title_tag):
	for titletag in title_tag:
		if titletag == "":
			break
		else:
			tag_list.append(titletag)

	tagging_public(title, tag_list)






#씽굿 tagging 함수
def tag_thinkgood_info(info, title, tag_list ,title_tag):
	for titletag in title_tag:
		if titletag == "":
			break
		else:
			tag_list.append(titletag)

	tagging_public(title, tag_list)






#캠퍼스픽 tagging 함수
def tag_campuspick(info, title, tag_list ,title_tag):
	for titletag in title_tag:
		if titletag == "":
			break
		else:
			tag_list.append(titletag)

	tagging_public(title, tag_list)





#캠퍼스픽 스터디 tagging 함수
def tag_campuspick_study(info, title, tag_list ,title_tag):
	for titletag in title_tag:
		if titletag == "":
			break
		else:
			tag_list.append(titletag)

	tagging_public(title, tag_list)

	if "알바&구인" in tag_list:
		tag_list.remove("알바&구인")





#행복기숙사 tagging 함수
def tag_sejong_dormitory(info, title, tag_list ,title_tag):
	for titletag in title_tag:
		if titletag == "":
			break
		else:
			tag_list.append(titletag)

	tagging_public(title, tag_list)





#세종대역 tagging 함수
def tag_sejong_station(info, title, tag_list, title_tag):
	for titletag in title_tag:
		if titletag == "":
			break
		else:
			tag_list.append(titletag)

	tagging_public(title, tag_list)





#세종대 두드림 tagging 함수
def tag_sejong_dodream(info, title, tag_list, title_tag):
	for titletag in title_tag:
		if titletag == "":
			break
		else:
			tag_list.append(titletag)

	tagging_public(title, tag_list)





#세종대 두드림 tagging 함수
def tag_sejong_mobilelibrary(info, title, tag_list, title_tag):
	for titletag in title_tag:
		if titletag == "":
			break
		else:
			tag_list.append(titletag)

	tagging_public(title, tag_list)





#tagging 공통 함수
def tagging_public(title, tag_list):

	for tag_name in tag_names:
		words = List[tag_name][1].split("/")

		if any((word in title) and (tag_check(title, word)) for word in words):
			tag_list.append(List[tag_name][0])

#예외처리
def tag_check(title, tag):
	if tag == 'IT':
		if real_word(title, tag)== 2 and title.find("IT IS") == -1 and title.find("DO IT") == -1: return True
		else: return False
	elif tag == 'SW':
		if real_word(title, tag)==2: return True
		else: return False
	elif tag == 'DBA':
		if real_word(title, tag)==3: return True
		else: return False
	elif tag == 'AI':
		if real_word(title, tag)==2: return True
		else: return False
	elif tag == 'SE':
		if real_word(title,tag)==2: return True
		else: return False
	elif tag == 'IOS':
		if real_word(title, tag)==3: return True
		else: return False
	elif tag == 'API':
		if real_word(title, tag)==3: return True
		else: return False
	elif tag == 'UX':
		if real_word(title,tag)==2: return True
		else: return False
	elif tag == 'UI':
		if real_word(title,tag)==2: return True
		else: return False
	elif tag == 'VR':
		if real_word(title,tag)==2: return True
		else: return False
	elif tag == '학식':
		if title.find("입학식") != -1: return False
		else: return True
	elif tag == '로펌':
		if title.find("윌로펌프") != -1: return False
		else: return True
	elif tag == '정규직':
		if title.find("비정규직") != -1: return False
		else: return True
	elif tag == '카페':
		if title.find("네이버 카페") != -1 or title.find("네이버카페") != -1 or title.find("다음 카페") != -1 or title.find("다음카페") != -1 or title.find("인터넷 카페") != -1 or title.find("인터넷카페")\
		 or title.find("NAVER 카페") != -1 or title.find("DAUM 카페") != -1:
			return False
		else: return True
	elif tag == '학사':
		if title.find("대학사") != -1: return False
		else: return True
	elif tag == '국제':
		if title.find("자유학기") != -1: return False
		else: return True
	elif tag == '스포츠':
		if title.find("1운동") != -1: return False
		elif title.find("18운동") != -1: return False
		elif title.find("화운동") != -1: return False
		elif title.find("화 운동") != -1: return False
		else: return True
	elif tag == '학사':
		if title.find("학사상") != -1 or title.find("학사고") != -1:
			return False
	else: return True