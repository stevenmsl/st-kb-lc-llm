import streamlit as st
from langchain_openai import AzureChatOpenAI, AzureOpenAI
import config

st.title('🦜🔗 Quickstart App')

def generate_response(input_text):
    llm = AzureChatOpenAI(
        temperature=0.7,
        # openai_api_type='azure',
        # api_key='c94040b6f0fb4ff3bf84cda0c816b04f',
        # api_version='2023-07-01-preview',
        azure_deployment= config.AZURE_OPENAI_GPT4_DEPLOYMENT_NAME ,
        # azure_endpoint='https://slinopenai2.openai.azure.com/'
    )
    st.info(llm.invoke(input_text))

with st.form('my_form'):
    text = st.text_area(
        'Enter text:',
         'What are the three key pieces of advice for learning how to code?'
    )
    submitted = st.form_submit_button('Submit')
    generate_response(text)

