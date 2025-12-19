import re
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import NoTranscriptFound

def get_video_id(url: str) -> str:
    match = re.search(r"(?:v=|youtu\.be/)([a-zA-Z0-9_-]{11})", url)
    if not match:
        raise ValueError("Invalid YouTube URL")
    return match.group(1)

def fetch_transcript(youtube_url: str) -> str:
    youtube_url = str(youtube_url)
    video_id = get_video_id(youtube_url)

    try:
        # 1️⃣ Try English first
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=["en"])
    except NoTranscriptFound:
        try:
            # 2️⃣ Try Hindi auto-generated
            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=["hi"])
        except NoTranscriptFound:
            # 3️⃣ Fallback: auto-select & translate to English
            transcript = (
                YouTubeTranscriptApi
                .list_transcripts(video_id)
                .find_transcript(["hi"])
                .translate("en")
                .fetch()
            )

    return " ".join(item["text"] for item in transcript)
