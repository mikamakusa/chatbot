import streamlit as st
import google.generativeai as genai


st.title = "Google Cloud Platform Chatbot Powered"

st.sidebar.header('Google Cloud Platform Credentials')
uplodaded_file = st.sidebar.file_uploader("Credentials file : ")
if uplodaded_file is not None:
    genai.configure(uplodaded_file)
else:
    st.sidebar.warning('Please fill out all fields')

if st.sidebar.button("back"):
    st.switch_page("main.py")

prompt = st.text_input("Prompt")

engines = ["gemini-1.5-pro-001", "claude-3-5-sonnet", "llama3", "mixtral-8x7b"]

selected_engine = st.selectbox("Select engine", engines)

if st.button("Generate : "):
    model = genai.generative_models(selected_engine)
    response = model.generate_content(prompt)
    result = ''.join([p.text for p in response.candidates[0].content.parts])
    st.write(result)