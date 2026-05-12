import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

ubisoft = yf.download("UBI.PA",start="2018-07-20",end="2025-12-31")
nintendo = yf.download("TYO",start="2018-07-20",end="2025-12-31")

plt.figure(figsize=(12,6))

plt.plot(ubisoft.index,ubisoft['Close'],label="ubisoft")
plt.plot(nintendo.index,nintendo['Close'],label="nintendo")

plt.title("Closing Prices Comparison")
plt.xlabel("Date")
plt.ylabel("Stock Price")
plt.legend()

plt.show()

ubisoft_weekly = ubisoft['Close'].resample('W').mean()
print(ubisoft_weekly.head())
nintendo_weekly = nintendo['Close'].resample('W').mean()
print(nintendo_weekly.head())

plt.figure(figsize=(12, 6))

plt.plot(ubisoft["Close"], label="Close Price")
plt.plot(ubisoft["MA20"], label="20-Day MA")
plt.plot(ubisoft["MA200"], label="200-Day MA")

plt.legend()
plt.title("Ubisoft Moving Averages")
plt.xlabel("Date")
plt.ylabel("Stock Price")

plt.show()

