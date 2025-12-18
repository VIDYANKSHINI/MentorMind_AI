
from app.evaluation.service import evaluate_full_transcript
from app.evaluation.transcrpit import get_transcript

def evaluate_video_task(youtube_url: str, user_id: str, job_id: str, store: dict):
    try:
        transcript = get_transcript(youtube_url)

        result = evaluate_full_transcript(transcript)

        store[job_id]["status"] = "completed"
        store[job_id]["result"] = result

    except Exception as e:
        store[job_id]["status"] = "failed"
        store[job_id]["result"] = str(e)
