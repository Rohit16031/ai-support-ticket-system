from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from llm_query import ask_question
from anomaly_detector import detect_anomalies
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse


app = FastAPI(
    title="AI Support Ticket System"
)
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
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

@app.get("/dashboard")
def dashboard():
    return FileResponse("dashboard.html")

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