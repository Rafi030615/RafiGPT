import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from decouple import config

promt = PromptTemplate(
    input_variables=["chat_history"]
)

st.set_page_config(
    page_title="RafiGPT-1.0",
    layout="wide"
)

st.title("RafiGPT-1.0")

if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {"role" : "assistant", "content" : "Hello there!"}
        ]
    
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])