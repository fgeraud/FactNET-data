import json
import os

def load_dataset():
    data = []
    files = os.listdir("data")
    for file in files:
        with open(f"data/{file}", "r") as f:
            data.append(json.loads(f.readlines()[0]))
    return data