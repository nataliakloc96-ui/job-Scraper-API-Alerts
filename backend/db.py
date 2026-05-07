import psycopg2
import os

DATABASE_URL = os.getenv("postgresql://scraper_1pbr_user:FgPpAiYSIygameqwN5e8zPi0X5vU4h4x@dpg-d7tr4nnavr4c73d0abrg-a.frankfurt-postgres.render.com/scraper_1pbr")

def get_conn():
    
    return psycopg2.connect(
        DATABASE_URL,        
        sslmode="require"
    )
