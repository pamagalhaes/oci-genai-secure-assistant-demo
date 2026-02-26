import json
import time
from pathlib import Path

LOG_PATH = Path("logs.jsonl")  # um JSON por linha

def log_event(event: dict):
    event["ts"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, ensure_ascii=False) + "\n")
