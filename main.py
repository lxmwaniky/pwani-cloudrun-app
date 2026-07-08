import datetime
import socket
import time
import json
from fastapi import FastAPI, Request, HTTPException

app = FastAPI(title="Cloud Study Jams Pwani")

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    try:
        response = await call_next(request)
        process_time = (time.time() - start_time) * 1000
        
        status_code = response.status_code
        # Determine GCP severity
        if status_code >= 500:
            severity = "ERROR"
        elif status_code >= 400:
            severity = "WARNING"
        else:
            severity = "INFO"
            
        log_data = {
            "severity": severity,
            "message": f"{request.method} {request.url.path} - {status_code} ({process_time:.2f}ms)",
            "method": request.method,
            "path": request.url.path,
            "status_code": status_code,
            "latency_ms": round(process_time, 2),
        }
        print(json.dumps(log_data), flush=True)
        return response
    except Exception as exc:
        process_time = (time.time() - start_time) * 1000
        log_data = {
            "severity": "ERROR",
            "message": f"{request.method} {request.url.path} - 500 Internal Server Error: {str(exc)} ({process_time:.2f}ms)",
            "method": request.method,
            "path": request.url.path,
            "status_code": 500,
            "latency_ms": round(process_time, 2),
            "exception": str(exc)
        }
        print(json.dumps(log_data), flush=True)
        raise exc

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

@app.get("/demo-400")
def trigger_400():
    raise HTTPException(status_code=400, detail="Demo Bad Request (400 Error)")

@app.get("/demo-500")
def trigger_500():
    raise HTTPException(status_code=500, detail="Demo Internal Server Error (500 Error)")