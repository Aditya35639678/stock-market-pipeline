import psycopg2

try:
    conn = psycopg2.connect(
        host="127.0.0.1",
        port=5433,
        database="stocks",
        user="admin",
        password="admin123"
    )

    print("Connected successfully!")

    conn.close()

except Exception as e:
    print("ERROR:")
    print(e)