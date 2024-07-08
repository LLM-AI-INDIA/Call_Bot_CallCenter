import streamlit as st
from src.chatbot import chat_bot
from src.user_crend import user_details_cred
from src.RAG_Regiter import RAG_register_bot
from src.transaction_register_bot import Transaction_chat_bot
from src.user_cred_for_transaction import users_cred_for_transaction

def login_page(thread_id,vAR_AI_application):
    col1,col2,col3 = st.columns((2,8,2))
    with col2:
        st.write("# ")
        st.write("# ")
        placeholder = st.empty()
        
    if vAR_AI_application == 'Transaction-based Interaction':
        user_details = users_cred_for_transaction()
    else:
        user_details = user_details_cred()
    
    # Insert a form in the container
    with placeholder.form("login"):
        st.markdown("<p style='text-align: center; color: black; font-size:25px;'><span style='font-weight: bold'>Enter your credentials</span></p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: left; color: black; margin-bottom: -155px; font-size:20px;'><span style='font-weight: bold'>Email</span></p>", unsafe_allow_html=True)
        email = st.text_input("")
        st.markdown("<p style='text-align: left; color: black; margin-top: 0px; margin-bottom: -155px; font-size:20px;'><span style='font-weight: bold'>Password</span></p>", unsafe_allow_html=True)
        username = st.text_input("", type="password")
        submit = st.form_submit_button("Login")
        # guest = st.form_submit_button("Guest")

    # if submit and email == actual_email and password == actual_password:
        # If the form is submitted and the email and password are correct,
        # clear the form/container and display a success message
            
    user_enter = {email , username}
    
    if user_enter in user_details:
        placeholder.empty()
        if vAR_AI_application == 'Conversational Interaction':
            chat_bot(email,username,thread_id)
        elif vAR_AI_application == 'Document-based Interaction':
            RAG_register_bot(email,username,thread_id)
        elif vAR_AI_application == 'Transaction-based Interaction':
            Transaction_chat_bot(email,username,thread_id)
    elif submit:
        st.error("Invalid email or password")
        
        