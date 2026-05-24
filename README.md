# Job Scraper API + Alerts

Production-ready job scraping and alerting platform that automatically collects job offers, stores them in PostgreSQL, removes duplicates, and sends real-time Telegram notifications.

## Live Demo

Frontend (Vercel):
job-scraper-api-alerts.vercel.app

Backend API (Render):  
https://job-scraper-api-alerts.onrender.com

Repository:  
https://github.com/nataliakloc96-ui/job-Scraper-API-Alerts.git

---

## Features

### Automated Job Scraping
Scrapes job listings automatically from external job boards.

### PostgreSQL Storage
Stores scraped jobs in database with persistent tracking.

### Duplicate Detection
Uses PostgreSQL conflict handling to prevent duplicate entries.

### Telegram Alerts
Instant notifications for newly discovered jobs.

### REST API
Expose collected jobs through FastAPI endpoints.

### Production Deployment
Cloud deployed on Render.

---

## Tech Stack

### Backend
- Python
- FastAPI
- PostgreSQL
- psycopg2
- BeautifulSoup
- requests

### Integrations
- Telegram Bot API

### Deployment
- Render

---

## Architecture

Job Sources  
↓  
Web Scraper Engine  
↓  
Data Parsing  
↓  
PostgreSQL Storage  
↓  
Duplicate Filtering  
↓  
Telegram Alerts  
↓  
REST API Delivery

---

## API Endpoints

### Get Jobs
`GET /jobs`

Returns stored jobs.

---

### Run Scraper
`POST /scrape`

Triggers scraping manually.

---

### Health Check
`GET /`

Backend status check.

---

## Database Logic

Uses conflict-safe inserts:

```sql
INSERT INTO jobs (...)
ON CONFLICT DO NOTHING
```

This guarantees no duplicate job records.

---

## Telegram Alerts

When new jobs are detected:

- Title
- Company
- Location
- Timestamp

are automatically sent via Telegram bot.

---

## Installation

Clone repository:

```bash
git clone https://github.com/nataliakloc96-ui/job-Scraper-API-Alerts.git
cd Job-Scraper-API-Alerts
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure environment variables:

```env
DATABASE_URL=
TELEGRAM_TOKEN=
CHAT_ID=
```

Run backend:

```bash
uvicorn main:app --reload
```

---

## Example Workflow

1. Scraper fetches jobs
2. Parses job data
3. Stores unique records
4. Detects new jobs
5. Sends Telegram alerts
6. API exposes collected jobs

---

## Screenshots

Add screenshots here:

- Telegram alerts
- Database records
- API response
- Render deployment dashboard

---

## Business Value

Automates job discovery and alerting for faster opportunity tracking without manual searching.

Useful for:

- job seekers
- recruiters
- monitoring niche job markets
- backend automation workflows

---

## Future Improvements

- Multi-board scraping
- Scheduled background workers
- Email alerts
- Admin dashboard
- Filtering by role/location
- Resume-job fit integration

---

## Author

Natalia Kurek

Backend / Automation / Data Engineering Portfolio Project