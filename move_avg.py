import pybithumb

# btc = pybithumb.get_ohlcv("BTC")
# close = btc["close"]
# window = close.rolling(5)
# ma = window.mean()
# print(ma)

##
def bull_marker(ticker):
    df = pybithumb.get_ohlcv(ticker)
    ma5 = df['close'].rolling(window=5).mean()
    last_ma5 = ma5[-2]
    
    price = pybithumb.get_current_price(ticker)

    if price > last_ma5:
        return True
    else:
        return False

tickers = pybithumb.get_tickers()
for i in tickers:
    isbull = bull_marker(i)
    if isbull is True:
        print(i,"상승장")
    else:
        print(i,"하락장")
