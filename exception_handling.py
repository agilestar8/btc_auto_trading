import pybithumb
import time

while(True):
    price = pybithumb.get_current_price("BTC")
    try:
        print(price/10)
       
    except:
        print("error", price)

    time.sleep(0.2)
