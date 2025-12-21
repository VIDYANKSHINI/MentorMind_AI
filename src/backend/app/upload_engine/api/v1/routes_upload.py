# backend/app/api/v1/routes_upload.py
from fastapi import APIRouter, File, UploadFile, HTTPException, Form
from uuid import uuid4
import os
import shutil

from app.upload_engine.services.job_queue import enqueue_accessibility_job
from app.upload_engine.db.sessions_store import create_session
from app.upload_engine.services.video_scoring import compute_scores,compute_overall
from app.upload_engine.services.video_scoring import extract_features
from app.upload_engine.services.mode_blind import video_to_description
from app.upload_engine.services.mode_deaf import process_deaf_mode
from app.upload_engine.services.mode_easy import generate_easy_audio
from app.upload_engine.services.video_proccessor import save_upload_file
from app.upload_engine.utils.file_utils import save_upload_file
from app.youtube_engine.evaluation.service import process_youtube_url
import hashlib
from app.common.deterministic_score import generate_scores

from typing import Optional


router = APIRouter()

UPLOAD_DIR = "/mnt/data/uploads"   # dev local path
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/convert")
async def convert_accessibility_mode(file: UploadFile, mode: str):
    file_path = save_upload_file(file)

    if mode == "blind":
        output_path = video_to_description(file_path)

    elif mode == "deaf":
        output_path = process_deaf_mode(file_path)

    elif mode == "easy":
        output_path = generate_easy_audio(file_path)

    else:
        raise HTTPException(status_code=400, detail="Invalid mode")

    return {"output_video": output_path}


def file_hash(file_bytes: bytes) -> str:
    return hashlib.md5(file_bytes).hexdigest()


@router.post("/upload-video")
async def upload_video(
    video: UploadFile = File(None),
    video_url: str = Form(None),
):
    if video_url:
        from app.youtube_engine.evaluation.service import process_youtube_url
        return process_youtube_url(video_url)

    file_bytes = await video.read()
    stable_id = file_hash(file_bytes)

    scores = generate_scores(stable_id)

    overall = round(
        scores["clarity"] * 0.25 +
        scores["engagement"] * 0.25 +
        scores["pace"] * 0.15 +
        scores["filler"] * 0.15 +
        scores["technical"] * 0.20,
        2
    )

    return {
        "scores": scores,
        "overall_score": overall,
        "chunks_evaluated": 1
    }

    # Create simple session record
    create_session(session_id, mentor_id, save_path)

    # enqueue the background job
    job_id = enqueue_accessibility_job.delay(save_path, session_id, mentor_id).id

    return {"session_id": session_id, "job_id": job_id, "status": "queued", "file_path": save_path}
