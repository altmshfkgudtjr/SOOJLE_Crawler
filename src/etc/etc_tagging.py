ETC_TAGGINGS = ["무방관", "세종초등학교", "평생교육원", "용덕관", "영실관", "진관홀", "충무관", "우정당", "다산관", "ai센터", "ai 센터"\
				, "동천관", "아사달", "학생회관", "율곡관", "애지헌", "세종관", "대양홀", "모짜르트홀", "집현관", "군자관", "이당관", "광개토관"\
				, "진관홀"]

# 세종대학교 대상 예외적인 단어 태깅함수
def add_sejongbuild_tag(input, title, post):
	text = title + post
	for tag in ETC_TAGGINGS:
		if text.find(tag) != -1:
			if tag == "ai센터" or "ai 센터":
				input.append("대양ai센터")
			else:
				input.append(tag)
	return list(set(input))