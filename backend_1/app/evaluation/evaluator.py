import os
from openai import OpenAI

def get_openai_client():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not set")
    return OpenAI(api_key=api_key)

def evaluate_chunk(text: str) -> dict:
    client = get_openai_client()

    prompt = f"""
You are an expert communication evaluator.

Score the transcript chunk on a scale of 0–10:
- clarity
- engagement
- pace
- filler_words
- technical_depth
- overall

Transcript:
{text}

Respond ONLY with valid JSON.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return eval(response.choices[0].message.content)
