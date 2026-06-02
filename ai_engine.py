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
    """
    Generates a targeted, one-paragraph executive business case 
    for automating a specific task with a specific tech stack.
    """
    client = get_client()
    if not client:
        return "AI Engine offline: Key missing."
        
    prompt = f"""
    Write a professional, single-paragraph executive business case justifying why we should automate 
    the operational task '{category}' using a '{architecture}' framework. 
    Focus strictly on enterprise execution efficiency, risk mitigation, and structural scalability. 
    Keep it punchy, corporate, and do not use generic intro phrases.
    """
    
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant", 
            messages=[
                {"role": "system", "content": "You are a senior managing director of technology strategy at a global consulting firm."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"🚨 API Connection Error: {str(e)}"

def generate_executive_summary(dataframe):
    """
    Aggregates the current state of the dashboard data and passes it 
    to the LLM for high-level cross-departmental anomaly detection and strategy.
    """
    client = get_client()
    if not client:
        return "AI Engine offline: Key missing."
        
    # Aggregate data to minimize tokens and keep analytics clean
    compressed_data = dataframe.groupby('Category')['Hours_Wasted'].sum().reset_index()
    data_string = compressed_data.to_string(index=False)
    
    prompt = f"""
    You are an elite corporate operations auditor and data analyst. Review this dataset representing 
    the current operational labor sinks across our core business segments.
    
    DATA (Hours Wasted annually per Category):
    {data_string}
    
    Provide a highly strategic, 3-bullet-point executive summary for leadership:
    1. Identify the single most critical labor sink and calculate its baseline percentage strain relative to the others.
    2. Pinpoint a hidden structural correlation or bottleneck indicated by these numbers.
    3. Issue an immediate tactical directive on where automation capital must be deployed first.
    
    Keep the tone clinical, sharp, and highly technical. No conversational fluff.
    """
    
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant", 
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2  # Low temperature forces strict analytical accuracy
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"🚨 AI Data Analysis Failed: {str(e)}"
