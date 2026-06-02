import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from ai_engine import get_atk_justification, generate_executive_summary

# ----------------------------------------------------
# 1. PAGE CONFIGURATION & ENTERPRISE THEMING
# ----------------------------------------------------
st.set_page_config(
    page_title="Cognizant Transformation Intelligence Hub",
    page_icon="🏢",
    layout="wide"
)

# Premium dark corporate theme injection
st.markdown("""
    <style>
    .main { background-color: #0d1117; color: #c9d1d9; }
    h1, h2, h3 { color: #ffffff !important; font-family: 'Helvetica Neue', sans-serif; }
    .stButton>button { background-color: #21262d; color: #c9d1d9; border: 1px solid #30363d; width: 100%; }
    .stButton>button:hover { background-color: #30363d; border-color: #8b949e; color: #ffffff; }
    div[data-testid="stMetricValue"] { color: #58a6ff !important; font-size: 2rem; }
    .stAlert { background-color: #161b22; border: 1px solid #388bfd; color: #c9d1d9; }
    </style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# 2. DATA GENERATION PIPELINE
# ----------------------------------------------------
@st.cache_data
def load_transformation_data():
    """Generates an enterprise-realistic operational baseline dataset."""
    np.random.seed(42)
    categories = [
        "Legacy Invoice Reconciliation", 
        "Manual KYC Compliance Verification", 
        "Multi-App Data Transcription", 
        "Triage & Ticket Assignment", 
        "Cross-System Inventory Auditing"
    ]
    
    data = {
        "Category": categories,
        "Hours_Wasted": [2400, 1850, 3100, 950, 1400],
        "Complexity_Score": [0.4, 0.85, 0.2, 0.35, 0.65],  # 0 to 1 scale
        "Friction_Index": [65, 88, 45, 30, 72],          # Implementation barrier
        "Impact_Potential": [80, 95, 60, 40, 75]         # Strategic yield
    }
    return pd.DataFrame(data)

df = load_transformation_data()

# ----------------------------------------------------
# 3. SIDEBAR PANEL CONTROLS (ROI PARAMETERS)
# ----------------------------------------------------
st.sidebar.image("https://img.icons8.com/fluency/96/000000/organization.png", width=60)
st.sidebar.title("Strategic Parameters")
st.sidebar.markdown("Configure runtime variables for macro financial projections.")

blended_rate = st.sidebar.slider("Blended Contractor Rate ($/hr)", 45, 180, 85)
engineering_yield = st.sidebar.slider("Target Engineering Yield (%)", 50, 100, 85) / 100

total_hours_wasted = df["Hours_Wasted"].sum()
gross_capital_loss = total_hours_wasted * blended_rate
reclaimable_capital = gross_capital_loss * engineering_yield

# ----------------------------------------------------
# 4. HEADER & LIVE AI CO-PILOT INTEGRATION
# ----------------------------------------------------
st.title("🏢 Cognizant Transformation Intelligence Hub")
st.markdown("Automated operational audit, engineering target-mapping, and programmatic ROI projections.")

# The core AI Agent integration block
st.subheader("🧠 AI Executive Co-Pilot")
st.markdown("Trigger an immediate algorithmic audit of the data currently displayed in the tables below.")

if st.button("Analyze Current Dashboard Analytics"):
    with st.spinner("Llama 3.1 parsing cross-departmental bottlenecks..."):
        ai_insights = generate_executive_summary(df)
        st.info(ai_insights)

st.markdown("---")

# Top-level executive metric banners
m1, m2, m3 = st.columns(3)
with m1:
    st.metric("Total Operational Friction", f"{total_hours_wasted:,} Hrs Wasted")
with m2:
    st.metric("Annual Run-Rate Capital Loss", f"${gross_capital_loss:,}")
with m3:
    st.metric("Model Reclaimable Capital", f"${int(reclaimable_capital):,}")

# ----------------------------------------------------
# 5. MULTI-TAB ARCHITECTURE
# ----------------------------------------------------
tab1, tab2, tab3 = st.tabs(["📊 Labor Sinks & ROI Matrix", "🤖 Automation Capitalization Registry", "🛡️ GRC Framework"])

with tab1:
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Operational Effort Distribution")
        sorted_df = df.sort_values(by="Hours_Wasted", ascending=False)
        
        fig_bar = go.Figure(go.Bar(
            x=sorted_df["Hours_Wasted"],
            y=sorted_df["Category"],
            orientation='h',
            marker=dict(color='#58a6ff', line=dict(color='#30363d', width=1))
        ))
        fig_bar.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', 
            plot_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(gridcolor='#1f242c', tickfont=dict(color='#8b949e')),
            yaxis=dict(autorange="reversed", tickfont=dict(color='#8b949e')),
            margin=dict(l=20, r=20, t=20, b=20), 
            height=350
        )
        st.plotly_chart(fig_bar, use_container_width=True)
        
    with col2:
        st.markdown("### Feasibility vs. Impact Matrix")
        
        fig_scatter = go.Figure(go.Scatter(
            x=df["Friction_Index"],
            y=df["Impact_Potential"],
            mode='markers+text',
            text=df["Category"].apply(lambda x: x[:15] + "..."),
            textposition="top center",
            marker=dict(size=14, color=df["Complexity_Score"], colorscale='Viridis', showscale=True),
            textfont=dict(color='#8b949e')
        ))
        fig_scatter.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', 
            plot_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(
                title=dict(text="Implementation Friction Index", font=dict(color='#8b949e')), 
                gridcolor='#1f242c', 
                tickfont=dict(color='#8b949e')
            ),
            yaxis=dict(
                title=dict(text="Strategic Impact Potential", font=dict(color='#8b949e')), 
                gridcolor='#1f242c', 
                tickfont=dict(color='#8b949e')
            ),
            margin=dict(l=20, r=20, t=20, b=20), 
            height=350
        )
        st.plotly_chart(fig_scatter, use_container_width=True)

with tab2:
    st.markdown("### Algorithmic Architecture Mapping")
    st.markdown("Select a baseline labor sink and assign a structural engineering pattern to generate a tailored AI justification.")
    
    sel1, sel2 = st.columns(2)
    with sel1:
        selected_task = st.selectbox("Isolate Labor Target Node", df["Category"].tolist())
    with sel2:
        selected_tech = st.selectbox("Target Automation Architecture Pattern", [
            "Generative AI / LLM Agent Core", 
            "Heuristic RPA Scripting Loop", 
            "Event-Driven Rest API Pipeline"
        ])
    
    if st.button("Generate AI Business Case"):
        with st.spinner("Compiling contextual corporate justification..."):
            case_text = get_atk_justification(selected_task, selected_tech)
            st.success(case_text)

with tab3:
    st.markdown("### Governance, Risk, and Compliance (GRC) Guardrails")
    st.warning("⚠️ All proposed cloud LLM architectures must map to internal security baselines.")
    
    st.markdown("""
    * **Data Sanitization Layer:** Zero Retention Architecture enforced at the API gateway layer. No corporate PII passes tokenization bounds.
    * **Model Isolation:** Enterprise payloads are processed over highly isolated VPC networks using dedicated, zero-data-training endpoints.
    * **Execution Boundaries:** Generative agents run purely inside deterministic environments with explicit human-in-the-loop validation barriers.
    """)
