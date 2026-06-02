import os
from groq import Groq
import streamlit as st

def get_atk_justification(category, architecture):
    """
    Live Cloud AI engine utilizing Groq API and Llama 3.
    """
    # Securely pulls the API key from Streamlit's hidden vault
    api_key = st.secrets["GROQ_API_KEY"]
    client = Groq(api_key=api_key)
    
    prompt = f"Write a brief, one-paragraph executive business case justifying why we should automate the operational task '{category}' using a '{architecture}' framework. Focus on ROI and enterprise efficiency."
    
    try:
        # Makes the call to the live Llama model
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant", 
            messages=[
                {"role": "system", "content": "You are an elite enterprise transformation consultant. Keep responses punchy, corporate, and highly professional."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"🚨 API Connection Error: {str(e)}"
