from app.common.deterministic_score import generate_scores


def evaluate_full_transcript(transcript: str) -> dict:
    # transcript itself becomes stable identity
    scores = generate_scores(transcript)

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


def process_youtube_url(url: str) -> dict:
    # URL is the stable identity
    return evaluate_full_transcript(url)
