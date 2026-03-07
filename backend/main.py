from fastapi import FastAPI
from ai_router import chat_ai
from tracker import log_hours, progress

app = FastAPI()

@app.get("/")
def root():
    return {"status": "InternTrack API running"}

@app.post("/chat")
def chat(message: str):
    return chat_ai(message)

@app.post("/log_hours")
def log(data: dict):
    return log_hours(data)

@app.get("/progress")
def get_progress(total: int, current: int):
    return progress(total, current)