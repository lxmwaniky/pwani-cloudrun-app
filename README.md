# Pwani Cloud Run Application

A production-grade, asynchronous web service built with **Python 3.14** and **FastAPI**, managed using **uv**. Developed as part of the GDG Pwani Google Cloud Study Jams assignment.

## Features
- **`/`**: Returns a welcoming message.
- **`/health`**: Endpoint for tracking container health status.
- **`/info`**: Dynamically fetches and displays container hostname and timestamp records.

---

## Local Setup & Development

1. **Clone the repository:**
   ```bash
   git clone https://github.com/lxmwaniky/pwani-cloudrun-app.git
   cd pwani-cloudrun-app
    ```

2. **Install dependencies using uv:**
   ```bash
   uv sync
   ```

3. **Run the local development server:**
   ```bash
   uv run uvicorn main:app --reload --port 8080
   ```

## Dockerization & Cloud Run Deployment

1. **Build the container image locally:**
   ```bash
   docker build -t pwani-cloudrun-app .
   ```

2. **Run the container locally to test:**
   ```bash
   docker run -p 8080:8080 -d pwani-cloudrun-app
   ```

3. **Push the image to Google Container Registry (GCR):**
   ```bash
   gcloud builds submit --tag gcr.io/[PROJECT-ID]/pwani-cloudrun-app .
   ```

4. **Deploy to Google Cloud Run:**
   ```bash
   gcloud run deploy pwani-cloudrun-app \
    --image gcr.io/[PROJECT-ID]/pwani-cloudrun-app \
    --platform managed \
    --region us-central1 \
    --allow-unauthenticated \
    --port 8080
   ```