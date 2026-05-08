import requests
from bs4 import BeautifulSoup
from db import get_conn
import os
from notifications import send_telegram

seen_jobs = set()

def scrape_jobs():
    url = "https://realpython.github.io/fake-jobs/"
    res = requests.get(url)

    soup = BeautifulSoup(res.text, "html.parser")

    jobs = []

    for job in soup.select(".card-content"):
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
            SELECT %s, %s, %s
            WHERE NOT EXISTS (
                       SELECT 1 FROM jobs 
                       WHERE title = %s AND company = %s
            )
        """, (
            job["title"], job["company"], job["location"],
            job["title"], job["company"]
             

        ))

        if key not in seen_jobs:
            seen_jobs.add(key)

            send_telegram(f"🆕 NEW JOB:\n{job['title']}\n{job['company']}\n{job['location']}"
            )
    conn.commit()
    conn.close()

if __name__ == "__main__":
    data = scrape_jobs()
    save_jobs(data)
    print("Zapisano:", len(data))