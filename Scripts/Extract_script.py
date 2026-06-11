import yfinance as yf
import psycopg2

# Download stock data
ticker = yf.Ticker("AAPL")
df = ticker.history(period="5d")

print(df)

# PostgreSQL connection
conn = psycopg2.connect(
    host="127.0.0.1",
    port=5433,
    database="stocks",
    user="admin",
    password="admin123"
)

cursor = conn.cursor()

# Insert data
for index, row in df.iterrows():
    cursor.execute("""
        INSERT INTO stock_prices
        (ticker, trade_date, open, high, low, close, volume)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
    """,
    (
        "AAPL",
        index.date(),
        float(row["Open"]),
        float(row["High"]),
        float(row["Low"]),
        float(row["Close"]),
        int(row["Volume"])
    ))

conn.commit()

print("Data inserted successfully!")

cursor.close()
conn.close()