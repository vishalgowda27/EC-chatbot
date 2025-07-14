import streamlit as st
from chatbot import load_data, get_answer

st.title("🤖 E&C Concepts Chatbot")
st.markdown("Ask questions from your E&C subjects! from Vishal Gowda ")

data = load_data()

sem = st.selectbox("Select Semester", list(data.keys()))
subject = st.selectbox("Select Subject", list(data[sem].keys()))
question = st.text_input("Enter your question")

if st.button("Ask"):
    answer = get_answer(data, sem, subject, question)
    st.success(answer) 

