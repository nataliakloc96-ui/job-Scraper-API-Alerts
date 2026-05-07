import psycopg2

def get_conn():
    
    return psycopg2.connect(
        dbname="scraper_1pbr",
        user="scraper_1pbr_user",
        password="FgPpAiYSIygameqwN5e8zPi0X5vU4h4x",
        host="dpg-d7tr4nnavr4c73d0abrg-a.frankfurt-postgres.render.com",
        port="5432",
        sslmode="require"
    )
