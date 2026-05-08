const API = "https://job-scraper-api-alerts.onrender.com";

async function loadJobs() {
    const res = await fetch(`${API}/jobs`);
    const data = await res.json();

    document.getElementById("jobs").innerHTML = 
    data.jobs.map(j =>
        `<li>${j.title} - ${j.company} (${j.location})</li>`
    ).join("");
}

        
async function loadStats() {
    const res = await fetch(`${API}/debug-db`);
    const data = await res.json();

    document.getElementById("stats").innerHTML = 
    `DB: ${data.database} | Jobs: ${data.count}`;
}
