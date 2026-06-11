import psycopg2

conn = psycopg2.connect(
    host="127.0.0.1",
    port=5433,
    database="stocks",
    user="admin",
    password="admin123"
)

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS stocks (
    id SERIAL PRIMARY KEY,
    ticker VARCHAR(10),
    date TIMESTAMP,
    open NUMERIC,
    high NUMERIC,
    low NUMERIC,
    close NUMERIC,
    volume BIGINT
);
""")

conn.commit()

print("Table created successfully!")

cur.close()
conn.close()