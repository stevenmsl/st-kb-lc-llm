import toml  
import os  
import streamlit as st  

# The package loadenv was previously used to manage environment variables. However, Streamlit only accepts TOML files for   
# managing secrets in a secure manner. Therefore, the loadenv package was dropped in favor of using a TOML file.   
# The TOML file is either read directly if the "st.secrets" object is not populated (i.e., in a local environment),   
# or the environment variables are populated from the "st.secrets" object (i.e., in a Streamlit sharing environment).   
# This way, we ensure compatibility with Streamlit's secrets management and allow for secure handling of sensitive data   
# in different environments.

# The secrets.toml file must be positioned within the .streamlit directory.

if st.secrets:  
    os.environ["OPENAI_API_KEY"] = st.secrets["openai"]["api_key"]  
    os.environ["OPENAI_API_TYPE"] = st.secrets["openai"]["api_type"]  
    os.environ["OPENAI_API_VERSION"] = st.secrets["openai"]["api_version"]  
    os.environ["AZURE_OPENAI_DEFAULT_DEPLOYMENT_NAME"] = st.secrets["azure_openai"]["default_deployment_name"]  
    os.environ["AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME"] = st.secrets["azure_openai"]["embedding_deployment_name"]  
    os.environ["AZURE_OPENAI_ENDPOINT"] = st.secrets["azure_openai"]["endpoint"]  
    os.environ["AZURE_OPENAI_GPT35TURBO_DEPLOYMENT_NAME"] = st.secrets["azure_openai"]["gpt35turbo_deployment_name"]  
    os.environ["AZURE_OPENAI_GPT4_DEPLOYMENT_NAME"] = st.secrets["azure_openai"]["gpt4_deployment_name"]  
    os.environ["PYTHONIOENCODING"] = st.secrets["other"]["pythonioencoding"]  
else:  
    secrets = toml.load("./secrets.toml")  
    os.environ["OPENAI_API_KEY"] = secrets["openai"]["api_key"]  
    os.environ["OPENAI_API_TYPE"] = secrets["openai"]["api_type"]  
    os.environ["OPENAI_API_VERSION"] = secrets["openai"]["api_version"]  
    os.environ["AZURE_OPENAI_DEFAULT_DEPLOYMENT_NAME"] = secrets["azure_openai"]["default_deployment_name"]  
    os.environ["AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME"] = secrets["azure_openai"]["embedding_deployment_name"]  
    os.environ["AZURE_OPENAI_ENDPOINT"] = secrets["azure_openai"]["endpoint"]  
    os.environ["AZURE_OPENAI_GPT35TURBO_DEPLOYMENT_NAME"] = secrets["azure_openai"]["gpt35turbo_deployment_name"]  
    os.environ["AZURE_OPENAI_GPT4_DEPLOYMENT_NAME"] = secrets["azure_openai"]["gpt4_deployment_name"]  
    os.environ["PYTHONIOENCODING"] = secrets["other"]["pythonioencoding"] 

AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_GPT4_DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_GPT4_DEPLOYMENT_NAME")
AZURE_OPENAI_GPT35TURBO_DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_GPT35TURBO_DEPLOYMENT_NAME")
AZURE_OPENAI_DEFAULT_DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEFAULT_DEPLOYMENT_NAME")
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME")
OPENAI_API_TYPE = os.getenv("OPENAI_API_TYPE")
OPENAI_API_VERSION = os.getenv("OPENAI_API_VERSION")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") 
