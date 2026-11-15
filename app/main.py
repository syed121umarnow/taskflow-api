
from fastapi import FastAPI

app = FastAPI(
    title="TaskFlow API",
    description="A task management REST API built with FastAPI",
    version="1.0.0",
)


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "application": "taskflow-api",
        "version": "1.0.0",
    }
