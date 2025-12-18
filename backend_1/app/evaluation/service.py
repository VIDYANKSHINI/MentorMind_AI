from app.evaluation.transcript import get_transcript
from app.evaluation.evaluator import evaluate_chunk

def chunk_text(text, size=800):
    for i in range(0, len(text), size):
        yield text[i:i+size]

def evaluate_youtube(url: str):
    transcript = get_transcript(url)
    scores = []

    for chunk in chunk_text(transcript):
        scores.append(evaluate_chunk(chunk))

    final = {
        k: round(sum(s[k] for s in scores) / len(scores), 2)
        for k in scores[0]
    }

    return final
