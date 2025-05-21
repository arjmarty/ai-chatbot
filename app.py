import streamlit as st
import os
from openai import OpenAI


# Set OpenAI API key
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

#set a default model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

#Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

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