from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from fastapi.security import OAuth2PasswordRequestForm
import uuid

from app.core.security import (
    authenticate_user,
    create_access_token,
    get_current_user
)
from app.evaluation.schemas import EvaluationRequest
from app.evaluation.tasks import evaluate_video_task

# -------------------------------
# Routers (SEPARATE!)
# -------------------------------
auth_router = APIRouter(prefix="/auth", tags=["Auth"])
eval_router = APIRouter(prefix="/evaluate", tags=["Evaluation"])

# -------------------------------
# In-memory job store (demo only)
# -------------------------------
JOB_STORE = {}

# ===============================
# AUTH
# ===============================
@auth_router.post("/login")
def login(form: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form.username, form.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user["username"]})
    return {
        "access_token": token,
        "token_type": "bearer"
    }

# ===============================
# EVALUATION
# ===============================
@eval_router.post("/")
def evaluate(
    data: EvaluationRequest,
    background_tasks: BackgroundTasks,
    user=Depends(get_current_user)
):
    job_id = str(uuid.uuid4())

    JOB_STORE[job_id] = {
        "status": "processing",
        "user_id": user["id"],
        "result": None
    }

    background_tasks.add_task(
        evaluate_video_task,
        data.youtube_url,
        user["id"],
        job_id,
        JOB_STORE
    )

    return {
        "job_id": job_id,
        "status": "submitted"
    }

@eval_router.get("/{job_id}")
def get_result(job_id: str, user=Depends(get_current_user)):
    job = JOB_STORE.get(job_id)

    if not job:
        raise HTTPException(404, "Job not found")

    if job["user_id"] != user["id"]:
        raise HTTPException(403, "Unauthorized")

    return job
