import openai
import streamlit as st
from openai import OpenAI
from streamlit_chat import message
import os
from dotenv import load_dotenv
load_dotenv()

def Transaction_chat_bot(email,username,thread_id):
    if 'history' not in st.session_state:
        st.session_state['history'] = []

    if 'generated' not in st.session_state:
        st.session_state['generated'] = ["Greetings! Thank you for the transaction you made last week. \n Are you contacting us about your last transaction?"]

    if 'past' not in st.session_state:
        st.session_state['past'] = ["We are delighted to have you here in the DeepSphere Live Agent Chat room!"]
    
    col1,col2,col3 = st.columns((2,8,2))
    with col2:
        user_input = f'my Name:{username} and Email id:{email}'
        if user_input == f'my Name:{username} and Email id:{email}':
            client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
            message_1 = client.beta.threads.messages.create(thread_id=thread_id,role="user",content=user_input)
            run = client.beta.threads.runs.create(thread_id=thread_id,assistant_id=os.environ["CALL_CENTER_CALLBOT_TRANSACTION_REGISTER"])
            # run = client.beta.threads.runs.create(thread_id=thread.id,assistant_id=assistant.id,run_id=run.id)
            
            while True:
                run = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run.id)
                if run.status=="completed":
                    messages = client.beta.threads.messages.list(thread_id=thread_id)
                    latest_message = messages.data[0]
                    text = latest_message.content[0].text.value
                    break
        
        def conversation(user_input,thread_id):
            client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
            message_1 = client.beta.threads.messages.create(thread_id=thread_id,role="user",content=user_input)
            run = client.beta.threads.runs.create(thread_id=thread_id,assistant_id=os.environ["CALL_CENTER_CALLBOT_TRANSACTION_REGISTER"])
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
        #container for the chat history
        response_container = st.container()
        
        #container for the user's text input
        container = st.container()
        with container:
            with st.form(key='my_form', clear_on_submit=True):
                
                user_input = st.text_input("Prompt:", placeholder="How can I help you?", key='input')
                submit_button = st.form_submit_button(label='Interact with LLM')
                
            if submit_button and user_input:
                
                # messages_history.append(HumanMessage(content=user_input))
                vAR_response = conversation(user_input,thread_id)
                
                st.session_state['past'].append(user_input)
                st.session_state['generated'].append(vAR_response)

        if st.session_state['generated']:
            with response_container:
                for i in range(len(st.session_state['generated'])):
                    message(st.session_state["past"][i], is_user=True, key=str(i) + '_user', avatar_style="big-smile")
                    message(st.session_state["generated"][i], key=str(i+55), avatar_style="thumbs")