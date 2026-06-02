import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from ai_engine import get_atk_justification, generate_executive_summary, ask_co_pilot_question

# ----------------------------------------------------
# 1. PREMIUM LAYOUT & CUSTOM STYLING CONFIGURATION
# ----------------------------------------------------
st.set_page_config(
    page_title="Cognizant Transformation Intelligence Hub",
    page_icon="🏢",
    layout="wide"
)

# Custom clean, modern enterprise dark style sheets
st.markdown("""
    <style>
    .main { background-color: #0b0e14; color: #adbac7; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }
    h1, h2, h3, h4 { color: #ffffff !important; font-weight: 600 !important; }
    .stTabs [data-baseweb="tab"] { color: #768390 !important; font-size: 1.05rem; padding: 12px 20px; }
    .stTabs [data-baseweb="tab"][aria-selected="true"] { color: #539bf5 !important; border-bottom-color: #539bf5 !important; font-weight: bold; }
    .stButton>button { background-color: #1c2128; color: #adbac7; border: 1px solid #373e47; border-radius: 6px; padding: 10px; font-weight: 500; transition: 0.2s ease; }
    .stButton>button:hover { background-color: #22272e; border-color: #539bf5; color: #ffffff; }
    div[data-testid="stMetricValue"] { color: #539bf5 !important; font-size: 2.2rem !important; font-weight: 600; }
    div[data-testid="stMetricLabel"] { color: #768390 !important; font-size: 0.95rem !important; }
    .stAlert { background-color: #1c2128; border: 1px solid #373e47; border-radius: 8px; color: #adbac7; }
    .css-1r6slb0 { background-color: #1c2128; border: 1px solid #373e47; border-radius: 8px; padding: 20px; }
    </style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# 2. SEED ENHANCED ENTERPRISE DATAFRAME
# ----------------------------------------------------
@st.cache_data
def load_transformation_data():
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
        "Complexity_Score": [0.4, 0.85, 0.2, 0.35, 0.65],
        "Friction_Index": [65, 88, 45, 30, 72],
        "Impact_Potential": [80, 95, 60, 40, 75]
    }
    return pd.DataFrame(data)

df = load_transformation_data()

# ----------------------------------------------------
# 3. SIDEBAR CONTROL CONSOLE & REAL-TIME PROJECTIONS
# ----------------------------------------------------
st.sidebar.image("https://img.icons8.com/fluency/96/000000/organization.png", width=55)
st.sidebar.title("Operational Variables")
st.sidebar.markdown("Modify financial parameters to adjust active machine projections instantly.")

blended_rate = st.sidebar.slider("Blended Labor Rate ($/hr)", 45, 180, 85)
engineering_yield = st.sidebar.slider("Target Engineering Yield (%)", 50, 100, 85) / 100

total_hours_wasted = df["Hours_Wasted"].sum()
gross_capital_loss = total_hours_wasted * blended_rate
reclaimable_capital = gross_capital_loss * engineering_yield

# Sidebar footprint overview
st.sidebar.markdown("---")
st.sidebar.markdown("### Active Session Scope")
st.sidebar.caption(f"📍 Database Node: `Production_V1`")
st.sidebar.caption(f"🔒 Network State: `Isolated Secure API`")

# ----------------------------------------------------
# 4. TITLE COMPONENT & TOP HEADER METRICS
# ----------------------------------------------------
st.title("🏢 Cognizant Transformation Intelligence Hub")
st.markdown("Modern operational discovery engine mapped to programmatic engineering pipelines.")

# Structural high-readability KPI blocks
with st.container():
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric("Identified Operational Friction", f"{total_hours_wasted:,} Hours Wasted")
    with m2:
        st.metric("Annualized Friction Run-Rate", f"${gross_capital_loss:,}")
    with m3:
        st.metric("Modelled Capital Reclamation", f"${int(reclaimable_capital):,}")

st.markdown("---")

# ----------------------------------------------------
# 5. EXPANDED 5-TAB ARCHITECTURE PIPELINE
# ----------------------------------------------------
tabs = st.tabs([
    "🧠 AI Co-Pilot & Data Chat", 
    "📊 Operational Labor Sinks", 
    "⚖️ Feasibility Matrix", 
    "🤖 Automation Capitalization Registry", 
    "🛡️ GRC Compliance Framework"
])

# ---- TAB 1: AI CO-PILOT ----
with tabs[0]:
    st.subheader("Interactive AI Intelligence Layer")
    st.markdown("Run automated diagnostic summaries or ask the context-aware model direct business questions regarding your data infrastructure.")
    
    col_a, col_b = st.columns([1, 1])
    
    with col_a:
        st.markdown("### 📊 Automated Macro Audit")
        if st.button("Generate Executive Analysis Report"):
            with st.spinner("AI analyzing core cross-departmental datasets..."):
                report = generate_executive_summary(df)
                st.info(report)
                
    with col_b:
        st.markdown("### 💬 Chat with Your Dataset")
        user_query = st.text_input("Ask a question (e.g., 'Which system has the highest friction score?')", placeholder="Type operational inquiry here...")
        if st.button("Submit Inquiry"):
            if user_query.strip() != "":
                with st.spinner("Sifting metrics for context..."):
                    answer = ask_co_pilot_question(df, user_query)
                    st.success(answer)
            else:
                st.warning("Please type a valid data question first.")

# ---- TAB 2: OPERATIONAL LABOR SINKS ----
with tabs[1]:
    st.subheader("Operational Effort Distribution")
    st.markdown("Pareto mapping of severe manual engineering overhead across target workflow components.")
    
    sorted_df = df.sort_values(by="Hours_Wasted", ascending=False)
    
    fig_bar = go.Figure(go.Bar(
        x=sorted_df["Hours_Wasted"],
        y=sorted_df["Category"],
        orientation='h',
        marker=dict(color='#316dca', line=dict(color='#444c56', width=1)),
        hovertemplate='<b>%{y}</b><br>Hours Wasted: %{x:,}<extra></extra>'
    ))
    fig_bar.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', 
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(gridcolor='#22272e', tickfont=dict(color='#768390'), title=dict(text="Annual Hours Spent Inefficiently", font=dict(color='#768390'))),
        yaxis=dict(autorange="reversed", tickfont=dict(color='#768390')),
        margin=dict(l=20, r=20, t=10, b=20), 
        height=380
    )
    st.plotly_chart(fig_bar, use_container_width=True)

# ---- TAB 3: FEASIBILITY MATRIX ----
with tabs[2]:
    st.subheader("Strategic Quadrant Analysis")
    st.markdown("Mapping friction limitations against targeted optimization returns to isolate execution targets.")
    
    fig_scatter = go.Figure(go.Scatter(
        x=df["Friction_Index"],
        y=df["Impact_Potential"],
        mode='markers+text',
        text=df["Category"].apply(lambda x: x if len(x) <= 20 else x[:17] + "..."),
        textposition="top center",
        marker=dict(size=16, color=df["Complexity_Score"], colorscale='Blues', showscale=True, colorbar=dict(title=dict(text="Complexity", font=dict(color='#768390')), tickfont=dict(color='#768390'))),
        textfont=dict(color='#adbac7', size=11),
        hovertemplate='<b>%{text}</b><br>Friction: %{x}<br>Impact: %{y}<extra></extra>'
    ))
    fig_scatter.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', 
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(title=dict(text="Implementation Friction Index (Higher = Harder)", font=dict(color='#768390')), gridcolor='#22272e', tickfont=dict(color='#768390')),
        yaxis=dict(title=dict(text="Strategic Impact Yield Potential", font=dict(color='#768390')), gridcolor='#22272e', tickfont=dict(color='#768390')),
        margin=dict(l=20, r=20, t=30, b=20), 
        height=400
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

# ---- TAB 4: AUTOMATION REGISTRY ----
with tabs[3]:
    st.subheader("Programmatic Pattern Engineering Framework")
    st.markdown("Isolate localized enterprise workloads to generate tailored execution justification portfolios automatically via the cloud core.")
    
    sel1, sel2 = st.columns(2)
    with sel1:
        selected_task = st.selectbox("Isolate Target Asset Node", df["Category"].tolist())
    with sel2:
        selected_tech = st.selectbox("Target Automation Solution Architecture", [
            "Generative AI / Autonomous LLM Agent Core", 
            "Heuristic RPA Scripting Orchestration Loop", 
            "Event-Driven Rest API Integration Layer"
        ])
    
    if st.button("Compile AI Justification Dossier"):
        with st.spinner("Assembling system architecture analysis patterns..."):
            case_text = get_atk_justification(selected_task, selected_tech)
            st.success(case_text)

# ---- TAB 5: GRC COMPLIANCE FRAMEWORK ----
with tabs[4]:
    st.subheader("Governance, Risk, and Compliance (GRC) Guardrails")
    st.info("🛡️ Cryptographic, data infrastructure, and system alignment requirements.")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### 🔒 Network Privacy Architecture")
        st.markdown("""
        * **Ephemeral API State Execution:** Zero-retention configuration flags mapped strictly across upstream proxy endpoints.
        * **PII Redaction Engine:** Automated string hashing executed locally prior to transmission across foreign context windows.
        * **Network Isolation Constraints:** Processing bound exclusively to transport encrypted HTTPS schemas.
        """)
    with c2:
        st.markdown("#### ⚖️ Model Alignment Guidelines")
        st.markdown("""
        * **Deterministic Validation Checks:** Hard logic assertions wrapped outside agent response parsers to control runtime drift.
        * **Audit Trailing Protocols:** Every transactional request logs contextual metrics securely into historical database registries.
        * **Human-In-The-Loop (HITL):** High-impact structural shifts require active operator authorization signatures.
        """)
