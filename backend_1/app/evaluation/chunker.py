def chunk_transcript(transcript, seconds=300):
    chunks, current = [], []
    start = transcript[0]["start"]

    for item in transcript:
        if item["start"] - start <= seconds:
            current.append(item["text"])
        else:
            chunks.append(" ".join(current))
            current = [item["text"]]
            start = item["start"]

    chunks.append(" ".join(current))
    return chunks
