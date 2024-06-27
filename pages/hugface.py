import streamlit as st
import huggingface_hub as hf
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

st.title = "Huggingface Chatbot"

st.sidebar.header("Huggingface Credentials")
hf_token = st.sidebar.text_input("Credentials file : ")
if st.sidebar.button("Connect"):
    if hf_token:
        hf.login(hf_token)

if st.sidebar.button("back"):
    st.switch_page("main.py")

prompt = st.text_input("Prompt")
engines = ["microsoft/DialoGPT-large"]
selected_engine = st.selectbox("Select engine", engines)
tokenizer = AutoTokenizer.from_pretrained(selected_engine)
model = AutoModelForCausalLM.from_pretrained(selected_engine)

def generate_response(prompt, max_length=100, num_return_sequences=1):
    inputs = tokenizer(prompt, return_tensors='pt')
    outputs = model.generate(
        inputs['input_ids'],
        max_length=max_length,
        num_return_sequences=num_return_sequences,
        pad_token_id=tokenizer.eos_token_id
    )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    st.write(response)