import json
import difflib

def load_data():
    with open("data/sem_data.json", "r") as file:
        return json.load(file)

def get_answer(data, semester, subject, user_question):
    try:
        subject_data = data[semester][subject]
        questions = list(subject_data.keys())

        print("User asked:", user_question)
        print("Available questions:", questions)

        # Lowercase everything for better matching
        match = difflib.get_close_matches(user_question.lower(), [q.lower() for q in questions], n=1, cutoff=0.5)

        if match:
            # Find original question text that matches lowercased version
            for q in questions:
                if q.lower() == match[0]:
                    matched_question = q
                    break
            return f"**Q: {matched_question}**\n\nA: {subject_data[matched_question]}"
        else:
            return "❌ Sorry, I couldn’t find a close enough answer. Try rephrasing."

    except Exception as e:
        return f"⚠️ Error: {str(e)}"
