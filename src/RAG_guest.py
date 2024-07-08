from langchain.chat_models import ChatOpenAI
import openai
import streamlit as st
import os
from openai import OpenAI
from streamlit_chat import message
from dotenv import load_dotenv
load_dotenv()

def RAG_guest_bot(thread_id):
    col1,col2,col3 = st.columns((2,8,2))
    with col2:
        def conversation(user_input,thread_id):
            client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
            thread = client.beta.threads.create()
            message = client.beta.threads.messages.create(thread_id=thread_id,role="user",content=user_input)
            run = client.beta.threads.runs.create(thread_id=thread_id,assistant_id=os.environ["CALL_CENTER_CALLBOT_DOCUMENT"])
            # run = client.beta.threads.runs.create(thread_id=thread.id,assistant_id=assistant.id,run_id=run.id)
            
            while True:
                run = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run.id)
                if run.status=="completed":
                    messages = client.beta.threads.messages.list(thread_id=thread_id)
                    latest_message = messages.data[0]
                    text = latest_message.content[0].text.value
                    break
                
            return text
        ########################################### chatbot UI###############################################
        if 'historyy' not in st.session_state:
                st.session_state['historyy'] = []

        if 'generatedd' not in st.session_state:
            st.session_state['generatedd'] = ["Our website provides you with tailored information if you're a registered user?"]

        if 'pastt' not in st.session_state:
            st.session_state['pastt'] = ["We are delighted to have you here in the DeepSphere Live Agent Chat room!"]
            
        #container for the chat history
        response_container = st.container()
        #container for the user's text input
        container = st.container()
        with container:
            with st.form(key='my_form ', clear_on_submit=True):
                
                user_input = st.text_input("Prompt:", placeholder="How can I help you?", key='input ')
                submit_button = st.form_submit_button(label='Interact with LLM')
                
            if submit_button and user_input:
                vAR_response = conversation(user_input,thread_id)
                st.session_state['pastt'].append(user_input)
                st.session_state['generatedd'].append(str(vAR_response))

        if st.session_state['generatedd']:
                with response_container:
                    for i in range(len(st.session_state['generatedd'])):
                        message(st.session_state["pastt"][i], is_user=True, key=str(i) + '_user ', avatar_style="big-smile")
                        message(st.session_state["generatedd"][i], key=str(i), avatar_style="thumbs")