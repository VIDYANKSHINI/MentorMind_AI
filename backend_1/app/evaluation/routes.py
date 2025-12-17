from fastapi import APIRouter, Depends, HTTPException
from celery.result import AsyncResult
from core.security import get_current_user
from evaluation.tasks import evaluate_video_task

router = APIRouter(prefix="/evaluate", tags=["Evaluation"])

@router.post("/")
def submit(url: str, user=Depends(get_current_user)):
    task = evaluate_video_task.delay(url, user["id"])
    return {"job_id": task.id}

@router.get("/{job_id}")
def result(job_id: str, user=Depends(get_current_user)):
    task = AsyncResult(job_id)
    if not task.ready():
        return {"status": "processing"}
    if task.result["user_id"] != user["id"]:
        raise HTTPException(403, "Unauthorized")
    return task.result["result"]
