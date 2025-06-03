import json
import os

MEMORY_FILE = "memory_store.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {
            "goal": "",
            "level": "",
            "completed": [],
            "skipped": [],
            "preferences": []
        }
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

