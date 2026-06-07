# AI Support Ticket Analytics System

## Overview

This project is an AI-powered support ticket analytics system built using FastAPI, Pandas, LangChain, and Groq LLM.

The system allows users to query support ticket data using natural language and detect anomalies in support operations.

---

## Features

* Natural language querying using LLM
* CSV-based ticket data ingestion
* REST API endpoints
* Rule-based anomaly detection
* Swagger API documentation
* Modular backend architecture

---

## Tech Stack

* Python
* FastAPI
* Pandas
* LangChain
* Groq LLM
* Uvicorn

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

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Groq API Key

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key
```

### 5. Run the Server

```bash
uvicorn main:app --reload
```

---

## API Endpoints

### Health Check

GET `/health`

---

### Natural Language Query

POST `/query`

Example:

```json
{
  "question": "How many open tickets are there?"
}
```

---

### Anomaly Detection

GET `/anomalies`

---

## Example Queries

* How many open tickets are there?
* Which agent resolved the most tickets?
* What is the average customer rating?
* How many escalated tickets are there?

---

## Architecture

User Query
↓
FastAPI API Layer
↓
LangChain Pandas Agent
↓
Groq LLM
↓
Pandas DataFrame
↓
Response

---

## Anomaly Detection Logic

The system identifies:

* Critical unresolved tickets
* Abnormally long resolution times
* Poor customer ratings

---

## Future Improvements

* Database integration
* Authentication & authorization
* Advanced ML-based anomaly detection
* Dashboard UI
* Real-time analytics
