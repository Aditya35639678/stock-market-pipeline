import yfinance as yf
import psycopg2

# Download stock data
tickers = ["AAPL", "MSFT", "GOOGL", "NVDA"]

# PostgreSQL connection
conn = psycopg2.connect(
        host="127.0.0.1",
        port=5433,
        database="stocks",
        user="admin",
        password="admin123"
    )
cur = conn.cursor()

for symbol in tickers:
    ticker = yf.Ticker(symbol)
    df = ticker.history(period="2y")
    df = df.dropna(subset=["Open", "High", "Low", "Close"])
    #print(df.head())
    #print(df.tail())
    #print("Rows:", len(df))

    for index, row in df.iterrows():

        cur.execute("""
        INSERT INTO stocks
        (ticker, date, open, high, low, close, volume)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
        ON CONFLICT (ticker, date)
        DO NOTHING
    """,
    (
        symbol,
        index.to_pydatetime(),
        float(row["Open"]),
        float(row["High"]),
        float(row["Low"]),
        float(row["Close"]),
        int(row["Volume"])
    ))
    print(f"Finished loading {symbol}")

conn.commit()
cur.close()
conn.close()