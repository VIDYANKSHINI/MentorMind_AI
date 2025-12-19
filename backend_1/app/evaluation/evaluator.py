import os
from openai import OpenAI
from youtube_transcript_api import YouTubeTranscriptApi

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_video_id(url) -> str:
    url = str(url)   # 🔥 FIX

    if "v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    else:
        raise ValueError("Invalid YouTube URL")



def get_transcript(youtube_url) -> str:
    video_id = get_video_id(youtube_url)
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    return " ".join(t["text"] for t in transcript)


def evaluate_transcript(transcript: str) -> dict:
    prompt = f"""
You are an expert education evaluator.

Rate the teacher based on:
- clarity
- engagement
- tone
- pacing
- content delivery

Give scores from 1 to 10.
Return STRICT JSON only.

Transcript:
{transcript}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You return only valid JSON."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return eval(response.choices[0].message.content)
