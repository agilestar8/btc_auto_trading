import requests
from bs4 import BeautifulSoup

# 웹 페이지 다운로드는 requests 모듈을 사용하고 
# 웹 페이지에서 원하는 데이터를 가져가는 파싱(parsing)은 BeautifulSoup 모듈을 사용

# 객체를 생성할 때 html 데이터와 HTML 문서를 파싱하는데 사용할 모듈의 이름인 "html5lib"을 넘겨주면 된다.
# select() 메서드를 사용하면 앞서 배운 CSS 셀렉터를 사용해서 HTML문서를 파싱

def get_per(code):
    url = "http://finance.naver.com/item/main.nhn?code=" + code
    html = requests.get(url).text

    soup = BeautifulSoup(html, "html.parser")

    tags = soup.select("#_per") #                   ("#_per")의미 : id셀렉터 = "_per"
    tag = tags[0]

    return float(tag.text)


def get_dvr(code):
    url = "http://finance.naver.com/item/main.nhn?code=" + code
    html = requests.get(url).text

    soup = BeautifulSoup(html,"html.parser")

    tags = soup.select("#_dvr")
    tag = tags[0]

    return float(tag.text)

def get_BA(code):
    url = "http://finance.naver.com/item/main.nhn?code=" + code
    html = requests.get(url).text

    soup = BeautifulSoup(html,"html.parser")
                            
    # tags = soup.select("table tbody tr td em") 
    # tags = soup.select(".lwidth tbody .strong td em")   # .strong td em : class셀렉터 = "strong"+td+ems
    # tags = soup.select("#tab_con1 > div:nth-child(3) > table > tbody > tr.strong > td > em")   
    tags = soup.select("#tab_con1 > div:nth-of-type(2) > table > tbody > tr.strong > td > em")
    
    return tags

for tag in get_BA("000660"):
        print(tag.text)
