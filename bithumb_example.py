import pybithumb
import time
import datetime

# 1. 현재 가격 가져오기
# tickers = pybithumb.get_tickers()
# for i in tickers:
#     price = pybithumb.get_current_price(i)
#     print(i, price)
#     time.sleep(0.1)


# 2. 저가, 고가, 평균 거래 금액, 거래량
# detail = pybithumb.get_market_detail("BTC")
# print(detail)


# 3. 호가
# orderbook = pybithumb.get_orderbook("BTC")
  
# for k in orderbook:
#     print(k)

# bids = orderbook['bids']  
# for bid in bids:
#     price = bid['price']
#     quant = bid['quantity']
#     print("매수호가: ", price, "매수잔량: ", quant)

# asks = orderbook['asks']
# for ask in asks:
#     print(ask)


# 여러 가상화폐 정보

all = pybithumb.get_current_price("ALL") 
for ticker, data in all.items():
    print(ticker, data['closing_price'])