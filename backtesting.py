import pybithumb
import numpy as np
import pandas as pd

# 1. 수익률 구하기
def get_ror(ticker,k):
    df = pybithumb.get_candlestick(ticker)
    df = df["2020"]

    df['range'] = (df['high'] - df['low']) * k
    df["target"] = df['open'] + df['range'].shift(1)

    fee = 0.0032 # 수수료
    df['ror'] = np.where(df['high'] > df['target'], 
                        df['close'] / df['target'] - fee, 1)


    ror = df['ror'].cumprod()[-2]
    return ror

for k in np.arange(0.1, 1.0, 0.1):
    ror = get_ror("APIX",k)
    print("%.1f %f" % (k, ror))


# 2. MDD(Maximum Draw Down)은 투자 기간 중에 포트폴리오의 전 고점에서 저점까지의 최대 누적 손실
# df = pybithumb.get_candlestick("BTC")
# df = df["2020"]

# df['range'] = (df['high'] - df['low']) * 0.5
# df["target"] = df['open'] + df['range'].shift(1)


# fee = 0.0032 # 수수료
# df['ror'] = np.where(df['high'] > df['target'], 
#                     df['close'] / df['target'] - fee, 1)

# ror = df['ror'].cumprod()[-2]

# df['hpr'] = df['ror'].cumprod()
# df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
# print(df)
# print("MDD(%): ", df['dd'].max())
# df.to_excel("backtest.xlsx")

