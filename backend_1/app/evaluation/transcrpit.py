from youtube_transcript_api import YouTubeTranscriptApi
import re

def extract_video_id(url: str) -> str:
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(pattern, url)
    if not match:
        raise ValueError("Invalid YouTube URL")
    return match.group(1)

def get_transcript(url: str) -> str:
    video_id = extract_video_id(url)
    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    full_text = " ".join([item["text"] for item in transcript])
    return full_text
