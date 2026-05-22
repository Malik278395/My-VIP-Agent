import streamlit as st
from groq import Groq

st.title("VIP AI Agent (Groq Power)")

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

if prompt := st.chat_input("G Sir..."):
    st.chat_message("user").markdown(prompt)
    
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama3-70b-8192", # Ye bohot powerful model hai
    )
    
    response = chat_completion.choices[0].message.content
    st.chat_message("assistant").markdown(response)
