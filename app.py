import io
import os
import requests
import pandas as pd
from celery import Celery
from celery.result import AsyncResult

import logging
import logging.config

from fastapi import (
    FastAPI,
    HTTPException,
    UploadFile,
    File,
)
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

logging.config.fileConfig(fname='logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

QUESTION_URL = "http://localhost:8000/api/questions"
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NCwiZW1haWwiOiJkdXkzQGdtYWlsLmNvbSIsImlzX2FkbWluIjp0cnVlLCJleHAiOjE3MzMxNzQ0MjZ9.9tbIkznmb9pcGmiY8_DL1N4aDFZi13iXfbhA1c77Ni4",
}

app = FastAPI(max_upload_size=100 * 1024 * 1024)
celery = Celery(
    __name__,
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

# Allow these methods to be used
methods = ["GET", "POST", "PUT", "DELETE"]
origin = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_credentials=True,
    allow_methods=methods,
    allow_headers=["*"]
)

@app.get("/tasks/{task_id}")
async def get_status(task_id):
    task_result = AsyncResult(task_id, app=celery)
    if task_result.failed():
        raise HTTPException(status_code=403, detail="Failed to execute task")
    
    result = {
        "task_id": task_id,
        "task_status": task_result.state,
        "task_result": task_result.result
    }
    return JSONResponse(result)

@app.post("/tasks/create_questions")
async def create_questions(csvFile: UploadFile = File(...)):
    contents = await csvFile.read()
    df = pd.read_csv(io.BytesIO(contents))
    filepath = "./tmp/tmp_file.csv"
    df.to_csv(filepath, index=False)
    task = task_create_questions.delay(filepath)
    return {
        "task_id": task.id
    }

@celery.task(name="create_questions")
def task_create_questions(filepath):
    send_file_headers = headers.copy()
    send_file_headers["Content-Type"] = "multipart/form-data"
    res = requests.post(url=QUESTION_URL+"/upload", headers=headers, files={'csvFile': open(filepath, 'rb')})
    os.remove(filepath)
    return res.json()