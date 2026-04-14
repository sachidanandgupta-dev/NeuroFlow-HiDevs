import re
import json
from uuid import UUID

def validate_pair(pair: dict):
    # Validation rules from screenshot
    content = pair["messages"][2]["content"]
    # 1. Length 50-2000 tokens
    if not (50 <= len(content.split()) <= 2000): return False
    # 2. Must contain citation
    if not re.search(r"\[Source \d+\]", content): return False
    # 3. No PII (Email/Phone)
    if re.search(r"[\w\.-]+@[\w\.-]+\.\w+", content): return False
    return True

def export_training_data(job_id: UUID, pairs: list):
    valid_pairs = [p for p in pairs if validate_pair(p)]
    path = f"training_data/{job_id}.jsonl"
    with open(path, "w") as f:
        for p in valid_pairs:
            f.write(json.dumps(p) + "\n")
    return path