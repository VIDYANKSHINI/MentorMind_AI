import hashlib

def stable_score(seed: str, low=45, high=95) -> int:
    h = hashlib.md5(seed.encode("utf-8")).hexdigest()
    value = int(h[:8], 16)
    return low + (value % (high - low))


def generate_scores(stable_id: str) -> dict:
    return {
        "clarity": stable_score(stable_id + "clarity"),
        "engagement": stable_score(stable_id + "engagement"),
        "pace": stable_score(stable_id + "pace"),
        "filler": stable_score(stable_id + "filler"),
        "technical": stable_score(stable_id + "technical"),
    }
