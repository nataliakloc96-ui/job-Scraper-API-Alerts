const API = "https://job-scraper-api-alerts.onrender.com";

async function loadJobs() {
    const res = await fetch(`${API}/jobs`);
    const data = await res.json();
    console.log(data);

    document.getElementById("jobs").innerHTML =
        data.jobs.map(job =>
            `<li>${job.title} — ${job.company} (${job.location})</li>`
        ).join("");
}

async function loadStats() {
    const res = await fetch(`${API}/debug-db`);
    const data = await res.json();
    console.log(data);

    document.getElementById("stats").innerHTML =
        `DB: ${data.database} | Jobs: ${data.count}`;
}

async function scrapeJobs() {
    const res = await fetch(`${API}/scrape`, { method: "POST" });
    const data = await res.json();
    console.log(data);

}

fetch(`${API}/jobs`)
fetch(`${API}/debug-db`)
fetch(`${API}/scrape`, { method: "POST" })
