import json
import os
import pandas as pd

RESULTS_FILE = "results.json"

def calculate_platelet_index(platelet_count):
    return min(10.0, (platelet_count - 150000) / 35000)

def injury_risk_level(score):
    if score >= 7:
        return "High"
    elif score >= 4:
        return "Moderate"
    else:
        return "Low"

def store_result(result):
    if os.path.exists(RESULTS_FILE):
        with open(RESULTS_FILE, 'r') as f:
            data = json.load(f)
    else:
        data = []
    data.append(result)
    with open(RESULTS_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def load_all_results():
    if os.path.exists(RESULTS_FILE):
        with open(RESULTS_FILE, 'r') as f:
            data = json.load(f)
            return pd.DataFrame(data)
    return None
