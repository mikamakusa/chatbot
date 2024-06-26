import streamlit as st

st.title = "Chatbot"
page_1 = st.sidebar.page_link("pages/aws.py", label="AWS Powered Chatbot")
page_2 = st.sidebar.page_link("pages/azure.py", label="Azure Powered Chatbot")
page_3 = st.sidebar.page_link("pages/gcp.py", label="GCP Powered Chatbot")