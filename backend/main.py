from fastapi import FastAPI 
from scraper import scrape_jobs, save_jobs
from db import get_conn
from fastapi.middleware.cors import CORSMiddleware
from apscheduler.schedulers.background import BackgroundScheduler
from scraper import scrape_jobs, save_jobs
import atexit
import requests
import os



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[""https://job-scraper-api-alerts.vercel.app",
    "https://job-scraper-api-alerts-git-main-nataliakloc96-uis-projects.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

    response = requests.post(url, json={
        "chat_id": CHAT_ID,
        "text": message
    })
    print("TELEGRAM STATUS:", response.status_code)
    print("TELEGRAM RESPONSE:", response.text)



def init_db():
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
                   id SERIAL PRIMARY KEY, 
                   title TEXT,
                   company TEXT,
                   location TEXT,
                   UNIQUE(title, company, location)
        );

    """)

    conn.commit()
    cursor.close()
    conn.close()

init_db()

def auto_scrape():
    print("AUTO SCRAPE STARTED")
    try:
        jobs = scrape_jobs()
        save_jobs(jobs)
        print(f"Saved: {len(jobs)} jobs")
    except Exception as e:
        print("AUTO SCRAPE ERROR:", e)


@app.get("/jobs")
def get_jobs():
    conn = get_conn()
  
    cursor = conn.cursor()

    cursor.execute("SELECT title, company, location FROM jobs ORDER BY id DESC LIMIT 50")
    rows = cursor.fetchall()

    cursor.close()

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
        "SELECT current_database();")
    db = cursor.fetchone()

    cursor.execute("SELECT inet_server_addr();")
    host = cursor.fetchone()

    cursor.execute("SELECT COUNT(*) FROM jobs;")
    count = cursor.fetchone()

    return {
        "database": db,
        "host": host,
        "count": count
    }

@app.get("/health")
def health():
    return {"ok": True}

@app.on_event("startup")
def startup():
    init_db()

@app.get("/")
def root():
    return {"status": "API running"}
    
scheduler = BackgroundScheduler()
scheduler.add_job(auto_scrape, 'interval', minutes=10)
scheduler.start()
    

