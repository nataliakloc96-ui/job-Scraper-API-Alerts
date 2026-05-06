import psycopg2

def get_conn():
    print("CONNECTING LOCAL DB (SSL DISABLED)")

    return psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="1111",
        host="localhost",
        port="5432",
        sslmode="disable"   # 🔥 NA SZTYWNO
    )