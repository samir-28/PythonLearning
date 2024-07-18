import yfinance as yf

Stock=input("Enter the stock name:")
market_data=yf.Ticker(Stock).history(period="1d")
last_mp=market_data['Close'].iloc[-1]
print("Last Market Price was:",last_mp)