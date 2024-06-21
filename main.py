import streamlit as st
from transformers import GPT2LMHeadModel, GPT2Tokenizer

model_name = ""
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

def generate_response(prompt):
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(inputs, max_length=150, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

st.title("Chatbot")
st.write("Entrez votre message")

user_input= st.text_input("Vous :")

if user_input:
    response = generate_response(user_input)
    st.write(f"Chatbot : {response}")

