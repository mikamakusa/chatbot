import streamlit as st
import openai


st.title = "Azure Powered Chatbot"

st.sidebar.header('Azure Credentials')
api_key = st.sidebar.text_input("API KEY : ")
endpoint = st.sidebar.text_input("ENDPOINT : ")

if st.sidebar.button("connect"):
    if api_key and endpoint:
        openai.api_key = api_key
        openai.api_base = endpoint
    else:
        st.sidebar.warning('Please fill out all fields')

if st.sidebar.button("back"):
    st.switch_page("main.py")

prompt = st.text_input("Prompt")
engines = [
    "text-davinci-003", "text-curie-001", "text-babbage-001", "text-ada-001", "gpt4"
]

selected_engine = st.selectbox("Select engine", engines)

def get_openai_response(prompt):
    response = openai.Completion.create(
        engine=selected_engine,
        prompt=prompt
    )
    return response.choices[0].text.strip()

if st.button("Generate"):
    with st.spinner("Answering..."):
        generated_text = get_openai_response(prompt)
        st.write("Answer :")
        st.write(generated_text)