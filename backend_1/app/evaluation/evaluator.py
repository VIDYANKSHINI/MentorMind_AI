from openai import OpenAI
from core.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def evaluate_chunk(text):
    prompt = f"""
Score this lecture chunk (0-10):
clarity, engagement, pace, filler, tech.
Return JSON only.
{text}
"""
    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    return eval(res.choices[0].message.content)
