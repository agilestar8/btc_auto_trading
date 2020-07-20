import pybithumb
import time

con_key = "835ee5da01b4c47d71aba33d3d5cc504"
sec_key = "49a50081960f2bf6c12a656d5e9e09a1"

bithumb = pybithumb.Bithumb(con_key, sec_key) # 빗썸 객체

# 1. get_balance(화폐) : 잔고 확인
#  순서대로 총 잔고, 거래 중인 비트코인의 수량, 보유 중인 총원화, 주문에 사용된 원화를 의미

# for i in pybithumb.get_tickers():
#     balance = bithumb.get_balance(i)
#     print(i,":",balance)
#     time.sleep(0.1)


# 2. buy_limit_order(화폐,구매할 가격,구매 개수) : 지정가 구매

# order = bithumb.buy_limit_order("BTC", 3900000, 0.001) # BTC를 / 390만원에 / 0.001개 구입
# print(order)


# 3. buy_market_order(화폐, 구매 개수) : 시장가 매수

# order = bithumb.buy_market_order("BTC", 1)      # BTC를, 1개
# print(order)

# 4. 본인 계좌의 보유 원화를 조회하고, 최우선 매도 호가 금액을 얻어와 매수할 수 있는 비트코인 개수를 계산

krw = bithumb.get_balance("BTC")[2] # 거래 수량 가져옴
orderbook = pybithumb.get_orderbook("BTC") # BTC 정보 가져옴
 
asks = orderbook['asks']        # BTC정보중 호가정보(가격,남은 수량) 가져옴
sell_price = asks[0]['price']   # 호가의 가격 가져옴
unit = krw/float(sell_price)           # 내 돈 / 현재 가격 = 구매할 수 있는 개수
print(unit)

# 실제 주문
# order = bithumb.buy_market_order("BTC", unit)
# print(order) # 주문번호

