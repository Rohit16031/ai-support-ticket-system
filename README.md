# AI Support Ticket Analytics System

## Overview

This project is an AI-powered support ticket analytics system built using FastAPI, Pandas, LangChain, and Groq LLM.

The system allows users to query support ticket data using natural language, detect anomalies in support operations, and visualize everything through an interactive analytics dashboard.

---

## Features

* Natural language querying using LLM
* CSV-based ticket data ingestion
* REST API endpoints
* Rule-based anomaly detection
* Swagger API documentation
* Modular backend architecture
* Interactive analytics dashboard (no frontend framework needed)

---

## Tech Stack

* Python
* FastAPI
* Pandas
* LangChain
* Groq LLM
* Uvicorn
* HTML / CSS / Vanilla JS (Dashboard)
* Chart.js (Dashboard charts)

---

## Project Structure

```text
ai-support-system/
│
├── main.py
├── data_loader.py
├── llm_query.py
├── anomaly_detector.py
├── prompts.py
├── dashboard.html
├── support_tickets.csv
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

## Setup Instructions

### 1. Create Virtual Environment

```bash
python -m venv venv
```

### 2. Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

> If you get a script execution error, run this first:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Groq API Key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_api_key_here
```

Get a free API key at: https://console.groq.com

### 5. Run the Server

```bash
uvicorn main:app --reload
```

### 6. Open the Dashboard

Visit in your browser:

```
http://localhost:8000/dashboard
```

---

## Dashboard

The dashboard is a single HTML file (`dashboard.html`) served directly by FastAPI. No Node.js, React, or separate frontend server needed.

### Tabs

* **Overview** — KPI cards, monthly trend, status distribution, category and priority breakdowns
* **Tickets** — Full searchable and filterable ticket table with pagination
* **Agents** — Agent performance charts and leaderboard
* **Anomalies** — Live anomaly detection results from the backend
* **AI Query** — Natural language interface powered by Groq LLM

### Backend Integration

The dashboard connects to the FastAPI backend automatically on load:

* `GET /health` — checks if backend is online (shown as green/red dot in sidebar)
* `GET /anomalies` — fetches anomaly data from the backend
* `POST /query` — sends natural language questions to the Groq LLM

If the backend is offline, the dashboard falls back to embedded ticket data for charts and tables.

---

## API Endpoints

### Health Check

```
GET /health
```

---

### Dashboard UI

```
GET /dashboard
```

---

### Natural Language Query

```
POST /query
```

Example request:

```json
{
  "question": "How many open tickets are there?"
}
```

Example response:

```json
{
  "question": "How many open tickets are there?",
  "answer": "There are 111 open tickets currently."
}
```

---

### Anomaly Detection

```
GET /anomalies
```

---

### Swagger Docs

```
GET /docs
```

---

## Example Queries

* How many open tickets are there?
* Which agent resolved the most tickets?
* What is the average customer rating?
* How many escalated tickets are there?
* Which agent has the lowest rating?
* What are the most common issue types?

---

## Architecture

```
User (Browser)
↓
dashboard.html → FastAPI (main.py)
                    ↓              ↓
              POST /query     GET /anomalies
                    ↓              ↓
            LangChain Agent   anomaly_detector.py
                    ↓              ↓
               Groq LLM       Pandas DataFrame
                    ↓              ↓
            Pandas DataFrame  support_tickets.csv
                    ↓
          support_tickets.csv
```

---

## Anomaly Detection Logic

The system identifies:

* Critical unresolved tickets
* Abnormally long resolution times (> 20 hours)
* Poor customer ratings (≤ 2 stars)

---

## Future Improvements

* Database integration
* Authentication & authorization
* Advanced ML-based anomaly detection
* Real-time analytics with WebSockets
* Export reports to PDF / Excel