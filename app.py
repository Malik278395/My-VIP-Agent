import streamlit as st
import google.generativeai as genai

st.title("VIP AI Agent")

# Yahan apni API Key daalna
api_key = "PASTE_YOUR_GEMINI_API_KEY_HERE"
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

if prompt := st.chat_input("Kuch pucho..."):
    st.chat_message("user").markdown(prompt)
    response = model.generate_content(prompt)
    st.chat_message("assistant").markdown(response.text)
