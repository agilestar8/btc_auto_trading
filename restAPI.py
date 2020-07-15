import requests 
import datetime

r = requests.get("https://api.korbit.co.kr/v1/ticker/detailed?currency_pair=btc_krw")

# Response객체는 json() 메서드를 호출하여 JSON 포맷의 데이터를 딕셔너리로 변환할 수 있습니다.
btc = r.json()

timestamp = btc["timestamp"]
date = datetime.datetime.fromtimestamp(timestamp/1000)
print(date)




