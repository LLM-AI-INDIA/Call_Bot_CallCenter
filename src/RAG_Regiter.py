import openai
import streamlit as st
from openai import OpenAI
from streamlit_chat import message
import os
from dotenv import load_dotenv
load_dotenv()

def RAG_register_bot(email,username,thread_id):
    col1,col2,col3,col4 = st.columns((2,2.5,3.5,2))
    col11,col22,col33 = st.columns((2,8,2))
    
    with col2:
        st.write('### ')
        st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Model Input Type</span></p>", unsafe_allow_html=True)
    with col3:
        vAR_input_type = st.radio(" ",['File Input', 'URL Input'],horizontal=True)
    
    if vAR_input_type == 'File Input':
        with col2:
            st.write('## ') 
            st.write('### ') 
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Model Input File</span></p>", unsafe_allow_html=True)
        with col3:   
            vAR_file = st.file_uploader(" ", type='pdf')    
        
        if vAR_file:
            with col22:
                st.write("# ")
                user_input = f'My Name:{username} and Email id:{email}'
                
                if user_input == f'My Name:{username} and Email id:{email}':
                    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
                    message_1 = client.beta.threads.messages.create(thread_id=thread_id,role="user",content=user_input)
                    run = client.beta.threads.runs.create_and_poll(thread_id=thread_id,assistant_id=os.environ["CALL_CENTER_CALLBOT_DOCUMENT"])
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
                    run = client.beta.threads.runs.create_and_poll(thread_id=thread_id,assistant_id=os.environ["CALL_CENTER_CALLBOT_DOCUMENT"])
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
                if 'history' not in st.session_state:
                        st.session_state['history'] = []

                if 'generated' not in st.session_state:
                    st.session_state['generated'] = ["Greetings! "+ username+"! Thank you for the transaction you\nmade last week. Are you contacting us about your last purchase?"]

                if 'past' not in st.session_state:
                    st.session_state['past'] = ["We are delighted to have you here in the DeepSphere Live Agent Chat room!"]
                

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

                        # if 'Rephrase:' in vAR_response.content:
                        #     vAR_final_response = pandas_bot(user_input,username)
                        #     # messages_history.append(AIMessage(content=str(vAR_final_response)))
                            
                        # else:
                        #     # messages_history.append(AIMessage(content=str(vAR_response.content)))
                        #     vAR_final_response = vAR_response.content
                        
                        st.session_state['past'].append(user_input)
                        st.session_state['generated'].append(vAR_response)

                if st.session_state['generated']:
                    with response_container:
                        for i in range(len(st.session_state['generated'])):
                            message(st.session_state["past"][i], is_user=True, key=str(i) + '_user', avatar_style="big-smile")
                            message(st.session_state["generated"][i], key=str(i+55), avatar_style="thumbs")
    
    elif vAR_input_type == 'URL Input':
        with col2:
            st.write("## ")
            st.markdown("<p style='text-align: left; color: black; font-size:20px;'><span style='font-weight: bold'>Model Input URL</span></p>", unsafe_allow_html=True)
        with col3:    
            vAR_URL = st.text_input(" ")                        
        
        if vAR_URL:
            with col22:
                st.write("# ")
                user_input = f'My Name:{username} and Email id:{email}'
                
                if user_input == f'My Name:{username} and Email id:{email}':
                    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
                    message_1 = client.beta.threads.messages.create(thread_id=thread_id,role="user",content=user_input)
                    run = client.beta.threads.runs.create_and_poll(thread_id=thread_id,assistant_id=os.environ["CALL_CENTER_CALLBOT_DOCUMENT"])
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
                    run = client.beta.threads.runs.create_and_poll(thread_id=thread_id,assistant_id=os.environ["CALL_CENTER_CALLBOT_DOCUMENT"])
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
                if 'history' not in st.session_state:
                        st.session_state['history'] = []

                if 'generated' not in st.session_state:
                    st.session_state['generated'] = ["Greetings! "+ username+"! Thank you for the transaction you\nmade last week. Are you contacting us about your last purchase?"]

                if 'past' not in st.session_state:
                    st.session_state['past'] = ["We are delighted to have you here in the DeepSphere Live Agent Chat room!"]
                

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

                        # if 'Rephrase:' in vAR_response.content:
                        #     vAR_final_response = pandas_bot(user_input,username)
                        #     # messages_history.append(AIMessage(content=str(vAR_final_response)))
                            
                        # else:
                        #     # messages_history.append(AIMessage(content=str(vAR_response.content)))
                        #     vAR_final_response = vAR_response.content
                        
                        st.session_state['past'].append(user_input)
                        st.session_state['generated'].append(vAR_response)

                if st.session_state['generated']:
                        with response_container:
                            for i in range(len(st.session_state['generated'])):
                                message(st.session_state["past"][i], is_user=True, key=str(i) + '_user', avatar_style="big-smile")
                                message(st.session_state["generated"][i], key=str(i+55), avatar_style="thumbs")
                    
                    