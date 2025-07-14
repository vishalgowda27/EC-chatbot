import json

def load_data():
    with open("data/sem_data.json", "r") as f:
        return json.load(f)

def get_answer(data, sem, subject, user_question):
    try:
        subject_data = data[sem][subject]
        for q, a in subject_data.items():
            if user_question.lower() in q.lower():
                return a
        return "Sorry, I don't have an answer for that yet."
    except KeyError:
        return "Invalid selection. Please check semester/subject."
