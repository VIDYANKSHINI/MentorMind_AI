import os
from openai import OpenAI

client = OpenAI()

def evaluate_chunk(text: str) -> dict:
    client = OpenAI()

    prompt = f"""
You are an expert communication evaluator.

Evaluate the following transcript chunk and give scores from 0–10.

Scoring rules:
- clarity: how understandable and structured the speech is
- engagement: how engaging and interesting the speaker is
- pace: speaking speed (too fast/slow reduces score)
- filler: score HIGH if FEW filler words are used
- technical: depth and correctness of technical content

Return ONLY valid JSON in this format:

{
  "clarity": number,
  "engagement": number,
  "pace": number,
  "filler": number,
  "technical": number
}

Transcript:
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return eval(response.choices[0].message.content)
