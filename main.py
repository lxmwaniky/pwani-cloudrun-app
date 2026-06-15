import datetime
import socket
from fastapi import FastAPI

app = FastAPI(title="Cloud Study Jams Pwani")



@app.get("/")
def read_root():
    return {
        "message": "Welcome to Cloud Run",
        "name": "Alex Nyambura"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/info")
def get_info():
    return {
        "hostname": socket.gethostname(),
        "timestamp": datetime.datetime.now().isoformat()
    }