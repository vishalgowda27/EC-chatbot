import gradio as gr
from chatbot import load_data, get_answer

data = load_data()

def chatbot_interface(sem, subject, question):
    return get_answer(data, sem, subject, question)

semesters = list(data.keys())
subjects_per_sem = {sem: list(data[sem].keys()) for sem in semesters}

def update_subjects(sem):
    return gr.Dropdown.update(choices=subjects_per_sem[sem])

with gr.Blocks() as demo:
    gr.Markdown("## 🤖 E&C Concepts Chatbot\nAsk questions from your E&C subjects! from Vishal Gowda")
    
    sem_dropdown = gr.Dropdown(choices=semesters, label="Select Semester")
    subject_dropdown = gr.Dropdown(choices=subjects_per_sem[semesters[0]], label="Select Subject")
    question_box = gr.Textbox(label="Enter your question")
    answer_box = gr.Textbox(label="Answer", interactive=False)
    
    sem_dropdown.change(fn=update_subjects, inputs=sem_dropdown, outputs=subject_dropdown)
    submit_btn = gr.Button("Ask")
    submit_btn.click(fn=chatbot_interface, inputs=[sem_dropdown, subject_dropdown, question_box], outputs=answer_box)

demo.launch()
