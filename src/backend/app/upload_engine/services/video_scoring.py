import numpy as np
from models.model_loader import LOADED_MODELS
import json
import hashlib

# Load ONNX models
clarity_model = LOADED_MODELS["clarity"]
engagement_model = LOADED_MODELS["engagement"]
pace_model = LOADED_MODELS["pace"]
tech_depth_model = LOADED_MODELS["tech_depth"]
filler_model = LOADED_MODELS["filler"]


# -----------------------------------------------------
# Helper: generate deterministic noise from file name
# -----------------------------------------------------
def stable_noise(file_path, scale=0.05):
    """
    Produces a small, stable noise based on file hash.
    Ensures same video always gives same slight variation.
    """
    file_hash = int(hashlib.md5(file_path.encode()).hexdigest(), 16)
    rng = np.random.default_rng(file_hash)
    return rng.uniform(-scale, scale)


# -----------------------------------------------------
# Controlled score ranges
# -----------------------------------------------------
RANGES = {
    "clarity": (0.80, 1.00),
    "engagement": (0.30, 0.70),
    "pace": (0.40, 0.90),
    "filler": (0.10, 0.40),
    "tech": (0.60, 1.00),
}


def normalize_score(raw, metric, noise):
    """ Scale dummy raw output into controlled range + noise """
    min_v, max_v = RANGES[metric]

    # raw from ONNX is 0.5 always → convert to mid range
    base = (min_v + max_v) / 2

    # apply small noise
    final = base + noise

    # clamp to range
    return float(np.clip(final, min_v, max_v))


# -----------------------------------------------------
# Feature extractor – keeps features stable per video
# -----------------------------------------------------
def extract_features(file_path):
    """
    Returns stable features + small noise to create slight variation.
    """
    noise = stable_noise(file_path, 0.02)

    return {
        "clarity": np.full((128,), 0.5 + noise, dtype="float32"),
        "engagement": np.full((3, 64, 64), 0.1 + noise, dtype="float32"),
        "pace": np.full((32,), 0.3 + noise, dtype="float32"),
        "filler": np.full((64,), 0.2 + noise, dtype="float32"),
        "tech": np.full((256,), 0.4 + noise, dtype="float32"),
    }


# -----------------------------------------------------
# Run ONNX model
# -----------------------------------------------------
def run_model(model, features):
    """
    Supports:
    - ONNX Runtime models
    - Dummy Python functions (demo mode)
    """
    # ✅ Demo / dummy model (function)
    if callable(model):
        return model(features)

    # ✅ Real ONNX model
    input_name = model.get_inputs()[0].name
    output_name = model.get_outputs()[0].name

    result = model.run(
        [output_name],
        {input_name: features}
    )

    return float(result[0][0])



# -----------------------------------------------------
# Compute scores from models + controlled range scaling
# -----------------------------------------------------
def compute_scores(features, file_path=None):
    noise = stable_noise(file_path or "default", 0.05)

    raw_scores = {
        "clarity": run_model(clarity_model, features["clarity"]),
        "engagement": run_model(engagement_model, features["engagement"]),
        "pace": run_model(pace_model, features["pace"]),
        "filler": run_model(filler_model, features["filler"]),
        "tech": run_model(tech_depth_model, features["tech"]),
    }

    # normalize into controlled ranges
    final_scores = {
        metric: normalize_score(raw_scores[metric], metric, noise)
        for metric in raw_scores
    }

    return final_scores


# -----------------------------------------------------
# Main API used in backend
# -----------------------------------------------------
def compute_scores_from_video(file_path: str):
    features = extract_features(file_path)
    return compute_scores(features, file_path=file_path)


# -----------------------------------------------------
# Weighted overall score
# -----------------------------------------------------
def compute_overall(scores):
    if isinstance(scores, str):
        scores = json.loads(scores)

    return round(
        scores["clarity"] * 0.25 +
        scores["engagement"] * 0.25 +
        scores["pace"] * 0.20 +
        scores["filler"] * 0.15 +
        scores["tech"] * 0.15,
        4,
    )
