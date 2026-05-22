import streamlit as st
import google.generativeai as genai

st.title("VIP AI Agent")

# Hum secrets se key utha rahe hain
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

if prompt := st.chat_input("G Sir..."):
    st.chat_message("user").markdown(prompt)
    try:
        response = model.generate_content(prompt)
        st.chat_message("assistant").markdown(response.text)
    except Exception as e:
        st.error(f"Error: {e}")
