import hashlib
import random
import time
from typing import Dict, Optional

# In-memory results store (demo only)
RESULTS_STORE: Dict[str, dict] = {}


def _stable_random(seed: str, low: int = 60, high: int = 95) -> int:
    """
    Generates deterministic-but-variable values.
    Same source → same result
    Different source → different result
    """
    h = hashlib.md5(seed.encode("utf-8")).hexdigest()
    random.seed(int(h[:8], 16))
    return random.randint(low, high)


def generate_demo_scores(source: str) -> Dict[str, int]:
    return {
        "clarity": _stable_random(source + "clarity"),
        "engagement": _stable_random(source + "engagement"),
        "tone": _stable_random(source + "tone"),
        "pacing": _stable_random(source + "pacing"),
        "content_delivery": _stable_random(source + "content"),
    }


def store_result(job_id: str, source: str) -> None:
    """
    Used by:
    - upload engine (video upload demo mode)
    """
    scores = generate_demo_scores(source)

    RESULTS_STORE[job_id] = {
        "scores": scores,
        "overall_score": round(sum(scores.values()) / len(scores), 2),
        "generated_at": time.time(),
        "source": source,
        "mode": "demo"
    }


# 🔹 NEW (used internally, does NOT change existing API)
def store_computed_result(job_id: str, scores: Dict[str, float], meta: dict = None) -> None:
    """
    Used by:
    - YouTube engine
    - Real ML scoring
    """
    RESULTS_STORE[job_id] = {
        "scores": scores,
        "overall_score": round(sum(scores.values()) / len(scores), 2),
        "generated_at": time.time(),
        "mode": "computed",
        "meta": meta or {}
    }


def get_result(job_id: str) -> Optional[dict]:
    return RESULTS_STORE.get(job_id)
