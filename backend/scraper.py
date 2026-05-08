from wsgiref import headers

import requests
from bs4 import BeautifulSoup
from db import get_conn
import os
from notifications import send_telegram

seen_jobs = set()

def scrape_jobs():
    url = "https://realpython.github.io/fake-jobs/"
    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.text, "html.parser")

    jobs = []

    for job in soup.select(".card-content")[:20]:
        title = job.select_one("h2").text.strip()
        company = job.select_one("h3").text.strip()
        location = job.select_one(".location").text.strip()

        jobs.append({
            "title": title,
            "company": company,
            "location": location
        })
    
    return jobs


def save_jobs(jobs):
    conn = get_conn()
    cursor = conn.cursor()
    print("CONNECTING TO DB...")
    print("HOST:", os.getenv("DB_HOST"))

    for job in jobs:
        key = (job["title"], job["company"])

        cursor.execute("""
            INSERT INTO jobs (title, company, location) 
            VALUES( %s, %s, %s)
            ON CONFLICT (title, company, location) DO NOTHING
            
        """, job) 

        if cursor.rowcount > 0:
            send_telegram(f"🆕 NEW JOB:\n{job[0]}\n{job[1]}\n{job[2]}")
            

        
    conn.commit()
    cursor.close()
    conn.close()

