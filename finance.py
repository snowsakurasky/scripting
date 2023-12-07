import yfinance as yf

df = yf.download("2330.TW", start='2021-12-03', end='2023-12-04')
print(df)

df.to_csv('fileoutput.csv', index=True, sep=',')
