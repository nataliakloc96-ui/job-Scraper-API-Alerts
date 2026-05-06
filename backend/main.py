from fastapi import FastAPI 
from scraper import scrape_jobs, save_jobs
from db import get_conn

app = FastAPI()

@app.get("/jobs")
def get_jobs():
    conn = get_conn()
  
    cursor = conn.cursor()

    cursor.execute("SELECT title, company, location FROM jobs ORDER BY id DESC LIMIT 50")
    rows = cursor.fetchall()

    conn.close()

    return{
        "jobs": [
            {"title": r[0], "company": r[1], "location": r[2]}
            for r in rows
        ]
    }


@app.post("/scrape")
def scrape():
    data = scrape_jobs()
    save_jobs(data)
    return {"saved": len(data)}

def run_scraper():
    try:
        jobs = scrape_jobs()
        print("SCRAPED:", len(jobs))

        save_jobs(jobs)
        return {"status": f"{len(jobs)} jobs saved"}
    except Exception as e:
        print("ERROR:", e)
        return {"error": str(e)}
    
@app.get("/debug-db")
def debug_db():
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute (
        "SELECT current_database();"
    )
    db = cursor.fetchone()

    cursor.execute("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema='public';
    """)
    tables = cursor.fetchall()

    return {
        "database": db,
        "tables": tables
    }
