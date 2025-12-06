from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict
from fastapi.middleware.cors import CORSMiddleware
import numpy as np

app = FastAPI()

# Allow frontend (HTML/JS) to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for demo, allow all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory storage for demo (user -> template vector)
user_templates: Dict[str, List[float]] = {}

FIXED_PHRASE = "mysecurephrase"  # user must type this phrase


class Sample(BaseModel):
    username: str
    phrase: str
    intervals: List[float]  # time gaps between key presses in ms


def compare_patterns(template: List[float], sample: List[float]) -> float:
    """Return average absolute difference between two patterns."""
    template_arr = np.array(template)
    sample_arr = np.array(sample)

    # If lengths mismatch, truncate to shortest
    min_len = min(len(template_arr), len(sample_arr))
    template_arr = template_arr[:min_len]
    sample_arr = sample_arr[:min_len]

    diff = np.abs(template_arr - sample_arr)
    return float(diff.mean())


@app.get("/")
def root():
    return {"message": "Behavior-based auth backend running"}


@app.post("/register")
def register(sample: Sample):
    # Check phrase
    if sample.phrase.strip().lower() != FIXED_PHRASE:
        return {
            "success": False,
            "message": f"Please type the exact phrase: '{FIXED_PHRASE}'",
        }

    if len(sample.intervals) < 3:
        return {
            "success": False,
            "message": "Type a bit more normally so we get enough data.",
        }

    # For demo: just store this pattern as template
    user_templates[sample.username] = sample.intervals
    return {
        "success": True,
        "message": f"Template saved for user '{sample.username}'.",
        "interval_count": len(sample.intervals),
    }


@app.post("/verify")
def verify(sample: Sample):
    if sample.username not in user_templates:
        return {
            "success": False,
            "message": "User not registered. Please register first.",
        }

    if sample.phrase.strip().lower() != FIXED_PHRASE:
        return {
            "success": False,
            "message": f"Please type the exact phrase: '{FIXED_PHRASE}'",
        }

    template = user_templates[sample.username]

    distance = compare_patterns(template, sample.intervals)

    # Simple fixed threshold for demo (tune this value)
    THRESHOLD = 80.0  # milliseconds average difference

    is_genuine = distance <= THRESHOLD

    return {
        "success": True,
        "genuine_user": is_genuine,
        "distance": distance,
        "threshold": THRESHOLD,
        "message": "Access granted" if is_genuine else "Access denied (pattern mismatch)",
    }
