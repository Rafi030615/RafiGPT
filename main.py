import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from decouple import config

prompt = PromptTemplate(
    input_variables=["chat_history", "question"],
    template="""test"""
)

llm = ChatOpenAI(openai_api_key=config("OPENAI_API_KEY"))
memory = ConversationBufferWindowMemory(memory_key="chat_history", k=5)
llm_chain = LLMChain(
    llm=llm,
    memory=memory,
    prompt=prompt
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
        
user_prompt = st.chat_input()

if user_prompt is not None:
    st.session_state.messages.append({"role" : "assistant", "content" : "Hello there!"})
    with st.chat_message("user"):
        st.write(user_prompt)

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Loading...."):
            ai_response = llm_chain.predict(question=user_prompt)
            st.write(ai_response)
    new_ai_message = {"role" : "assistant", "content" : ai_response}
    st.session_state.messages.append(new_ai_message)
