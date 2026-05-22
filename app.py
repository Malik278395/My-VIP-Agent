import streamlit as st
import google.generativeai as genai

st.title("VIP AI Agent")

# Secrets se key uthao
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

# 100% sahi naam, "models/" prefix ke saath
model = genai.GenerativeModel('models/gemini-1.5-flash')

if prompt := st.chat_input("Kuch pucho..."):
    st.chat_message("user").markdown(prompt)
    try:
        response = model.generate_content(prompt)
        st.chat_message("assistant").markdown(response.text)
    except Exception as e:
        st.error(f"Error details: {e}")
