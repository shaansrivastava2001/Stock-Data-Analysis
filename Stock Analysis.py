pip install yfinance

import yfinance as yf
import pandas as pd

apple = yf.Ticker('AAPL')
apple_info = apple.info
print("Apple_info: ",apple_info)

print("Country: ",apple_info['country'])
print("Sector: ",apple_info['sector'])

apple_share_price_data = apple.history(period="max")
apple_share_price_data.reset_index(inplace=True)
apple_share_price_data.plot(x="Date", y="Open")

print(apple.dividends)
apple.dividends.plot()