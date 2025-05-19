import os   
from dotenv import load_dotenv
import streamlit as st

from llm_models import LLMModels
from chat import Chat
from chat_history import ChatHistory
load_dotenv()
# llm_models = LLMModels()

# Inicializa o histórico do chat na session_state se não existir
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = ChatHistory()

list_of_models = ['llama-3.3-70b-versatile', 'gemma2-9b-it']
selected_model = st.sidebar.selectbox("Models", list_of_models)

chat = Chat(selected_model)
input_text = st.chat_input("Oi, como você está?")

if input_text:
    chat.completion(input_text)
    st.session_state.chat_history.add_user_message(input_text)
    st.session_state.chat_history.add_assistant_message(chat.get_content())

def draw_chat_history():
    for message in st.session_state.chat_history.get_history():
        if message['role'] == 'user':
            st.chat_message("user").markdown(message['content'])
        else:
            st.chat_message("assistant").markdown(message['content'])

draw_chat_history()




