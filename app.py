import streamlit as st

first_message = st.chat_input("Hi! How may I help you?", accept_file=True, file_type=None)

if first_message and first_message.text:
    st.markdown(first_message.text)