import streamlit as st
import google.generativeai as genai

st.title("VIP AI Agent")

# Yahan apni API Key likh do (jo aapne Google AI Studio se li hai)
my_api_key = "YAHAN_APNI_API_KEY_LIKHO"

genai.configure(api_key=my_api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

if prompt := st.chat_input("G Sir..."):
    st.chat_message("user").markdown(prompt)
    try:
        response = model.generate_content(prompt)
        st.chat_message("assistant").markdown(response.text)
    except Exception as e:
        st.error(f"Error: {e}")
