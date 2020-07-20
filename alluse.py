import pybithumb
import time
import datetime
import numpy as np

# API사용을 위해 로컬에서 key불러오기
with open("bithumbAPI.txt") as f:
    lines = f.readlines()
    key = lines[0].strip()
    secret = lines[1].strip()
    bithumb = pybithumb.Bithumb(key, secret)

# 목표가격 함수
def get_target_price(ticker):
    df = pybithumb.get_candlestick(ticker)
    yesterday = df.iloc[-2]

    price = yesterday["close"]
    yesterday_high = yesterday["high"]
    yesterday_low = yesterday["low"]
    target = (yesterday_high-yesterday_low)*0.5 + price
    return target

# 5일간의 이동평균 가격
def get_ma5(ticker):
    df = pybithumb.get_candlestick(ticker)
    ma5 = df["close"].rolling(5).mean()
    last_ma5 = ma5[-2]
    return last_ma5

# 구매(매수) 함수
def buy_crypto_currency(ticker):
    krw = bithumb.get_balance(ticker)[2]
    orderbook = pybithumb.get_orderbook(ticker)
    sell_price = orderbook['asks'][0]['price']   
    unit = krw/float(sell_price)
    bithumb.buy_market_order(ticker, unit)

# 판매(매도) 함수
def sell_crypto_currency(ticker):
    unit = bithumb.get_balance(ticker)[0]
    bithumb.sell_market_order(ticker, unit)

# 실제 투자 전 테스트 : 수익률 구하기
def get_ror(k):
    df = pybithumb.get_candlestick("BTC")
    # df = df["2020"]

    df['range'] = (df['high'] - df['low']) * k
    df["target"] = df['open'] + df['range'].shift(1)
    df['bull'] = df['open'] > df['ma5']

    fee = 0.0032 # 수수료
    df['ror'] = np.where((df['high'] > df['target']) & df['bull'],
                        df['close'] / df['target'] - fee, 1)

    df['hpr'] = df['ror'].cumprod()
    df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
    
    print("MDD: ", df['dd'].max())
    print("HPR: ", df['hpr'][-2])
    df.to_excel("larry_ma.xlsx")
    ror = df['ror'].cumprod()[-2]
    return ror

# 최적의 k(변동폭) 구하기
for k in np.arange(0.1, 1.0, 0.1):
    ror = get_ror(k)
    print("%.1f %f" % (k, ror))


# 메인 : 프로그램 시작
now = datetime.datetime.now()
mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
target_price = get_target_price("BTC")
ma5 = get_ma5("BTC")

while True:
    try:
        # 다음날이 되면, 판매 및 목표가격 변경
        now = datetime.datetime.now()
        if mid < now < mid + datetime.timedelta(seconds=10) : 
            sell_crypto_currency("BTC")
            mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
        
            target_price = get_target_price("BTC")
            ma5_price = get_ma5("BTC")
            
            
        # 조건 충족 시 구입
        current_price = pybithumb.get_current_price("BTC")
        if (current_price > target_price) and (current_price > ma5_price):
            buy_crypto_currency("BTC")
   
    except:
        print("error")
 
    time.sleep(1)