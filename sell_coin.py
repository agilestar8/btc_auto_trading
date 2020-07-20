import pybithumb

con_key = "835ee5da01b4c47d71aba33d3d5cc504"
sec_key = "49a50081960f2bf6c12a656d5e9e09a1"

bithumb = pybithumb.Bithumb(con_key,sec_key)

# 1. sell_limit_order(화폐, 판매할 가격, 판매할 개수) : 지정가 매도

order = bithumb.sell_limit_order("BTC",10000000, 1)     # 판매
unit = bithumb.get_balance("BTC")[0]                       # BTC잔고정보 조회(총 잔고,거래중인 수량,원화,사용된 원화)
print(unit)

# 2. cancel_order(주문번호) : 주문 취소

cancel = bithumb.cancel_order(order)
print(cancel)





