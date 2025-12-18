
from app.utils.youtube import extract_video_id
from app.evaluation.transcrpit import get_transcript
from app.evaluation.chunker import chunk_text
from app.evaluation.evaluator import evaluate_chunk
from app.evaluation.aggregator import aggregate_scores

async def evaluate_video_task(transcript: str):
    video_id = extract_video_id(url)
    transcript = get_transcript(video_id)
    chunks = chunk_text(transcript)

    scores = [evaluate_chunk(c) for c in chunks]
    result = aggregate_scores(scores)

    return {"user_id": user_id, "result": result}
