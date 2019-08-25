from time import gmtime, strftime
from time_convert import datetime_to_unixtime



today = strftime("%Y-%m-%d %H:%M:%S", gmtime())
today = datetime_to_unixtime(today)
# author 은 0으로 지정
List = (\
	{'post_id': "1", 'info': "domain_sejong_main",\
	'title': "세종대학교", 'date': today,\
	'post': "세종대학교 공식 홈페이지입니다. [Tel]02-3408-3114 [E-mail]webmaster@sejong.ac.kr",\
	'img': "1", 'url': "http://www.sejong.ac.kr/",\
	'title_tag': "사이트/"},\
	{'post_id': "2", 'info': "domain_sejong_entrance",\
	'title': "세종대학교 입학안내", 'date': today,\
	'post': "정시/수시/편입학 등 세종대학교 입학에 대한 정보를 알려드립니다. [Tel]02-3408-3456,4455 [Fax]02-3408-3556",\
	'img': "1", 'url': "https://ipsi.sejong.ac.kr/",\
	'title_tag': "사이트/입학/"},\
	{'post_id': "3", 'info': "domain_sejong_student",\
	'title': "학사정보시스템", 'date': today,\
	'post': "세종대학교와 관련된 개인정보 관리, 학적관리, 학점/평점 산출, 수강신청, 등록금확인 등을 할 수 있는 사이트입니다.",\
	'img': "1", 'url': "http://uis.sejong.ac.kr",\
	'title_tag': "사이트/학사/"},\
	{'post_id': "4", 'info': "domain_sejong_blackboard",\
	'title': "세종대학교 블랙보드", 'date': today,\
	'post': "세종대학교 강의 관리 사이트입니다.",\
	'img': "1", 'url': "https://blackboard.sejong.ac.kr/",\
	'title_tag': "사이트/학사/"},\
	{'post_id': "5", 'info': "domain_sejong_manual",\
	'title': "학술전산처 전산정보실 프로그램 메뉴얼", 'date': today,\
	'post': "Office365 및 학사정보시스템, 학생경력개발시스템, 전자출결시스템에 대한 메뉴얼을 알려드립니다.",\
	'img': "1", 'url': "http://portal.sejong.ac.kr/popup/manual_popup1.html",\
	'title_tag': "사이트/FAQ/"},\
	{'post_id': "6", 'info': "domain_sejong_udream",\
	'title': "학생경력개발시스템", 'date': today,\
	'post': "학부생의 진로설계, 진로상담, 경력개발, 실전취업 등 각종 진로와 취업에 대한 정보를 얻을 수 있는\
사이트입니다. [위치]학생회관 308호 [Tel]02-3408-4152 [Fax]02-3408-3300 [E-mail]job@sejong.ac.kr",\
	'img': "1", 'url': "http://udream.sejong.ac.kr/",\
	'title_tag': "사이트/취업&진로/"},\
	{'post_id': "7", 'info': "domain_sejong_library",\
	'title': "학술정보원", 'date': today,\
	'post': "세종대학교 학술정보원(도서관) 이용 안내 및 공지사항과 스터디룸 예약, 자유열람실 좌석현황, \
각종 도서 및 논문 등을 알려드립니다.",\
	'img': "http://library.sejong.ac.kr/site/sejong/images/header/logo_sejonglib.gif", 'url': "http://library.sejong.ac.kr/index.ax",\
	'title_tag': "사이트/도서/학술정보원/"},\
	{'post_id': "8", 'info': "domain_sejong_librarysearch",\
	'title': "학술정보원 전자정보검색", 'date': today,\
	'post': "학술정보원에 있는 도서, 논문 및 저널 등 전자정보를 검색할 수 있습니다.",\
	'img': "http://library.sejong.ac.kr/site/sejong/images/header/logo_sejonglib.gif", 'url': "http://library.sejong.ac.kr/search/Search.ax?sid=9",\
	'title_tag': "사이트/도서/학술정보원/"},\
	{'post_id': "9", 'info': "domain_sejong_sjce",\
	'title': "SJCE", 'date': today,\
	'post': "세종대학교 컴퓨터공학과 학생회 홈페이지입니다. 사물함 신청, 돕바 신청, 학생회비 사용 내역 확인\
, C스터디 신청 등을 할 수 있습니다. [위치]율곡관 302호 [Tel]02-3408-3321",\
	'img': "http://sjce.kr/files/attach/images/106/2eea01f370220284997245440c77eeb3.jpg", 'url': "http://sjce.kr/",\
	'title_tag': "사이트/컴퓨터공학과/"},\
	{'post_id': "10", 'info': "domain_sejong_modoo",\
	'title': "모두의 거리", 'date': today,\
	'post': "세종대학교 주변 맛집 및 상가에 대하여 알려드립니다.",\
	'img': "1", 'url': "https://sejongst.modoo.at/",\
	'title_tag': "사이트/기타/"},\
	{'post_id': "11", 'info': "domain_sejong_redtable",\
	'title': "세종대학교 레드 테이블", 'date': today,\
	'post': "Red table에서 세종대학교의 학생식당 및 카페 메뉴를 보고, 온라인 결제를 할 수 있는 사이트입니다.",\
	'img': "http://campus.redtable.kr/img/logo-1-1.png", 'url': "http://campus.redtable.kr/",\
	'title_tag': "사이트/학식/"},\
	{'post_id': "12", 'info': "domain_sejong_mbookcosmos",\
	'title': "세종대 모바일 북카페", 'date': today,\
	'post': "도서 요약본, 오디오북, 독서퀴즈, 도서 주문 등을 할 수 있는 사이트입니다. ",\
	'img': "http://msejong.bookcosmos.com/logoimg/intro.gif", 'url': "http://msejong.bookcosmos.com/intro.asp",\
	'title_tag': "사이트/도서/"},\
	{'post_id': "13", 'info': "domain_sejong_foreigner",\
	'title': "국제교류원", 'date': today,\
	'post': "세종대학교 국제교류원 공식 홈페이지입니다. [위치]광개토관 910호 [Tel]02-3408-4051-3 [Fax]02-3408-4197",\
	'img': "http://ili.sejong.ac.kr/static/org02/images/header_logo.gif", 'url': "http://ili.sejong.ac.kr/index.do",\
	'title_tag': "사이트/국제/"},\
	{'post_id': "14", 'info': "domain_sejong_museum",\
	'title': "박물관", 'date': today,\
	'post': "세종대학교 박물관의 소개, 유물, 전시실 소개에 대한 정보를 알려드립니다.\
[개관요일] 월요일 ~ 금요일 [개관시간] a.m. 10:00 ~ p.m. 15:00 (공휴일 휴관, 관람요금 무료)",\
	'img': "http://museum.sejong.ac.kr/static/museum/images/common/h1_logo_header.gif", 'url': "http://museum.sejong.ac.kr/index.do",\
	'title_tag': "사이트/박물관/"},\
	{'post_id': "15", 'info': "domain_sejong_clubdevelop",\
	'title': "웹 개발 동아리 Openyearround", 'date': today,\
	'post': "세종대학교 웹 개발 동아리로서 스터디를 통해 웹/모바일 어플리케이션 개발에 중점을 두고 있고, \
현재 각종 공모전 및 학술제에 참여하고 있습니다.",\
	'img': "http://openyearround.co.kr/images/background3.jpg", 'url': "http://openyearround.co.kr/",\
	'title_tag': "사이트/IT&컴퓨터/동아리/공모전&대외활동/"},\
	{'post_id': "16", 'info': "domain_thinkgood_carrer",\
	'title': "씽굿-대한민국 대표 공모전 미디어", 'date': today,\
	'post': "대한민국 대표 공모전 포털이며, 공모전의 기획 홍보 접수 심사 시상 전시 등 공모전의 전과정을 \
프로모션하는 국내최고의 공모전 컨텐츠 프로모션 회사입니다.",\
	'img': "https://www.thinkcontest.com/assets/img/icon/apple-icon-72x72.png", 'url': "https://www.thinkcontest.com/Contest/CateField.html?page=1",\
	'title_tag': "사이트/공모전&대외활동/커뮤니티/"},\
	{'post_id': "17", 'info': "domain_sejong_counselor",\
	'title': "학생생활상담소", 'date': today,\
	'post': "세종대학교 학생생활상담소 사이트입니다. 비공개 상담, 야간 위기 상담 가능 \
[이용시간]평일 a.m 09:00 ~ p.m 5:30(점심시간 p.m 12 ~ p.m 13) [위치]학생회관 310호 \
[Tel]02-3408-3336",\
	'img': "http://counsel.sejong.ac.kr/files/attach/images/138/40854527837c821e310d389123fb811b.png", 'url': "http://counsel.sejong.ac.kr/",\
	'title_tag': "사이트/고민&상담/"},\
	{'post_id': "18", 'info': "domain_sejong_skbs",\
	'title': "SKBS", 'date': today,\
	'post': "세종대학교 군자방송국 SKBS 입니다. SKBS 뉴스 및 방송 제보 가능 \
[위치]학생회관 619호 [Tel]02-3408-3354",\
	'img': "http://www.skbs.kr/files/attach/images/109/d07548f093db6751bae1ba1aed813c5c.png", 'url': "http://www.skbs.kr/",\
	'title_tag': "사이트/방송국/소식/교내/"},\
	{'post_id': "19", 'info': "domain_campuspick_career",\
	'title': "캠퍼스픽", 'date': today,\
	'post': "대학생을 위한 동아리, 대외활동, 공모전, 스터디, 취업정보, 커뮤니티 등을 알 수 있는 사이트입니다.",\
	'img': "0", 'url': "https://www.campuspick.com/",\
	'title_tag': "사이트/공모전&대외활동/동아리&모임/취업&진로/커뮤니티/"},\
	{'post_id': "20", 'info': "domain_dabang_place",\
	'title': "다방 : Dabang", 'date': today,\
	'post': "대한민국 대표 부동산 필수 앱 [때가 됬다 다방 할 때]",\
	'img': "http://static.dabangapp.com/img/opengraph.png", 'url': "https://www.dabangapp.com/",\
	'title_tag': "사이트/자취&하숙/"},\
	{'post_id': "21", 'info': "domain_zigbang_place",\
	'title': "직방 : Zigbang", 'date': today,\
	'post': "부동산정보 전문 앱 [집 구할 때, 직방]",\
	'img': "http://s.zigbang.com/v1/web/common/new/h_logo.png", 'url': "https://www.zigbang.com/",\
	'title_tag': "사이트/자취&하숙/"},\
	{'post_id': "22", 'info': "domain_peterpanz_place",\
	'title': "피터팬 : Perterpanz", 'date': today,\
	'post': "국내 최대 부동산 직거래 서비스 [피터팬의 좋은방 구하기]",\
	'img': "https://www.peterpanz.com/images/logo/group_271.png", 'url': "https://www.peterpanz.com/",\
	'title_tag': "사이트/자취&하숙/"},\
	{'post_id': "23", 'info': "domain_everytime_lecture",\
	'title': "에브리타임 강의평가", 'date': today,\
	'post': "로그인, 학교 인증 후 강의평을 확인할 수 있습니다.",\
	'img': "https://www.everytime.kr/images/about/logo.png", 'url': "https://everytime.kr/lecture",\
	'title_tag': "사이트/수강/커뮤니티/"},\
	{'post_id': "24", 'info': "domain_everytime_comunity",\
	'title': "에브리타임", 'date': today,\
	'post': "대학교 커뮤니티 및 시간표 서비스, 시간표 작성 및 학업 관리, 학교 생활 정보, 학교별 익명 커뮤니티 기능을 제공합니다.",\
	'img': "https://www.everytime.kr/images/about/logo.png", 'url': "https://everytime.kr/",\
	'title_tag': "사이트/수강/커뮤니티/"},\
	{'post_id': "25", 'info': "domain_naver_welfare",\
	'title': "학생복지양성평등위원회", 'date': today,\
	'post': "애플온캠퍼스, 무료 대여사업을 진행 중입니다.",\
	'img': "2", \
	'url': "https://cafe.naver.com/welfaresejong",\
	'title_tag': "사이트/기타/"},\
	{'post_id': "26", 'info': "domain_naver_physicsastronomy",\
	'title': "세종대학교 물리천문학과", 'date': today,\
	'post': "세종대학교 물리학과, 천문우주학과 공식 카페입니다. [위치]영실관 113호, 601호 [Tel]02-3408-3316(물리학과) 02-3408-3920(천문우주학과)",\
	'img': "2", \
	'url': "https://cafe.naver.com/sejongphas",\
	'title_tag': "사이트/물리천문학과/"},\
	{'post_id': "27", 'info': "domain_naver_arthall",\
	'title': "세종대학교 영화예술학과 극장팀", 'date': today,\
	'post': "세종대학교 영화예술학과 극장팀 공식 카페입니다. 세종아트홀 대관 및 무대, 조명, 음향, 의상, 소품, 분장, 영상, 기획 등 자료 조회/대여 가능합니다.",\
	'img': "2", \
	'url': "https://cafe.naver.com/sejongthesoul",\
	'title_tag': "사이트/영화예술학과/거래&대여/"},\
	{'post_id': "28", 'info': "domain_naver_filmtool",\
	'title': "세종대학교 영화예술학과 기자재팀 공식 카페입니다. 기자재, 음향장비, 스튜디오 대여/신청 가능합니다.", 'date': today,\
	'post': "기자재, 음향장비, 스튜디오 대여 가능합니다.",\
	'img': "2", 'url': "https://cafe.naver.com/filmtool",\
	'title_tag': "사이트/영화예술학과/거래&대여/"},\
	{'post_id': "29", 'info': "domain_facebook_bamboo",\
	'title': "세종대학교 대나무숲", 'date': today,\
	'post': "학우분들께서 하고싶은 말들을 익명으로 올려드립니다.",\
	'img': "4", 'url': "https://ko-kr.facebook.com/sejongbamboo/",\
	'title_tag': "사이트/커뮤니티/"},\
	{'post_id': "30", 'info': "domain_naver_film",\
	'title': "세종대학교 영화예술학과", 'date': today,\
	'post': "세종대학교 영화예술학과 공식 카페입니다. [위치]광개토관 1201호 [Tel]02-3408-3327",\
	'img': "2", 'url': "https://cafe.naver.com/sejongfilm18",\
	'title_tag': "사이트/영화예술학과/"},\
	{'post_id': "31", 'info': "domain_naver_business",\
	'title': "세종대학교 경영학과", 'date': today,\
	'post': "세종대학교 경영학과 공식 카페입니다. [위치]광개토관 317호 [Tel]02-3408-3310,3311",\
	'img': "2", 'url': "https://cafe.naver.com/sejongbiz",\
	'title_tag': "사이트/경영학과/"},\
	{'post_id': "32", 'info': "domain_naver_engineering",\
	'title': "세종대학교 공과대학", 'date': today,\
	'post': "세종대학교 공과대학 공식 카페입니다. [위치]충무관 410A호 [Tel]02-3408-3524",\
	'img': "2", 'url': "https://cafe.naver.com/sjengineering",\
	'title_tag': "사이트/공과대학/"},\
	{'post_id': "33", 'info': "domain_naver_cluborchestra",\
	'title': "세종대학교 지음", 'date': today,\
	'post': "세종대학교 음악동아리 아마추어 오케스트라 지음입니다. [위치]학생회관 613호",\
	'img': "2", 'url': "https://cafe.naver.com/ziumsince2012",\
	'title_tag': "사이트/동아리&모임/음악/"},\
	{'post_id': "34", 'info': "domain_naver_clubkingbora",\
	'title': "세종대학교 총동아리연합회 보라", 'date': today,\
	'post': "세종대학교 총동아리연합회 보라입니다. [위치]학생회관 408호",\
	'img': "2", 'url': "https://cafe.naver.com/sejongclubunion",\
	'title_tag': "사이트/동아리&모임/"},\
	{'post_id': "35", 'info': "domain_naver_clubwebtoon",\
	'title': "세종대학교 한손", 'date': today,\
	'post': "세종대학교 만화동아리 한손입니다. [위치]학생회관 522호",\
	'img': "2", 'url': "https://cafe.naver.com/sghanson",\
	'title_tag': "사이트/동아리&모임/디자인/"},\
	{'post_id': "36", 'info': "domain_naver_clubliterature",\
	'title': "세종대학교 문학회", 'date': today,\
	'post': "행동하는 예술인, 세종대학교 동아리 문학회입니다.",\
	'img': "2", 'url': "https://cafe.naver.com/semunchang",\
	'title_tag': "사이트/동아리&모임/"},\
	{'post_id': "37", 'info': "domain_naver_natureenergy",\
	'title': "세종대학교 환경에너지공간융합학과", 'date': today,\
	'post': "세종대학교 환경에너지공간융합학과 공식 카페입니다. [위치]영실관 516호 [Tel]02-3408-3320",\
	'img': "2", 'url': "https://cafe.naver.com/seeu1",\
	'title_tag': "사이트/환경에너지공간융합학과/공과대학/"},\
	{'post_id': "38", 'info': "domain_naver_clubband",\
	'title': "세종대학교 사운드플러스", 'date': today,\
	'post': "세종대학교 중앙밴드동아리 사운드플러스입니다.",\
	'img': "2", 'url': "https://cafe.naver.com/sjsoundplus",\
	'title_tag': "사이트/동아리&모임/음악/"},\
	{'post_id': "39", 'info': "domain_naver_lifesystem",\
	'title': "세종대학교 생명시스템학부", 'date': today,\
	'post': "세종대학교 생명시스템학부 공식 카페입니다. [위치]영관실304A호 [Tel]02-3408-3319",\
	'img': "2", 'url': "https://cafe.naver.com/sjlifesystem",\
	'title_tag': "사이트/생명시스템학부/"},\
	{'post_id': "40", 'info': "domain_naver_software",\
	'title': "세종대학교 소프트웨어학과", 'date': today,\
	'post': "세종대학교 소프트웨어학과 공식 카페입니다. [위치]율곡관 303A호 [Tel]02-3408-3667",\
	'img': "2", 'url': "https://cafe.naver.com/sejongsoftware",\
	'title_tag': "사이트/소프트웨어학과/IT&컴퓨터/"},\
	{'post_id': "41", 'info': "domain_naver_clubbasketball",\
	'title': "세종대학교 RUSH", 'date': today,\
	'post': "세종대학교 중앙 농구동아리 러쉬입니다.",\
	'img': "2", 'url': "https://cafe.naver.com/sjrush516",\
	'title_tag': "사이트/동아리&모임/스포츠/"},\
	{'post_id': "42", 'info': "domain_naver_foreigner",\
	'title': "세종대학교 교환학생 카페", 'date': today,\
	'post': "세종대학교 교환학생 정보교환 카페입니다.",\
	'img': "2", 'url': "https://cafe.naver.com/sejongexchange",\
	'title_tag': "사이트/국제/"},\
	{'post_id': "43", 'info': "domain_naver_music",\
	'title': "세종대학교 음악과", 'date': today,\
	'post': "세종대학교 음악과 공식 카페입니다. [위치]모짜르트홀 102호 [Tel]02-3408-3324",\
	'img': "2", 'url': "https://cafe.naver.com/mumumusic",\
	'title_tag': "사이트/음악과/음악/"},\
	{'post_id': "44", 'info': "domain_naver_animation",\
	'title': "세종대학교 만화애니메이션학과", 'date': today,\
	'post': "세종대학교 만화애니메이션학과 공식 카페입니다. [위치]군자관 415호 [Tel]02-3408-3328",\
	'img': "2", 'url': "https://cafe.naver.com/secan",\
	'title_tag': "사이트/만화애니메이션학과/디자인/"},\
	{'post_id': "45", 'info': "domain_naver_mathstatistics",\
	'title': "세종대학교 수학통계학부", 'date': today,\
	'post': "세종대학교 수학통계학부 공식 카페입니다. [위치]다산관 109호 [Tel]02-3408-3315",\
	'img': "2", 'url': "https://cafe.naver.com/flyingmath",\
	'title_tag': "사이트/수학통계학부/"},\
	{'post_id': "46", 'info': "domain_naver_korean",\
	'title': "세종대학교 국어국문학과", 'date': today,\
	'post': "세종대학교 국어국문학과 공식 카페입니다. [위치]집현관 908호 [Tel]02-3408-3301",\
	'img': "2", 'url': "https://cafe.naver.com/sejonguvkl",\
	'title_tag': "사이트/국어국문학과/"},\
	{'post_id': "47", 'info': "domain_naver_energy",\
	'title': "세종대학교 에너지자원공학과", 'date': today,\
	'post': "세종대학교 에너지자원공학과 공식 카페입니다. [위치]영실관 516호 [Tel]02-3408-3671",\
	'img': "2", 'url': "https://cafe.naver.com/energysejong",\
	'title_tag': "사이트/에너지자원공학과/"},\
	{'post_id': "48", 'info': "domain_naver_chemistry",\
	'title': "세종대학교 화학과", 'date': today,\
	'post': "세종대학교 화학과 공식 카페입니다. [위치]영실관 215호 [Tel]02-3408-3317",\
	'img': "2", 'url': "https://cafe.naver.com/sejongchemistry",\
	'title_tag': "사이트/화학과/"},\
	{'post_id': "49", 'info': "domain_naver_sjnanuri",\
	'title': "세종나누리", 'date': today,\
	'post': "세종대학교 나눔봉사단 봉사활동서포터즈입니다. [위치]집현관 115호 [Tel]02-3408-2909 [Fax]02-3408-2908 [Email]volunteer@sejong.ac.kr",\
	'img': "2", 'url': "https://cafe.naver.com/sjnanuri",\
	'title_tag': "사이트/봉사/"},\
	{'post_id': "50", 'info': "domain_naver_eieapple",\
	'title': "세종대학교 전자정보공학대학 애플", 'date': today,\
	'post': "세종대학교 전자정보공학대학 학생회 애플입니다. [위치]율곡관 602호 [Tel]02-3408-2546",\
	'img': "2", 'url': "https://cafe.naver.com/sejongeie",\
	'title_tag': "사이트/전자정보공학대학/IT&컴퓨터/"},\
	{'post_id': "51", 'info': "domain_naver_intellimechanical",\
	'title': "세종대학교 지능기전공학부", 'date': today,\
	'post': "세종대학교 지능기전공학부 공식 카페입니다. [위치]군자관 102호 [Tel]02-3408-3900",\
	'img': "2", 'url': "https://cafe.naver.com/aimechatronic",\
	'title_tag': "사이트/지능기전공학부/IT&컴퓨터/"},\
	{'post_id': "52", 'info': "domain_naver_clubunsa",\
	'title': "세종대학교 UNSA", 'date': today,\
	'post': "세종대학교 학술/엽합 중앙동아리 운사입니다. 멘토/멘티 및 모의총회 활동 [위치]학생회관 521호",\
	'img': "2", 'url': "https://cafe.naver.com/MyCafeIntro.nhn?clubid=28987205",\
	'title_tag': "사이트/동아리&모임/멘토링/"},\
	{'post_id': "53", 'info': "domain_daum_hotelier",\
	'title': "세종대학교 호텔리어 리딩그룹", 'date': today,\
	'post': "세종대학교 동아리 호텔리어입니다. ",\
	'img': "3", 'url': "http://cafe.daum.net/HotelAsia/1eW",\
	'title_tag': "사이트/동아리&모임/"},\
	{'post_id': "54", 'info': "domain_daum_mechnicalspace",\
	'title': "세종대학교 기계항공우주공학부", 'date': today,\
	'post': "세종대학교 기계항공우주공학부 공식 카페입니다. [위치]충무관 1009호 [Tel]02-3408-3663",\
	'img': "3", 'url': "http://cafe.daum.net/sejongaerospace",\
	'title_tag': "사이트/기계항공우주공학부/"},\
	{'post_id': "55", 'info': "domain_daum_youthhostel",\
	'title': "세종대학교 유스호스텔", 'date': today,\
	'post': "세종대학교 중앙여행동아리 YouthHostel 입니다. [위치]학생회관 509호",\
	'img': "3", 'url': "http://cafe.daum.net/sejongyh",\
	'title_tag': "사이트/동아리&모임/여행/"},\
	{'post_id': "56", 'info': "domain_daum_clubsamulnori",\
	'title': "세종대학교 터벌림", 'date': today,\
	'post': "세종대학교 중앙풀물패 동아리 터벌림입니다. [위치]학생회관 621호",\
	'img': "3", 'url': "http://cafe.daum.net/1661",\
	'title_tag': "사이트/동아리&모임/음악/"},\
	{'post_id': "57", 'info': "domain_daumr_conversation",\
	'title': "세종대학교 회화과", 'date': today,\
	'post': "세종대학교 회화과 공식 카페입니다. [위치]진관홀 310호 [Tel]02-3408-3322",\
	'img': "3", 'url': "http://cafe.daum.net/SJFINEART",\
	'title_tag': "사이트/회화과/"},\
	{'post_id': "58", 'info': "domain_daum_clubbaseball",\
	'title': "세종대학교 KINGS", 'date': today,\
	'post': "세종대학교 중앙 야구 동아리 킹스입니다. [위치]학생회관 519호",\
	'img': "3", 'url': "http://cafe.daum.net/sejongkings",\
	'title_tag': "사이트/동아리&모임/스포츠/"},\
	{'post_id': "59", 'info': "domain_daum_clubmusic",\
	'title': "세종대학교 늘혬", 'date': today,\
	'post': "세종대학교 중앙 음악동아리 늘혬입니다. [위치]학생회관 510호",\
	'img': "3", 'url': "http://cafe.daum.net/nlheam",\
	'title_tag': "사이트/동아리&모임/음악/"},\
	{'post_id': "60", 'info': "domain_daum_clubtaekkyun",\
	'title': "세종대학교 발파람", 'date': today,\
	'post': "세종대학교 택견동아리 발파람입니다. [위치]학생회관 503호",\
	'img': "3", 'url': "http://cafe.daum.net/taekkyun2003",\
	'title_tag': "사이트/동아리&모임/스포츠/"},\
	{'post_id': "61", 'info': "domain_daum_datascience",\
	'title': "세종대학교 데이터사이언스학과", 'date': today,\
	'post': "세종대학교 데이터사이언스학과 공식 카페입니다. [위치]군자과 102호 [Tel]02-6935-2544",\
	'img': "3", 'url': "http://cafe.daum.net/sejongdatascience",\
	'title_tag': "사이트/데이터사이언스학과/IT&컴퓨터/"},\
	{'post_id': "62", 'info': "domain_daum_sejongstation",\
	'title': "세종대역", 'date': today,\
	'post': "세종대학교 커뮤니티로서, 공지사항, 대외활동, 시험족보 등에 관하여 알려드립니다.",\
	'img': "3", 'url': "http://cafe484.daum.net/_c21_/home?grpid=1SVkj",\
	'title_tag': "사이트/커뮤니티/공모전&대외활동/"},\
	{'post_id': "63", 'info': "domain_facebook_sejong",\
	'title': "세종대학교 페이스북", 'date': today,\
	'post': "세종대학교 공식 페이스북 페이지입니다.",\
	'img': "4", 'url': "https://facebook.com/sejongpr/",\
	'title_tag': "사이트/공지/"},\
	{'post_id': "64", 'info': "domain_facebook_sejongstation",\
	'title': "세종대역 페이스북", 'date': today,\
	'post': "세종대학교 커뮤니티, 세종대역의 공식 페이스북 페이지입니다.",\
	'img': "4", 'url': "https://facebook.com/sejongstation",\
	'title_tag': "사이트/커뮤니티/"},\
	{'post_id': "65", 'info': "domain_sejong_volunteer",\
	'title': "나눔봉사단", 'date': today,\
	'post': "세종대학교 나눔봉사단 공식 홈페이지이며, 일반 봉사 및 해외 봉사 등에 관한 정보를 알려드립니다. \
[위치]집현관 115호 [Tel]02-3408-2909 [Fax]02-3408-2908",\
	'img': "http://volunteer.sejong.ac.kr/web/images/vms/common/logo_vms.png", 'url': "http://volunteer.sejong.ac.kr/main.do",\
	'title_tag': "사이트/봉사/해외/"},\
	{'post_id': "66", 'info': "domain_facebook_wooseong",\
	'title': "우정당 푸드코트", 'date': today,\
	'post': "세종대학교 우정당의 공식 페이스북 페이지입니다. 우정당에 대한 공지에 대하여을 알려드립니다. \
[위치]우정당 1층 푸드코트 [Tel]02-3409-9142",\
	'img': "4", 'url': "https://www.facebook.com/aramarksj/?rc=p",\
	'title_tag': "사이트/학식/"},\
	{'post_id': "67", 'info': "domain_facebook_sejongcarry",\
	'title': "세종대 대신 전해드립니다", 'date': today,\
	'post': "세종대학교 대신 전해드립니다, 세대전의 공식 페이스북 페이지이며, 익명으로 각종 정보를 알려드립니다.",\
	'img': "4", 'url': "https://ko-kr.facebook.com/sejonguni/",\
	'title_tag': "사이트/커뮤니티/"},\
	{'post_id': "68", 'info': "domain_promotion_reportarticle",\
	'title': "홍보실 :: 기사·홍보 제안", 'date': today,\
	'post': "행사, 연구성과, 대회수상 실적 등 학교 홍보가 될 만한 기사소재나 학교를 널리 알릴 수 있는 기발하고 참신한 아이디어가 있다면?! hongbo@sejong.ac.kr 로 제안해 주세요!\
[위치]집현관 205호 [Tel]02-3408-1460",\
	'img': "1", 'url': "http://www.sejongpr.ac.kr/contents/pr/cor/road.html",\
	'title_tag': "사이트/홍보원/소식/"},\
	{'post_id': "69", 'info': "domain_hotel_job",\
	'title': "호텔관광대학 :: 취업 게시판", 'date': today,\
	'post': "호텔관광대학 공식사이트 취업관련 게시판입니다.",\
	'img': "1", 'url': "http://home.sejong.ac.kr/bbs/bbslist.do?&bbsid=693&wslID=hoteldpt&currentPage=1",\
	'title_tag': "사이트/호텔관광대학/취업&진로/"},\
	{'post_id': "70", 'info': "domain_sejong_korean",\
	'title': "[SJ]세종대학교 국어국문학과", 'date': today,\
	'post': "세종대학교 국어국문학과 홈페이지입니다. [위치]집현관 908호 [Tel]02-3408-3301",\
	'img': "1", 'url': "http://home.sejong.ac.kr/~kordpt/",\
	'title_tag': "사이트/국어국문학과/"},\
	{'post_id': "71", 'info': "domain_sejong_international",\
	'title': "[SJ]세종대학교 국제학부", 'date': today,\
	'post': "세종대학교 국제학부 홈페이지입니다.",\
	'img': "1", 'url': "http://home.sejong.ac.kr/~interdpt/",\
	'title_tag': "사이트/국제학부/"},\
	{'post_id': "72", 'info': "domain_sejong_english",\
	'title': "[SJ]세종대학교 영어영문학과", 'date': today,\
	'post': "세종대학교 영어영문학과 홈페이지입니다. [위치]집현과 805호 [Tel]02-3408-3302",\
	'img': "1", 'url': "http://home.sejong.ac.kr/~engdpt/",\
	'title_tag': "사이트/국제학부/영어영문학과/"},\
	{'post_id': "73", 'info': "domain_sejong_japanese",\
	'title': "[SJ]세종대학교 일어일문학과", 'date': today,\
	'post': "세종대학교 일어일문학과 홈페이지입니다. [위치]집현관 715호 [Tel]02-3408-3303",\
	'img': "1", 'url': "http://japan.sejong.ac.kr/",\
	'title_tag': "사이트/국제학부/일어일문학과/"},\
	{'post_id': "74", 'info': "domain_sejong_chinatrade",\
	'title': "[SJ]세종대학교 중국통상학과", 'date': today,\
	'post': "세종대학교 중국통상학과 입니다. [위치]집현관 615호 [Tel]02-3408-3309",\
	'img': "1", 'url': "http://home.sejong.ac.kr/~cndpt/",\
	'title_tag': "사이트/국제학부/중국통상학과/"},\
	{'post_id': "75", 'info': "domain_sejong_ck",\
	'title': "[SJ]세종대학교 CK사업단", 'date': today,\
	'post': "세종대학교 국제학부 CK사업단 홈페이지입니다. [위치]집현관 815호 [Tel]02-3408-3233",\
	'img': "1", 'url': "http://home.sejong.ac.kr/~hsk/",\
	'title_tag': "사이트/국제학부/CK사업단/"},\
	{'post_id': "76", 'info': "domain_sejong_history",\
	'title': "[SJ]세종대학교 역사학과", 'date': today,\
	'post': "세종대학교 역사학과 홈페이지입니다. [위치]집현관 915호 [Tel]02-3408-3305",\
	'img': "1", 'url': "http://home.sejong.ac.kr/~histdpt/",\
	'title_tag': "사이트/역사학과/"},\
	{'post_id': "77", 'info': "domain_sejong_education",\
	'title': "[SJ]세종대학교 교육학과", 'date': today,\
	'post': "세종대학교 교육학과 홈페이지입니다. [위치]집현관 706호 [Tel]02-3408-3304",\
	'img': "1", 'url': "http://home.sejong.ac.kr/~edudpt/",\
	'title_tag': "사이트/교육학과/"},\
	{'post_id': "78", 'info': "domain_sejong_ecotrade",\
	'title': "[SJ]세종대학교 경제통상학과", 'date': today,\
	'post': "세종대학교 경제통상학과 홈페이지입니다. [위치]집현관 412호 [Tel]02-3408-3306",\
	'img': "1", 'url': "http://home.sejong.ac.kr/~entdpt/",\
	'title_tag': "사이트/경제통상학과/"},\
	{'post_id': "79", 'info': "domain_sejong_administ",\
	'title': "[SJ]세종대학교 행정학과", 'date': today,\
	'post': "세종대학교 행정학과 홈페이지입니다. [위치]집현관 604호 [Tel]02-3408-3308",\
	'img': "1", 'url': "http://home.sejong.ac.kr/~admdpt/",\
	'title_tag': "사이트/행정학과/"},\
	{'post_id': "80", 'info': "domain_sejong_mediacommunication",\
	'title': "[SJ]세종대학교 미디어커뮤니케이션학과", 'date': today,\
	'post': "세종대학교 미디어커뮤니케이션학과 홈페이지입니다. [위치]집현관 506호 [Tel]02-3408-3307",\
	'img': "1", 'url': "http://home.sejong.ac.kr/~nnbdpt/",\
	'title_tag': "사이트/미디어커뮤니케이션학과/"},\
	{'post_id': "81", 'info': "domain_sejong_management",\
	'title': "[SJ]세종대학교 경영학부", 'date': today,\
	'post': "세종대학교 경영학부 홈페이지입니다. [위치]광개토관 317호 [Tel]02-3408-3310, 3311",\
	'img': "1", 'url': "http://home.sejong.ac.kr/~mnadpt/",\
	'title_tag': "사이트/경영학부/"},\
	{'post_id': "82", 'info': "domain_sejong_hotel",\
	'title': "[SJ]세종대학교 호텔관광대학", 'date': today,\
	'post': "세종대학교 호텔관광대학 홈페이지입니다. [위치]광개토관 501호 [Tel]02-3408-3516",\
	'img': "1", 'url': "http://home.sejong.ac.kr/~hoteldpt/",\
	'title_tag': "사이트/호텔관광대학/"},\
	{'post_id': "83", 'info': "domain_sejong_hotelout",\
	'title': "[SJ]세종대학교 호텔관광외식경영학부", 'date': today,\
	'post': "세종대학교 호텔관광외식경영학부 홈페이지입니다. [위치]광개토관 517호 [Tel]02-3408-3312, 3313, 3314",\
	'img': "1", 'url': "http://home.sejong.ac.kr/~hoteldpt/",\
	'title_tag': "사이트/호텔관광대학/호텔관광외식경영학부/"},\
	{'post_id': "84", 'info': "domain_sejong_hoteltour",\
	'title': "[SJ]세종대학교 호텔외식관광프랜차이즈경영학과", 'date': today,\
	'post': "세종대학교 호텔외식관광프랜차이즈경영학과 홈페이지입니다. [위치]광개토관 1009A호 [Tel]02-3408-3952",\
	'img': "1", 'url': "http://home.sejong.ac.kr/~hoteldpt/",\
	'title_tag': "사이트/호텔관광대학/호텔외식관광프랜차이즈경영학과"},\
	{'post_id': "85", 'info': "domain_sejong_hotelbusiness",\
	'title': "[SJ]세종대학교 호텔외식비지니스학과", 'date': today,\
	'post': "세종대학교 호텔외식비지니스학과 홈페이지입니다. [위치]광개토관 1009A호 [Tel]02-3408-3500",\
	'img': "1", 'url': "http://home.sejong.ac.kr/~hoteldpt/",\
	'title_tag': "사이트/호텔관광대학/호텔외식비지니스학과/"},\
	{'post_id': "86", 'info': "domain_sejong_glovalcooking",\
	'title': "[SJ]세종대학교 글로벌조리학과", 'date': today,\
	'post': "세종대학교 글로벌조리학과 홈페이지입니다. [위치]광개토관 1009A호 [Tel]02-3408-3952",\
	'img': "1", 'url': "http://home.sejong.ac.kr/~hoteldpt/",\
	'title_tag': "사이트/호텔관광대학/글로벌조리학과/"},\
	{'post_id': "87", 'info': "domain_sejong_physicsastro",\
	'title': "[SJ]세종대학교 물리천문학과", 'date': today,\
	'post': "세종대학교 물리천문학과 홈페이지입니다. [위치]영실관 113호, 601호 [Tel]02-3408-3316(물리학과)/02-3408-3920(천문우주학과)",\
	'img': "1", 'url': "http://home.sejong.ac.kr/~phyastrodpt/",\
	'title_tag': "사이트/물리천문학과/물리학과/천문우주학과/"},\
	{'post_id': "88", 'info': "domain_sejong_chemistry",\
	'title': "[SJ]세종대학교 화학과", 'date': today,\
	'post': "세종대학교 화학과 홈페이지입니다. [위치]영실관 215호 [Tel]02-3408-3317",\
	'img': "1", 'url': "http://home.sejong.ac.kr/~chemdpt/",\
	'title_tag': "사이트/화학과/"},\
	{'post_id': "89", 'info': "domain_sejong_biolosys",\
	'title': "[SJ]세종대학교 생명시스템학부", 'date': today,\
	'post': "세종대학교 생명시스템학부 홈페이지입니다. [위치]영실관 304A호 [Tel]02-3408-3319",\
	'img': "1", 'url': "http://home.sejong.ac.kr/~biolodpt/",\
	'title_tag': "사이트/생명시스템학부/"},\
	{'post_id': "90", 'info': "domain_sejong_food",\
	'title': "[SJ]세종대학교 식품생명공학과", 'date': today,\
	'post': "세종대학교 식품생명공학과 홈페이지입니다. [위치]영실관 304A호 [Tel]02-3408-3319",\
	'img': "1", 'url': "http://home.sejong.ac.kr/~fooddpt/",\
	'title_tag': "사이트/생명시스템학부/식품생명공학과/"},\
	{'post_id': "91", 'info': "domain_sejong_bioconver",\
	'title': "[SJ]세종대학교 바이오융합공학과", 'date': today,\
	'post': "세종대학교 바이오융합공학과 홈페이지입니다. [위치]충무관 612호 [Tel]02-3408-3334",\
	'img': "1", 'url': "http://home.sejong.ac.kr/~bioscidpt/",\
	'title_tag': "사이트/생명시스템학부/바이오융합공학과/"},\
	{'post_id': "92", 'info': "domain_sejong_bioindus",\
	'title': "[SJ]세종대학교 바이오산업자원공학과", 'date': today,\
	'post': "세종대학교 바이오산업자원공학과 홈페이지입니다. [위치]다산관 211B [Tel]02-3408-3435",\
	'img': "1", 'url': "http://home.sejong.ac.kr/~bioeng/",\
	'title_tag': "사이트/생명시스템학부/바비오산업자원공학과/"},\
	{'post_id': "93", 'info': "domain_sejong_elecommunication",\
	'title': "[SJ]세종대학교 전자정보통신공학과", 'date': today,\
	'post': "세종대학교 전자정보통신공학과 홈페이지입니다. [위치]충무관 1107호 [Tel]02-3408-4467",\
	'img': "1", 'url': "http://home.sejong.ac.kr/~electrodpt/",\
	'title_tag': "사이트/전자정보통신공학과/"},\
	{'post_id': "94", 'info': "domain_sejong_computer",\
	'title': "[SJ]세종대학교 컴퓨터공학과", 'date': today,\
	'post': "세종대학교 컴퓨터공학과 홈페이지입니다. [위치]율곡관 302호 [Tel]02-3408-3321",\
	'img': "1", 'url': "http://ce.sejong.ac.kr/",\
	'title_tag': "사이트/컴퓨터공학과/"},\
	{'post_id': "95", 'info': "domain_sejong_software",\
	'title': "[SJ]세종대학교 소프트웨어학과", 'date': today,\
	'post': "세종대학교 소프트웨어학과 홈페이지입니다. [위치]율곡관 303A호 [Tel]02-3408-3667",\
	'img': "1", 'url': "http://home.sejong.ac.kr/~digitdpt/",\
	'title_tag': "사이트/소프트웨어학과/"},\
	{'post_id': "96", 'info': "domain_sejong_infoprotection",\
	'title': "[SJ]세종대학교 정보보호학과", 'date': today,\
	'post': "세종대학교 정보보호학과 홈페이지입니다. [위치]광개토관 1009B호 [Tel]02-3408-4181",\
	'img': "1", 'url': "http://home.sejong.ac.kr/~isdpt/",\
	'title_tag': "사이트/정보보호학과/"},\
	{'post_id': "97", 'info': "domain_sejong_imc",\
	'title': "[SJ]세종대학교 지능기전공학부", 'date': today,\
	'post': "세종대학교 지능기전공학부 홈페이지입니다. [위치]군자관 102호 [Tel]02-3408-3900",\
	'img': "1", 'url': "http://imc.sejong.ac.kr/",\
	'title_tag': "사이트/지능기전공학부/"},\
	{'post_id': "98", 'info': "domain_sejong_designinnovation",\
	'title': "[SJ]세종대학교 디자인이노베이션", 'date': today,\
	'post': "세종대학교 디자인이노베이션 홈페이지입니다. [위치]진관홀 514호 [Tel]02-3408-3323",\
	'img': "1", 'url': "http://home.sejong.ac.kr/~design/",\
	'title_tag': "사이트/창의소프트학부/디자인이노베이션/"},\
	{'post_id': "99", 'info': "domain_sejong_animation",\
	'title': "[SJ]세종대학교 만화애니메이션텍", 'date': today,\
	'post': "세종대학교 만화애니메이션학과 홈페이지입니다. [위치]군자관 408호 [Tel]02-3408-3328",\
	'img': "1", 'url': "http://home.sejong.ac.kr/~anitec/",\
	'title_tag': "사이트/창의소프트학부/만화애니메이션학과/"},\
	{'post_id': "100", 'info': "domain_sejong_archiengineer",\
	'title': "[SJ]세종대학교 건축공학과", 'date': today,\
	'post': "세종대학교 건축공학과 홈페이지입니다. [위치]충무관 719호 [Tel]02-3408-3331",\
	'img': "1", 'url': "http://ae.sejong.ac.kr/website/index.php",\
	'title_tag': "사이트/건축공학부/건축공학과/"},\
	{'post_id': "101", 'info': "domain_sejong_archi",\
	'title': "[SJ]세종대학교 건축학과", 'date': today,\
	'post': "세종대학교 건축학과 홈페이지입니다. [위치]충무관 719호 [Tel]02-3408-3434",\
	'img': "1", 'url': "http://arch.sejong.ac.kr/",\
	'title_tag': "사이트/건축공학부/건축학과"},\
	{'post_id': "102", 'info': "domain_sejong_build",\
	'title': "[SJ]세종대학교 건설환경공학과", 'date': today,\
	'post': "세종대학교 건설환경공학과 홈페이지입니다. [위치]충무관 718호 [Tel]02-3408-3332",\
	'img': "1", 'url': "http://home.sejong.ac.kr/~builddpt/",\
	'title_tag': "사이트/건설환경공학과/"},\
	{'post_id': "103", 'info': "domain_sejong_environmentenergy",\
	'title': "[SJ]세종대학교 환경에너지공간융합학과", 'date': today,\
	'post': "세종대학교 환경에너지공간융합학과 홈페이지입니다. [위치]영실관 516호 [Tel]02-3408-3320",\
	'img': "1", 'url': "http://home.sejong.ac.kr/~eegdpt/",\
	'title_tag': "사이트/환경에너지공간융합학과/"},\
	{'post_id': "104", 'info': "domain_sejong_energy",\
	'title': "[SJ]세종대학교 에너지자원공학과", 'date': today,\
	'post': "세종대학교 에너지자원공학과 홈페이지입니다. [위치]영실관 516호 [Tel]02-3408-3671",\
	'img': "1", 'url': "http://home.sejong.ac.kr/~energydpt/",\
	'title_tag': "사이트/에너지자원공학과/"},\
	{'post_id': "105", 'info': "domain_sejong_machine",\
	'title': "[SJ]세종대학교 기계공학과", 'date': today,\
	'post': "세종대학교 기계공학과 홈페이지입니다. [위치]충무관 1009호 [Tel]02-3408-3663",\
	'img': "1", 'url': "http://home.sejong.ac.kr/~medpt/",\
	'title_tag': "사이트/기계항공우주공학부/기계공학과/"},\
	{'post_id': "106", 'info': "domain_sejong_space",\
	'title': "[SJ]세종대학교 항공우주공학과", 'date': today,\
	'post': "세종대학교 항공우주공학과 홈페이지입니다. [위치]충무관 1009호 [Tel]02-3408-3333",\
	'img': "1", 'url': "http://home.sejong.ac.kr/~aerodpt/",\
	'title_tag': "사이트/기계항공우주공학부/항공우주공학과/"},\
	{'post_id': "107", 'info': "domain_sejong_nano",\
	'title': "[SJ]세종대학교 나노신소재공학과", 'date': today,\
	'post': "세종대학교 나노신소재공학과 홈페이지입니다. [위치]충무관 816호 [Tel]02-3408-3664, 3668",\
	'img': "1", 'url': "http://home.sejong.ac.kr/~nanodpt/",\
	'title_tag': "사이트/나노신소재공학과/"},\
	{'post_id': "108", 'info': "domain_sejong_nuclear",\
	'title': "[SJ]세종대학교 원자력공학과", 'date': today,\
	'post': "세종대학교 원자력공학과 홈페이지입니다. [위치]다산관 211A-2호 [Tel]02-3408-3491",\
	'img': "1", 'url': "http://home.sejong.ac.kr/~nuedpt/",\
	'title_tag': "사이트/원자력공학과/"},\
	{'post_id': "109", 'info': "domain_sejong_defensesys",\
	'title': "[SJ]세종대학교 국방시스템공학과", 'date': today,\
	'post': "세종대학교 국방시스템공학과 홈페이지입니다. [위치]광개토관 1009C호 [Tel]02-3408-3674",\
	'img': "1", 'url': "http://home.sejong.ac.kr/~dsedpt/",\
	'title_tag': "사이트/국방시스템공학과/"},\
	{'post_id': "110", 'info': "domain_sejong_aerosys",\
	'title': "[SJ]세종대학교 항공시스템공학과", 'date': today,\
	'post': "세종대학교 항공시스템공학과 홈페이지입니다. [위치]다산관 430호 [Tel]02-3408-3448",\
	'img': "1", 'url': "http://home.sejong.ac.kr/~aerosysdpt/",\
	'title_tag': "사이트/항공시스템공학과/"},\
	{'post_id': "111", 'info': "domain_sejong_conversation",\
	'title': "[SJ]세종대학교 회화과", 'date': today,\
	'post': "세종대학교 회화과 홈페이지입니다. [위치]진관홀 310호 [Tel]02-3408-3322",\
	'img': "1", 'url': "http://home.sejong.ac.kr/~picdpt",\
	'title_tag': "사이트/회화과/"},\
	{'post_id': "112", 'info': "domain_sejong_indusdesign",\
	'title': "[SJ]세종대학교 산업디자인학과", 'date': today,\
	'post': "세종대학교 산업디자인학과 홈페이지입니다. [위치]진관홀 514호 [Tel]02-3408-3323",\
	'img': "1", 'url': "http://home.sejong.ac.kr/~iddpt/",\
	'title_tag': "사이트/산업디자인학과/"},\
	{'post_id': "113", 'info': "domain_sejong_fashiondesign",\
	'title': "[SJ]세종대학교 패션디자인학과", 'date': today,\
	'post': "세종대학교 패션디자인학과 홈페이지입니다. [위치]군자관 202호 [Tel]02-3408-3665",\
	'img': "1", 'url': "http://sjfd.sejong.ac.kr/",\
	'title_tag': "사이트/패션디자인학과/"},\
	{'post_id': "114", 'info': "domain_sejong_music",\
	'title': "[SJ]세종대학교 음악과", 'date': today,\
	'post': "세종대학교 음악과 홈페이지입니다. [위치]모짜르트홀 102호 [Tel]02-3408-3324",\
	'img': "1", 'url': "http://home.sejong.ac.kr/~musicdpt/",\
	'title_tag': "사이트/음악과/"},\
	{'post_id': "115", 'info': "domain_sejong_pysical",\
	'title': "[SJ]세종대학교 체육학과", 'date': today,\
	'post': "세종대학교 체육학과 홈페이지입니다. [위치]용덕관 114호 [Tel]02-3408-3325",\
	'img': "1", 'url': "http://home.sejong.ac.kr/~pedpt/",\
	'title_tag': "사이트/체육학과/"},\
	{'post_id': "116", 'info': "domain_sejong_dance",\
	'title': "[SJ]세종대학교 무용과", 'date': today,\
	'post': "세종대학교 무용과 홈페이지입니다. [위치]용덕관 403호 [Tel]02-3408-3326",\
	'img': "1", 'url': "http://home.sejong.ac.kr/~dancedpt/",\
	'title_tag': "사이트/무용과/"},\
	{'post_id': "117", 'info': "domain_sejong_movie",\
	'title': "[SJ]세종대학교 영화예술학과", 'date': today,\
	'post': "세종대학교 영화예술학과 홈페이지입니다. [위치]광개토관 1201호 [Tel]02-3408-3327",\
	'img': "1", 'url': "http://home.sejong.ac.kr/~moviedpt/",\
	'title_tag': "사이트/영화예술학과/"},\
	{'post_id': "118", 'info': "domain_sejong_classic",\
	'title': "대양휴머니티칼리지", 'date': today,\
	'post': "세종대학교 대양휴머니티칼리지 홈페이지입니다. 고전독서인증, 글쓰기, 세종창의학기제, SHP 등에 관한 정보를 알 수 있습니다. [위치]광개토관 110A호 [Tel]02-3408-3929",\
	'img': "1", 'url': "http://classic.sejong.ac.kr/",\
	'title_tag': "사이트/대양휴머니티칼리지/독서퀴즈/"},\
	{'post_id': "119", 'info': "domain_sejong_law",\
	'title': "[SJ]세종대학교 법학부", 'date': today,\
	'post': "세종대학교 법학부 홈페이지입니다. [위치]집현관 304B호 [Tel]02-3408-3318",\
	'img': "1", 'url': "http://home.sejong.ac.kr/~openmajor/",\
	'title_tag': "사이트/법학부/"},\
	{'post_id': "120", 'info': "domain_sejong_phonenum1",\
	'title': "세종대학교 행정본부 전화번호부", 'date': today,\
	'post': "세종대학교 행정부서 전화번호부 pdf 파일입니다.",\
	'img': "1", 'url': "http://www.sejong.ac.kr/etc/download/01_Organization.pdf",\
	'title_tag': "사이트/전화번호부/"},\
	{'post_id': "121", 'info': "domain_sejong_phonenum1",\
	'title': "세종대학교 학과 전화번호부", 'date': today,\
	'post': "세종대학교 학과 교수님 및 조교 전화번호부 pdf 파일입니다.",\
	'img': "1", 'url': "http://www.sejong.ac.kr/etc/download/02_College.pdf",\
	'title_tag': "사이트/전화번호부/"},\
	{'post_id': "122", 'info': "domain_sejong_findinfo",\
	'title': "세종대학교 교내 전화번호 검색", 'date': today,\
	'post': "세종대학교 학과/부서/인명/기관 명으로 전화번호를 검색할 수 있는 홈페이지입니다.",\
	'img': "1", 'url': "http://www.sejong.ac.kr/etc/phonebooksearch.jsp",\
	'title_tag': "사이트/전화번호부/"},\
	{'post_id': "123", 'info': "domain_sejongout_pysics",\
	'title': "세종대학교 물리학과", 'date': today,\
	'post': "세종대학교 물리학과 홈페이지입니다. [위치]영실관 113호 [Tel]02-3408-3316",\
	'img': "1", 'url': "http://physics.sejong.ac.kr/index.php",\
	'title_tag': "사이트/물리학과/"},\
	{'post_id': "124", 'info': "domain_sejongout_astro",\
	'title': "세종대학교 천문우주학과", 'date': today,\
	'post': "세종대학교 천문우주학과 홈페이지입니다. [위치]영실관 601호 [Tel]02-3408-3920",\
	'img': "1", 'url': "http://astro.sejong.ac.kr/web/index.php",\
	'title_tag': "사이트/천문우주학과/"},\
	{'post_id': "125", 'info': "domain_sejongout_japanese",\
	'title': "세종대학교 일어일문학과", 'date': today,\
	'post': "세종대학교 일어일문학과 전공 홈페이지입니다. [위치]집현관 715호 [Tel]02-3408-3303",\
	'img': "1", 'url': "http://japan.sejong.ac.kr/",\
	'title_tag': "사이트/일어일문학과/"},\
	{'post_id': "126", 'info': "domain_sejongout_archiengineer",\
	'title': "세종대학교 건축공학과", 'date': today,\
	'post': "세종대학교 건축공학과 홈페이지입니다. [위치]충무관 719호 [Tel]02-3408-3331",\
	'img': "1", 'url': "http://ae.sejong.ac.kr/website/index.php",\
	'title_tag': "사이트/건축공학과/"},\
	{'post_id': "127", 'info': "domain_sejongout_archi",\
	'title': "세종대학교 건축학과", 'date': today,\
	'post': "세종대학교 건축학과 홈페이지입니다. [위치]충무관 719호 [Tel]02-3408-3434",\
	'img': "1", 'url': "http://arch.sejong.ac.kr/",\
	'title_tag': "사이트/건축학과/"},\
	{'post_id': "128", 'info': "domain_sejongout_computer",\
	'title': "세종대학교 컴퓨터공학과", 'date': today,\
	'post': "세종대학교 컴퓨터공학과 홈페이지입니다. [위치]율곡관 302호 [Tel]02-3408-3321",\
	'img': "1", 'url': "http://ce.sejong.ac.kr/",\
	'title_tag': "사이트/컴퓨터공학과/"},\
	{'post_id': "129", 'info': "domain_sejongout_imc",\
	'title': "세종대학교 지능기전공학부", 'date': today,\
	'post': "세종대학교 지능기전공학부 홈페이지입니다. [위치]군자관 102호 [Tel]02-3408-3900",\
	'img': "1", 'url': "http://imc.sejong.ac.kr/",\
	'title_tag': "사이트/지능기전공학부/"},\
	{'post_id': "130", 'info': "domain_classic_faq",\
	'title': "고전독서인증 FAQ", 'date': today,\
	'post': "대양휴머니티칼리지 고전독서인증FAQ에 대하여 알려드립니다.고전독서인증을 완료하였을 경우 언제, 어디에서 확인 가능한가요?\
4학년 2학기(마지막 학기)입니다. 고전독서인증 대체 이수를 위해 마지막 학기가 끝난 후 계절 학기에 <고전특강> 수강이 가능한가요?\
정규 학기에 <고전특강>을 수강하고 있습니다. 그런데 과목을 Pass하지 못할 것 같아 계절 학기에 <고전특강>을 재수강하려고 합니다. 연속으로 수강이 가능한가요?\
고전독서1(중핵필수/1학점)을 고전특강(자율교양선택/1학점) 과목으로 대체이수 하였을 경우, 총 2학점이 부여되나요?\
독서인증시험은 어디에서 보나요?예약한 날짜 및 시간에 독서인증시험을 보지 못하면 어떻게 되나요?패키지 도서는 무엇인가요?한 타임에 여러 도서를 한꺼번에 시험 볼 수 있나요?\
문제를 풀고 난 후 실수로 제출 버튼을 누르지 않았습니다. 점수는 합격점을 넘었는데 이 경우 어떻게 되나요?독서당 시험 응시는 7학기 전까지만 가능한 건가요?\
휴학 중에도 독서당 시험 응시가 가능한가요?",\
	'img': "1", 'url': "http://classic.sejong.ac.kr/info/MAIN_02_06.do",\
	'title_tag': "사이트/대양휴머니티칼리지/독서퀴즈/FAQ/"},\
	{'post_id': "131", 'info': "domain_classic_creativefaq",\
	'title': "창의학기제 FAQ", 'date': today,\
	'post': "대양휴머니티칼리지 창의학기제FAQ에 대하여 알려드립니다.세종창의학기제란 무엇인가요?세종창의학기제란 정해진 교과과정의 과목이 아닌 학생이 강의실 밖에서 자신이 도전해보고 싶은 분야의\
 학습목표와 주제를 스스로 설계하고 다양한 체험과 경험을 통해 창의적이고 전문적인 학습과제를 도전하고 수행하면서 정규학점으로 인정받고 자신의 진로를 모색하는 기회를 제공받고, 4차 산업혁명을 \
 선도하는 창의 융합적인 세종형 인재를 양성하는 특별한 교육 과정입니다.세종창의학기제 지원 대상 및 자격은 어떻게 되나요?3~8학기 재학생으로 개인 혹은 팀으로 신청 가능합니다.\
휴학생 및 초과학기 학생은 신청이 불가능합니다.자기주도 창의교양의 경우 2~5인의 재학생들이 자율적으로 학습동아리 구성이 가능합니다.단, 해외봉사의 경우 1인 신청도 가능합니다.\
자기주도 창의전공의 경우 1~5인의 재학생들이 단독 또는 팀을 만들어 신청 가능합니다.세종창의학기제 운영교과목은 어떻게 되나요?세종창의학기제 최대인정 학점은 어떻게 되나요?\
자기주도 창의교양은 6학점까지 인정 가능합니다.단, 해외봉사활동의 경우 12학점까지 가능합니다.자기주도 창의전공은 12학점까지 인정 가능합니다. 단, 현장실습(국내, 해외 인턴십)을 포함하여 18학점까지\
취득 가능합니다.세종창의학습 주제(과제) 개설 인정 기준은 어떻게 되나요?자기주도 창의교양의 경우 창의적이고 융합적인 성격의 학습 주제이며, 자기주도 창의전공의 경우 전공 분야의 창의적이고 전문적인\
성격의 학습 주제이어야 합니다.창의학습 지도교수는 어떻게 결정되나요?창의학습 지도교수는 학생이 희망하는 교수님께 직접 요청하셔야 합니다.지도교수는 교내 전임 및 비전임교수 가능하며, 다수의 \
교수님들이 팀티칭 형식의 지도도 가능합니다.단, 시간강사는 지도교수 지정이 불가능합니다.창의학습 지도교수님과 상담 혹은 지도를 받는 횟수나 기간이 정해져 있나요?\
매주 정해진 요일에 주당 2시간 이상 자기주도 창의학습을 10주 이상 진행하고, 주차별 자기주도 학습보고서를 지도교수님께 반드시 제출해야 합니다.창의학습 성적인정 기준은 어떻게 되나요?\
지도교수와 함께 창의학습운영위에서 성적을 평가하며, 평가방법은 절대평가입니다.세종창의학기제 지원 절차는 어떻게 되나요?도전하고자 하는 학습주제(과제)를 함께 할 자율적 팀(동아리)를 \
구성하고 지도교수의 추천을 받아 세종창의학기제 신청서와 자기주도 학습설계서(계획서)를 작성한 후 대양휴머니티칼리지 행정실(광개토관 110호)에 제출합니다.세종창의학기제 선발 과정은 어떻게 되나요?\
창의학습운영위원회 서류 및 면접 심사가 진행됩니다.",\
	'img': "1", 'url': "http://classic.sejong.ac.kr/info/MAIN_04_04.do",\
	'title_tag': "사이트/대양휴머니티칼리지/창의학기제/FAQ/"},\
	{'post_id': "132", 'info': "domain_counselor_faq",\
	'title': "세종대학교 학교생활상담소 FAQ", 'date': today,\
	'post': "세종대학교 학생생활상담소 FAQ 사이트입니다. 비공개 상담, 야간 위기 상담 가능 \
[이용시간]평일 a.m 09:00 ~ p.m 5:30(점심시간 p.m 12 ~ p.m 13) [위치]학생회관 310호 \
[Tel]02-3408-3336",\
	'img': "1", 'url': "http://counsel.sejong.ac.kr/index.php?mid=menu051",\
	'title_tag': "사이트/고민&상담/FAQ/"},\
	{'post_id': "133", 'info': "domain_sejong_chong",\
	'title': "세종대학교 총학생회", 'date': today,\
	'post': "세종대학교 총학생회 홈페이지입니다. 총학생회에 대한 설명, 공지와 습득 분실물 정보 및 강의 후기 등에 대하여 알려드립니다. [위치]학생회관 401호 [Tel]02-3408-3364",\
	'img': "1", 'url': "http://www.sejongstudent.com/xe/notice",\
	'title_tag': "사이트/고민&상담/FAQ/"},\
	{'post_id': "134", 'info': "domain_sejong_chonginsta",\
	'title': "[Instagram]세종대학교 총학생회", 'date': today,\
	'post': "세종대학교 총학생회 인스타그램입니다. 공지와 행사 및 이벤트 등에 대하여 알려드립니다. [위치]학생회관 401호 [Tel]02-3408-3364",\
	'img': "1", 'url': "http://www.sejongstudent.com/xe/notice",\
	'title_tag': "사이트/고민&상담/FAQ/"},\
	{'post_id': "135", 'info': "domain_everytime_book",\
	'title': "에브리타임 책방", 'date': today,\
	'post': "에브리타임 세종대학교 책&도서 대여 사이트입니다.",\
	'img': "https://www.everytime.kr/images/about/logo.png", 'url': "https://bookstore.everytime.kr/?campus=60",\
	'title_tag': "사이트/에브리타임/도서/거래&대여/"},\
	{'post_id': "136", 'info': "domain_sejongstation_class",\
	'title': "세종대역 강의후기", 'date': today,\
	'post': "세종대학교 커뮤니티 세종대역의 익명 강의후기 사이트입니다.",\
	'img': "3", 'url': "http://cafe484.daum.net/_c21_/bbs_list?grpid=1SVkj&fldid=KOd3",\
	'title_tag': "사이트/세종대역/기타/"},\
	{'post_id': "137", 'info': "domain_sejongstation_test",\
	'title': "세종대역 시험족보", 'date': today,\
	'post': "세종대학교 커뮤니티 세종대역의 익명 시험족보 사이트입니다.",\
	'img': "3", 'url': "http://cafe484.daum.net/_c21_/bbs_list?grpid=1SVkj&fldid=KOcg",\
	'title_tag': "사이트/세종대역/기타/"},\
	{'post_id': "138", 'info': "domain_dodream_main",\
	'title': "두드림 (Dodream)", 'date': today,\
	'post': "학생들이 학교를 즐겁게 다녀야 한다는 기본 이념에 따라, 비교과통합관리시스템을 창의교육개발원 비교과통합지원센터에서 명명했습니다. \
학점부담 없고, 팀플 부담 없고, 과제 부담 없이 학생들은 본인이 하고 싶은 다양한 프로그램에 참여할 수 있습니다. [위치]학술정보원 4층 비교과통합지원센터 [Tel]02-6935-2505",\
	'img': "1", 'url': "https://do.sejong.ac.kr/",\
	'title_tag': "사이트/두드림/"},\
	{'post_id': "139", 'info': "domain_mobilelibrary_main",\
	'title': "세종대학교 전자도서관", 'date': today,\
	'post': "세종대학교 전자도서관으로, 대출/반납/예약/연장 기능이 있는 온라인 디지털도서관입니다. [위치]학술정보원 [Tel]02-3408-3072",\
	'img': "1", 'url': "https://ebook.sejong.ac.kr/default.asp",\
	'title_tag': "사이트/전자도서관/"}\
)