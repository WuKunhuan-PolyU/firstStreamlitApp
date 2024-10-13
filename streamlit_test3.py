import streamlit as st
import json

def save_history(history):
    with open('history.json', 'w') as f:
        json.dump(history, f)
def load_history():
    try:
        with open('history.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
if 'text_history' not in st.session_state:
    st.session_state.text_history = load_history()

text_input = st.text_input("Enter some text:")
submit_button = st.button("Submit")
if submit_button:
    st.session_state.text_history.append(text_input)
    save_history(st.session_state.text_history)
    st.write("You've inputted:", text_input)
    st.session_state.input_box = ""
clear_button = st.button("Clear History")
if clear_button:
    st.session_state.text_history = []
    save_history(st.session_state.text_history)

st.write("## Past inputs")
for text in st.session_state.text_history:
    st.write(text)
