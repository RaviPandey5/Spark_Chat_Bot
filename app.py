import os

import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai


load_dotenv()

st.set_page_config(
    page_title="Chat with Gemini-Pro!",
    page_icon=":dizzy:",  # Favicon emoji
    layout="centered",  # Page layout option
)
css = """
<style>
.title {
    font-size: 48px;
    color: #4F8BF9;
    text-align: center;
}
</style>
"""
st.markdown(css, unsafe_allow_html=True)
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')



def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role

if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

st.markdown('<h1 class="title">🧙 Spark Pro - ChatBot</h1>', unsafe_allow_html=True)


for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# Input field for user's message
user_prompt = st.chat_input("Ask Spark-Pro...")

if user_prompt:

    st.chat_message("user").markdown(user_prompt)

    gemini_response = st.session_state.chat_session.send_message(user_prompt)


    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)

