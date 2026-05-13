import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

ubisoft = yf.download("UBI.PA",start="2018-07-20",end="2025-12-31")
nintendo = yf.download("7974.T",start="2018-07-20",end="2025-12-31")

ubisoft["MA20"] = ubisoft["Close"].rolling(window=20).mean()
ubisoft["MA200"] = ubisoft["Close"].rolling(window=200).mean()

nintendo["MA20"] = nintendo["Close"].rolling(window=20).mean()
nintendo["MA200"] = nintendo["Close"].rolling(window=200).mean()

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

plt.plot(ubisoft["Close"], label="Close Price Ubisoft")
plt.plot(ubisoft["MA20"], label="20-Day MA")
plt.plot(ubisoft["MA200"], label="200-Day MA")

plt.legend()
plt.title("Ubisoft Moving Averages")
plt.xlabel("Date")
plt.ylabel("Stock Price")

plt.show()


plt.plot(nintendo["Close"], label="Close Price Nintendo")
plt.plot(nintendo["MA20"], label="20-Day MA")
plt.plot(nintendo["MA200"], label="200-Day MA")

plt.legend()
plt.title("Nintendo Moving Averages")
plt.xlabel("Date")
plt.ylabel("Stock Price")

plt.show()

plt.figure(figsize=(12, 6))

plt.plot(ubisoft.index, ubisoft["Volume"], label="Ubisoft Volume")
plt.plot(nintendo.index, nintendo["Volume"], label="Nintendo Volume")

plt.title("Trading Volume Comparison")
plt.xlabel("Date")
plt.ylabel("Volume")
plt.legend()

plt.show()
