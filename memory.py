import json
import os

MEMORY_FILE = "memory.json"

MAX_MESSAGES = 10  # Keep last 20 messages


def load_memory():

    if not os.path.exists(MEMORY_FILE):
        return []

    with open(MEMORY_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def save_memory(messages):

    # Limit memory size
    if len(messages) > MAX_MESSAGES:
        messages = messages[-MAX_MESSAGES:]

    with open(MEMORY_FILE, "w") as file:
        json.dump(messages, file, indent=4)