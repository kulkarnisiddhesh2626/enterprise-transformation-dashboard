import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from ai_engine import get_atk_justification, generate_executive_summary, ask_co_pilot_question

# ----------------------------------------------------
# 1. HIGH-CONTRAST LIGHT THEME & CSS INJECTION
# ----------------------------------------------------
st.set_page_config(
    page_title="Cognizant Transformation Intelligence Hub",
    page_icon="🏢",
    layout="wide"
)

# Premium light corporate stylesheet forcing sharp black text and readable elements
st.markdown("""
    <style>
    /* Main body background and font color */
    .main { background-color: #ffffff; color: #000000; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }
    
    /* Strict overrides for titles and headers */
    h1, h2, h3, h4, p, span, li, label { color: #000000 !important; font-weight: 500; }
    h1, h2, h3 { font-weight: 700 !important; }
    
    /* Input element fields text forcing black */
    .stTextInput input { color: #000000 !important; background-color: #f8f9fa !important; border: 1px solid #ced4da !important; }
    div[data-baseweb="select"] { color: #000000 !important; background-color: #f8f9fa !important; }
    
    /* High-contrast Navigation Tabs */
    .stTabs [data-baseweb="tab"] { color: #495057 !important; font-size: 1.05rem; padding: 12px 20px; }
    .stTabs [data-baseweb="tab"][aria-selected="true"] { color: #0056b3 !important; border-bottom-color: #0056b3 !important; font-weight: bold; }
    
    /* Enterprise Buttons */
    .stButton>button { background-color: #f8f9fa; color: #000000 !important; border: 1px solid #ced4da; border-radius: 6px; padding: 10px; font-weight: 600; transition: 0.2s ease; }
    .stButton>button:hover { background-color: #e2e6ea; border-color: #0056b3; color: #0056b3 !important; }
    
    /* Metrics panel configuration */
    div[data-testid="stMetricValue"] { color: #0056b3 !important; font-size: 2.2rem !important; font-weight: 700; }
    div[data-testid="stMetricLabel"] { color: #212529 !important; font-size: 0.95rem !important; font-weight: 600; }
    
    /* Content alert boxes and info windows */
    .stAlert { background-color: #f8f9fa; border: 1px solid #0056b3; border-radius: 8px; color: #000000 !important; }
    .stAlert p { color: #000000 !important; }
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
st.sidebar.caption("📍 Database Node: `Production_V1`")
st.sidebar.caption("🔒 Network State: `Isolated Secure API`")

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
        marker=dict(color='#0056b3', line=dict(color='#ced4da', width=1)),
        hovertemplate='<b>%{y}</b><br>Hours Wasted: %{x:,}<extra></extra>'
    ))
    fig_bar.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', 
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(gridcolor='#e9ecef', tickfont=dict(color='#000000'), title=dict(text="Annual Hours Spent Inefficiently", font=dict(color='#000000'))),
        yaxis=dict(autorange="reversed", tickfont=dict(color='#000000')),
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
        marker=dict(size=16, color=df["Complexity_Score"], colorscale='Blues', showscale=True, colorbar=dict(title=dict(text="Complexity", font=dict(color='#000000')), tickfont=dict(color='#000000'))),
        textfont=dict(color='#000000', size=11),
        hovertemplate='<b>%{text}</b><br>Friction: %{x}<br>Impact: %{y}<extra></extra>'
    ))
    fig_scatter.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', 
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(title=dict(text="Implementation Friction Index (Higher = Harder)", font=dict(color='#000000')), gridcolor='#e9ecef', tickfont=dict(color='#000000')),
        yaxis=dict(title=dict(text="Strategic Impact Yield Potential", font=dict(color='#000000')), gridcolor='#e9ecef', tickfont=dict(color='#000000')),
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
