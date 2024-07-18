import yfinance as yf
import mplfinance as mpf

symbol=input("Enter Stock Name:")
start_date='2022-01-01'
end_date='2024-04-01'

stock_data=yf.download(symbol,start=start_date,end=end_date)
mpf.plot(stock_data ,type='candle', style='yahoo' ,title=f'{symbol} Candlestick chart')