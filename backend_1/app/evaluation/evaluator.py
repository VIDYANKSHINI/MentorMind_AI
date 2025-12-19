import json
from openai import OpenAI

client = OpenAI()

SYSTEM_PROMPT = """
You are an expert teaching quality evaluator.
Return ONLY valid JSON. No markdown. No explanations.
"""

def evaluate_transcript(transcript: str) -> dict:
    response = client.responses.create(
        model="gpt-4.1-mini",
        response_format={"type": "json"},
        input=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": f"""
Evaluate this lecture on:
clarity, engagement, tone, pacing, content_delivery.

Return EXACT JSON:
{{
  "clarity": {{ "score": 0-10, "reason": "" }},
  "engagement": {{ "score": 0-10, "reason": "" }},
  "tone": {{ "score": 0-10, "reason": "" }},
  "pacing": {{ "score": 0-10, "reason": "" }},
  "content_delivery": {{ "score": 0-10, "reason": "" }},
  "overall_score": 0-10
}}

Transcript:
{transcript}
"""
            }
        ]
    )

    return json.loads(response.output_text)
