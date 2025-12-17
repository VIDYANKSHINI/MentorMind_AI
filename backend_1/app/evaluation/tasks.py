from core.celery_app import celery_app
from utils.youtube import extract_video_id
from evaluation.transcript import get_transcript
from evaluation.chunker import chunk_transcript
from evaluation.evaluator import evaluate_chunk
from evaluation.aggregator import aggregate

@celery_app.task(bind=True, autoretry_for=(Exception,), retry_backoff=5)
def evaluate_video_task(self, url, user_id):
    video_id = extract_video_id(url)
    transcript = get_transcript(video_id)
    chunks = chunk_transcript(transcript)

    scores = [evaluate_chunk(c) for c in chunks]
    result = aggregate(scores)

    return {"user_id": user_id, "result": result}
