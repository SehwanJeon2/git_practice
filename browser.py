import webbrowser

webbrowser.open("https://daum.net")

#모모랜드 모든 멤버들의 검색 페이지를 한 번에 여는 코드


#webbrowser.open("https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EB%AA%A8%EB%AA%A8%EB%9E%9C%EB%93%9C")
#webbrowser.open("https://search.daum.net/search?w=tot&q=%EB%82%98%EC%9C%A4&ppkey=2081279&rtmaxcoll=PRF")
#webbrowser.open("https://search.daum.net/search?w=tot&q=%ED%98%9C%EB%B9%88&ppkey=2081895&rtmaxcoll=PRF")


url = "https://search.daum.net/search?q="
momo = [
    "나윤", "혜빈", "아인", "낸시", "주이", "연우", "제인",
    "데이지", "태하"
]

#keyword = input("검색어를 입력해 주세요: ")
for myGirl in momo:
    webbrowser.open(url + myGirl)


#webbrowser.open(url + keyword)