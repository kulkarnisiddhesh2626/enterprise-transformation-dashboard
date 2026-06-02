import os
from groq import Groq
import streamlit as st

def get_client():
    """Securely initializes the Groq client using Streamlit secrets."""
    try:
        api_key = st.secrets["GROQ_API_KEY"]
        return Groq(api_key=api_key)
    except Exception:
        st.error("🔒 GROQ_API_KEY missing from Streamlit Secrets. Please check your app settings.")
        return None

def get_atk_justification(category, architecture):
    """Generates a targeted executive business case for specific tech stack implementations."""
    client = get_client()
    if not client:
        return "AI Engine offline: Key missing."
        
    prompt = f"""
    Write a professional, single-paragraph executive business case justifying why we should automate 
    the operational task '{category}' using a '{architecture}' framework. 
    Focus strictly on enterprise execution efficiency, risk mitigation, and structural scalability. 
    Keep it punchy, corporate, and do not use generic introductory filler text.
    """
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant", 
            messages=[
                {"role": "system", "content": "You are a managing director of technology strategy at a global consulting firm."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"🚨 API Connection Error: {str(e)}"

def generate_executive_summary(dataframe):
    """Parses operational data metrics to extract macro-level anomalies and strategy directives."""
    client = get_client()
    if not client:
        return "AI Engine offline: Key missing."
        
    compressed_data = dataframe.groupby('Category')['Hours_Wasted'].sum().reset_index()
    data_string = compressed_data.to_string(index=False)
    
    prompt = f"""
    You are an elite corporate operations auditor. Review this dataset representing 
    annual operational labor sinks across our core business segments.
    
    DATA (Hours Wasted annually per Category):
    {data_string}
    
    Provide a highly strategic, 3-bullet-point executive summary for leadership:
    1. Identify the single most critical labor sink and calculate its baseline percentage strain relative to the others.
    2. Pinpoint a structural bottleneck indicated by these numbers.
    3. Issue an immediate tactical directive on where automation capital must be deployed first.
    
    Keep the tone clinical, sharp, and highly technical. No conversational fluff.
    """
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant", 
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"🚨 AI Data Analysis Failed: {str(e)}"

def ask_co_pilot_question(dataframe, user_query):
    """Allows users to query the state of the dashboard database using natural conversational language."""
    client = get_client()
    if not client:
        return "AI Engine offline: Key missing."
        
    data_string = dataframe.to_string(index=False)
    
    prompt = f"""
    You are the built-in AI Data Assistant for this enterprise dashboard. Answer the user's natural language question based strictly on the current operational metrics provided below.
    
    CURRENT METRICS DATASET:
    {data_string}
    
    USER QUESTION: {user_query}
    
    Formulate your answer concisely. Use clear numbers, calculate percentages if asked, and maintain an objective enterprise advisor tone.
    """
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant", 
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"🚨 Query Exception: {str(e)}"
