from fastapi import FastAPI
from pydantic import BaseModel

from llm_query import ask_question
from anomaly_detector import detect_anomalies

app = FastAPI(
    title="AI Support Ticket System"
)

# Request model
class QueryRequest(BaseModel):
    question: str

# Root endpoint
@app.get("/")
def root():
    return {
        "message": "AI Support Ticket System Running"
    }

# Health check endpoint
@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

# Natural language query endpoint
@app.post("/query")
def query_data(request: QueryRequest):

    answer = ask_question(request.question)

    return {
        "question": request.question,
        "answer": answer
    }

# Anomaly detection endpoint
@app.get("/anomalies")
def anomalies():

    return {
        "anomalies": detect_anomalies()
    }