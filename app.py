import streamlit as st
import openai

first_message = st.chat_input("Hi! How may I help you?", accept_file=True, file_type=None)

intro_msg = "Hello and Welcome to COARE!"

if st.button("Press this button"):
    st.write(intro_msg)

if first_message and first_message.text:
    st.markdown(first_message.text)

if first_message and first_message["files"]:
    st.image(first_message["files"][0])

with st.chat_message("user"):
    st.write("Hello stranger!")