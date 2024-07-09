import streamlit as st
from PIL import Image
from src.guest_chatbot import guest_bot
from src.login import login_page
from src.RAG_guest import RAG_guest_bot
from src.transaction_guest_bot import Transaction_gusest_bot
from src.transaction_invoice import Transaction_invoice_download
import os
from openai import OpenAI
st.set_page_config(layout="wide")

# Adding (css)stye to application
with open('style/final.css') as f:
    st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

# Adding company logo
imcol1, imcol2, imcol3, imcol4 = st.columns((3.5,3,2.5,3.8))

with imcol2:
    st.write("## ")
    st.image('image/llmatscale-logo.png')
with imcol3:
    st.image('image/Call Center AI logo (1).png')   

st.markdown("<p style='text-align: center; color: black; font-size:25px; margin-top: -30px'><span style='font-weight: bold'></span>GENERATIVE AI Re-Invents Call Center Conversations</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: blue;margin-top: -10px ;font-size:20px;'><span style='font-weight: bold'></span>With a Large Language Model (LLM), customer experiences are significantly improved</p>", unsafe_allow_html=True)
st.markdown("<hr style=height:2.5px;margin-top:0px;width:100%;background-color:gray;>",unsafe_allow_html=True)

#---------Side bar-------#
with st.sidebar:
    st.markdown("<p style='text-align: center; color: white; font-size:25px;'><span style='font-weight: bold; font-family: century-gothic';></span>Solutions Scope</p>", unsafe_allow_html=True)
    vAR_AI_application = st.selectbox("",['Select Application','Conversational Interaction','Document-based Interaction','Transaction-based Interaction'],key='application')
    vAR_LLM_model = st.selectbox("",['LLM Models',"gpt-3.5-turbo-16k-0613","gpt-4-0314","gpt-3.5-turbo-16k","gpt-3.5-turbo-1106","gpt-4-0613","gpt-4-0314"],key='text_llmmodel')
    vAR_LLM_framework = st.selectbox("",['LLM Framework',"Langchain"],key='text_framework')

    vAR_Library = st.selectbox("",
                    ["Library Used","Streamlit","Image","Pandas","openAI"],key='text1')
    vAR_Gcp_cloud = st.selectbox("",
                    ["GCP Services Used","VM Instance","Computer Engine","Cloud Storage"],key='text2')
    st.markdown("#### ")
    href = """<form action="#">
            <input type="submit" value="Clear/Reset"/>
            </form>"""
    st.sidebar.markdown(href, unsafe_allow_html=True)
    st.markdown("# ")
    st.markdown("<p style='text-align: center; color: White; font-size:20px;'>Build & Deployed on<span style='font-weight: bold'></span></p>", unsafe_allow_html=True)
    s1,s2=st.columns((2,2))
    with s1:
        st.markdown("### ")
        st.image('image/aws_logo.png')
    with s2:    
        st.markdown("### ")
        st.image("image/oie_png.png")

# Function to create a new thread
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
def get_or_create_thread_id():
    if 'thread_id' not in st.session_state:
        thread = client.beta.threads.create()
        st.session_state.thread_id = thread.id
    return st.session_state.thread_id

# Call the function to get or create the thread_id when the app starts
thread_id = get_or_create_thread_id()

if vAR_AI_application == 'Conversational Interaction':
    
    tab1,tab2=st.tabs(["Guest","Registered user"])
    with tab1:
        guest_bot(thread_id)
    with tab2:
        login_page(thread_id,vAR_AI_application)
        
elif vAR_AI_application == 'Document-based Interaction':
    tab1,tab2=st.tabs(["Guest","Registered user"])
    with tab1:
        RAG_guest_bot(thread_id)
    with tab2:
        login_page(thread_id,vAR_AI_application)
        
elif vAR_AI_application == 'Transaction-based Interaction':
    tab1,tab2,tab3=st.tabs(["Guest","Registered user","Invoice download"])
    
    with tab1:
        Transaction_gusest_bot(thread_id)
    with tab2:
        login_page(thread_id,vAR_AI_application)
    with tab3:
        Transaction_invoice_download(thread_id)