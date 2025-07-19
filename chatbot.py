import json
from fuzzywuzzy import fuzz

def load_data():
    with open("data.json", "r") as f:
        return json.load(f)

def get_answer(data, sem, subject, question):
    best_score = 0
    best_answer = "Sorry, I couldn’t find an answer."
    for q, a in data[sem][subject].items():
        score = fuzz.ratio(q.lower(), question.lower())
        if score > best_score:
            best_score = score
            best_answer = a
    return best_answer
