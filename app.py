import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import os
from data_generator import generate_mock_data
from ai_engine import get_atk_justification

# --- 1. PREMIUM APP CONFIGURATION ---
st.set_page_config(
    page_title="Cognizant Transformation Hub", 
    layout="wide", 
    page_icon="🏢",
    initial_sidebar_state="expanded"
)

# --- 2. ADVANCED DATA ENGINE & CACHING ---
@st.cache_data
def load_and_preprocess_data():
    if not os.path.exists('synthetic_data.csv'):
        generate_mock_data()
    df = pd.read_csv('synthetic_data.csv')
    return df

df = load_and_preprocess_data()

# --- 3. CUSTOM UI/UX INJECTION (Light Enterprise Brand Kit) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global Core Layout Styling */
    html, body, [data-testid="stAppViewContainer"], .main {
        font-family: 'Inter', sans-serif !important;
        background-color: #F8FAFC !important;
    }
    
    /* Clean White Sidebar Layout */
    [data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        border-right: 1px solid #E2E8F0 !important;
    }
    
    /* Sidebar Section Text Colors (Dark for white background) */
    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3, 
    [data-testid="stSidebar"] h4, 
    [data-testid="stSidebar"] h5, 
    [data-testid="stSidebar"] h6,
    [data-testid="stSidebar"] p {
        color: #0C1C3C !important;
    }
    
    /* Form Label Styling */
    [data-testid="stSidebar"] [data-testid="stWidgetLabel"] p {
        color: #475569 !important;
        font-weight: 600 !important;
        font-size: 13px !important;
    }

    /* Form Inputs and Dropdowns */
    [data-testid="stSidebar"] div[data-baseweb="select"] * {
        color: #0F172A !important;
    }
    [data-testid="stSidebar"] input {
        color: #0F172A !important;
    }
    
    /* Slider Controls Styling */
    [data-testid="stSidebar"] [data-testid="stThumbValue"] {
        color: #0F172A !important;
        font-weight: 600 !important;
    }
    [data-testid="stSidebar"] [data-testid="stTickBarMin"], 
    [data-testid="stSidebar"] [data-testid="stTickBarMax"] {
        color: #64748B !important;
    }
    
    /* Clean Enterprise Tab Row */
    button[data-baseweb="tab"] {
        font-size: 14px !important;
        font-weight: 600 !important;
        padding: 14px 24px !important;
        color: #64748B !important;
        transition: all 0.2s ease-in-out;
    }
    button[data-baseweb="tab"][aria-selected="true"] {
        color: #0033A0 !important;
        border-bottom-color: #0033A0 !important;
    }
    
    /* Core Metric Callouts */
    div[data-testid="stMetric"] {
        background: #ffffff !important;
        padding: 22px !important;
        border-radius: 10px !important;
        box-shadow: 0 4px 12px rgba(15, 23, 42, 0.03) !important;
        border: 1px solid #E2E8F0 !important;
        border-top: 4px solid #0033A0 !important;
    }
    div[data-testid="stMetricLabel"] {
        font-weight: 600 !important;
        color: #64748B !important;
        text-transform: uppercase;
        font-size: 11px !important;
        letter-spacing: 0.75px;
    }
    div[data-testid="stMetricValue"] {
        font-weight: 700 !important;
        color: #0C1C3C !important;
        font-size: 26px !important;
    }
    
    /* System Alert Formatting */
    .stAlert {
        border-radius: 8px !important;
        border: none !important;
        background-color: #EFF6FF !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- 4. CORPORATE SIDEBAR CONTROLS & MODELING CONFIG ---
# Official Cognizant Logo
COGNIZANT_LOGO = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Cognizant_logo_2022.svg/512px-Cognizant_logo_2022.svg.png"

# Padding container for the logo to sit nicely in the white sidebar
st.sidebar.markdown("<div style='padding-top: 10px; padding-bottom: 20px;'>", unsafe_allow_html=True)
st.sidebar.image(COGNIZANT_LOGO, width=190)
st.sidebar.markdown("</div>", unsafe_allow_html=True)

st.sidebar.markdown("<h4 style='margin:0; font-size:16px; color:#0033A0 !important;'>Global Controls</h4>", unsafe_allow_html=True)

reporting_period = st.sidebar.selectbox("Reporting Window", ["FY26 - Q1", "FY26 - Q2", "FY26 - Q3", "FY26 - Q4"])
selected_tower = st.sidebar.multiselect("Business Segment Group", options=df['Tower'].unique(), default=df['Tower'].unique())
filtered_df = df[df['Tower'].isin(selected_tower)]

st.sidebar.markdown("---")
st.sidebar.markdown("<h4 style='margin:0; font-size:16px; color:#0033A0 !important;'>💡 Real-Time Financial Modeler</h4>", unsafe_allow_html=True)
target_rate = st.sidebar.slider("Blended Contractor Rate ($/hr)", min_value=25, max_value=150, value=65, step=5)
efficiency_upside = st.sidebar.slider("Expected Engineering Yield (%)", min_value=10, max_value=70, value=35, step=5)

st.sidebar.markdown("---")
st.sidebar.markdown("<h4 style='margin:0; font-size:16px; color:#0033A0 !important;'>Report Extraction</h4>", unsafe_allow_html=True)
csv_data = filtered_df.to_csv(index=False).encode('utf-8')
st.sidebar.download_button(
    label="📥 Generate Audit-Ready Ledger",
    data=csv_data,
    file_name=f"CTS_Transform_Report_{reporting_period.replace(' ', '')}.csv",
    mime='text/csv',
    use_container_width=True
)

# --- 5. EXECUTIVE COMMAND CENTER HEADER ---
st.markdown(f"""
    <div style="background-color: white; padding: 24px; border-radius: 12px; margin-bottom: 25px; border: 1px solid #E2E8F0; box-shadow: 0 4px 12px rgba(15,23,42,0.02);">
        <h1 style="margin: 0; color: #0C1C3C; font-size: 28px; font-weight: 700;">Transformation Intelligence Command Center</h1>
        <p style="margin: 6px 0 0 0; color: #64748B; font-size: 14px;">Cognizant Digital Operations Business Metrics Strategy Unit &bull; <strong>{reporting_period} Workspace</strong></p>
    </div>
""", unsafe_allow_html=True)

# Calculation Engine Logic
total_hours = filtered_df['Hours_Spent'].sum()
total_tasks = len(filtered_df)
current_cost_pool = total_hours * target_rate
projected_savings = current_cost_pool * (efficiency_upside / 100.0)

# Render Custom Metrics Rows
k1, k2, k3, k4 = st.columns(4)
k1.metric("Gross Operational Effort", f"{total_hours:,.0f} Hrs", "Baseline Pool")
k2.metric("Addressable Workflows", f"{total_tasks:,} Nodes", "Aggregated Volume")
k3.metric("Run-Rate Financial Cost", f"${current_cost_pool:,.0f}", f"@ ${target_rate}/hr blended")
k4.metric("Modeled Annual Value", f"${projected_savings:,.0f}", f"At {efficiency_upside}% Yield Target", delta_color="normal")

st.markdown("<br>", unsafe_allow_html=True)

# --- 6. ADVANCED INTERACTIVE EXPERIENCES (TABS WITH EXPLICIT TITLES) ---
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Operational Effort Distribution", 
    "🤖 Automation Capitalization Registry", 
    "💰 Predictive ROI Modeling", 
    "⚖️ Feasibility vs. Impact Matrix", 
    "🛡️ Compliance & Risk Guardrails"
])

# TAB 1: PARETO EFFORT TOPOGRAPHY
with tab1:
    st.markdown("## 📊 Operational Effort Distribution Analysis")
    st.markdown("##### Visualizing workflow resource concentration profiles across active functional teams to isolate labor sinks.")
    st.markdown("---")
    
    dimension = st.segmented_control("Analyze Distribution Vectors:", options=['Category', 'Tower', 'Task_Type'], default='Category')
    
    pareto_data = filtered_df.groupby(dimension)['Hours_Spent'].sum().reset_index().sort_values(by='Hours_Spent', ascending=False)
    pareto_data['Cumulative_Percentage'] = (pareto_data['Hours_Spent'].cumsum() / pareto_data['Hours_Spent'].sum()) * 100
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=pareto_data[dimension], y=pareto_data['Hours_Spent'], name="Aggregated Hours",
        marker=dict(color='#0033A0', cornerradius="top 8px"),
        hovertemplate="<b>%{x}</b><br>Total Effort: %{y:,.0f} Hours<extra></extra>"
    ))
    fig.add_trace(go.Scatter(
        x=pareto_data[dimension], y=pareto_data['Cumulative_Percentage'], name="Pareto Curve %",
        yaxis="y2", line=dict(color="#00B140", width=3, shape="spline"), mode="lines+markers"
    ))
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        yaxis=dict(title="Operational Time (Hours)", gridcolor="#E2E8F0"),
        yaxis2=dict(title="Cumulative Share (%)", overlaying="y", side="right", range=[0, 105], showgrid=False),
        margin=dict(l=40, r=40, t=20, b=40),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    st.plotly_chart(fig, use_container_width=True)

# TAB 2: REGISTRY & AI CASE BUILDER
with tab2:
    st.markdown("## 🤖 Automation Capitalization Registry")
    st.markdown("##### Systematic algorithmic assignment of technological levers determined by complexity rankings and log attributes.")
    st.markdown("---")
    
    opp_df = filtered_df.groupby(['Category', 'Complexity'])['Hours_Spent'].sum().reset_index()
    opp_df = opp_df.sort_values(by='Hours_Spent', ascending=False).rename(columns={'Hours_Spent': 'Monthly_Hours'})
    
    def assign_lever(row):
        if 'Meeting' in row['Category'] or 'Align' in row['Category']: return 'Process Redesign'
        elif row['Complexity'] == 'Low': return 'RPA / Scripted Core'
        elif row['Complexity'] == 'Medium': return 'API Matrix Layer'
        else: return 'Generative AI Framework'
        
    opp_df['Target_Architecture'] = opp_df.apply(assign_lever, axis=1)
    opp_df['Yield_Forecast_Hours'] = (opp_df['Monthly_Hours'] * (efficiency_upside / 100.0)).round(0)
    
    st.dataframe(
        opp_df[['Category', 'Complexity', 'Target_Architecture', 'Monthly_Hours', 'Yield_Forecast_Hours']],
        column_config={
            "Category": "Identified Task Objective",
            "Complexity": st.column_config.TextColumn("Complexity Matrix"),
            "Target_Architecture": st.column_config.TextColumn("Recommended Stack"),
            "Monthly_Hours": st.column_config.NumberColumn("Monthly Baseline (Hrs)", format="%d hrs"),
            "Yield_Forecast_Hours": st.column_config.ProgressColumn("Target Optimization Yield", format="%d hrs", min_value=0, max_value=int(opp_df['Monthly_Hours'].max()))
        },
        use_container_width=True,
        hide_index=True
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    c1, c2 = st.columns([1, 2])
    with c1:
        st.markdown("### 💡 Cognizant AI Justification Agent")
        st.write("Synthesize an instant automated business case proposal for internal executive alignment review boards.")
        selected_task = st.selectbox("Target Pipeline Entry:", options=opp_df['Category'].unique())
    with c2:
        selected_row = opp_df[opp_df['Category'] == selected_task].iloc[0]
        st.markdown("<div style='height:40px;'></div>", unsafe_allow_html=True)
        if st.button("Generate Strategic Business Case", use_container_width=True):
            with st.spinner("Processing Model Directives via Secure Node..."):
                justification = get_atk_justification(selected_row['Category'], selected_row['Target_Architecture'])
                st.markdown(f"""
                    <div style="background-color: #F8FAFC; padding: 20px; border-radius: 8px; border: 1px dashed #0033A0;">
                        <strong style="color:#0033A0; font-size:14px;">Strategic Proposal Draft:</strong><br><br>
                        <span style="font-size: 13.5px; color:#334155; line-height:1.6;">{justification}</span>
                    </div>
                """, unsafe_allow_html=True)

# TAB 3: FINANCIAL ROI MATRIX
with tab3:
    st.markdown("## 💰 Predictive ROI Modeling Matrix")
    st.markdown("##### Dynamic optimization sensitivity charting visualizing projected hours salvaged alongside financial reclamation figures.")
    st.markdown("---")
    
    tower_savings = filtered_df.groupby('Tower')['Hours_Spent'].sum().reset_index()
    tower_savings['Calculated_Hours_Saved'] = tower_savings['Hours_Spent'] * (efficiency_upside / 100.0)
    tower_savings['Calculated_Cash_Value'] = tower_savings['Calculated_Hours_Saved'] * target_rate
    
    fig2 = go.Figure()
    fig2.add_trace(go.Bar(
        x=tower_savings['Tower'], y=tower_savings['Calculated_Hours_Saved'], 
        name='Hours Salvaged / Mo', marker_color='#00B140', text=tower_savings['Calculated_Hours_Saved'].astype(int), textposition='auto'
    ))
    fig2.add_trace(go.Bar(
        x=tower_savings['Tower'], y=tower_savings['Calculated_Cash_Value'], 
        name='Monthly Cash Reclamation ($)', marker_color='#0033A0', yaxis="y2", text=tower_savings['Calculated_Cash_Value'].astype(int), textposition='outside'
    ))
    
    fig2.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        barmode='group',
        yaxis=dict(title="Effort Recoverable (Hours)", gridcolor="#E2E8F0"),
        yaxis2=dict(title="Financial Return Value ($)", overlaying="y", side="right", showgrid=False),
        margin=dict(l=40, r=40, t=30, b=40),
        legend=dict(orientation="h", yanchor="bottom", y=1.05, xanchor="left", x=0)
    )
    st.plotly_chart(fig2, use_container_width=True)

# TAB 4: STRATEGIC MATRIX
with tab4:
    st.markdown("## ⚖️ Strategic Feasibility vs. Impact Coordinates")
    st.markdown("##### Decision matrix detailing operational friction against time rewards. Target the upper-left quadrant for maximum efficiency yields.")
    st.markdown("---")
    
    matrix_data = filtered_df.groupby('Category').agg({'Hours_Spent': 'sum', 'Complexity': 'first'}).reset_index()
    cost_map = {'Low': 2.0, 'Medium': 5.0, 'High': 8.0}
    
    np.random.seed(42)
    matrix_data['Cost_Score'] = matrix_data['Complexity'].map(cost_map) + np.random.uniform(-0.6, 0.6, len(matrix_data))
    
    fig3 = go.Figure()
    fig3.add_trace(go.Scatter(
        x=matrix_data['Cost_Score'], y=matrix_data['Hours_Spent'],
        mode='markers+text', text=matrix_data['Category'], textposition="top center",
        marker=dict(size=16, color=matrix_data['Hours_Spent'], colorscale='Blues', showscale=False, line=dict(width=1, color='#0C1C3C'))
    ))
    
    fig3.add_hline(y=matrix_data['Hours_Spent'].median(), line_dash="dot", line_color="#CBD5E1", line_width=1.5)
    fig3.add_vline(x=5.0, line_dash="dot", line_color="#CBD5E1", line_width=1.5)
    
    fig3.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(title="Implementation Friction / Expense Rating (0 ➡️ 10)", range=[0, 10], gridcolor="#E2E8F0"),
        yaxis=dict(title="Identified Process Efficiency Potential (Hours Pool)", gridcolor="#E2E8F0"),
        margin=dict(l=40, r=40, t=20, b=40)
    )
    st.plotly_chart(fig3, use_container_width=True)

# TAB 5: COMPLIANCE GOVERNANCE GUARDRAILS
with tab5:
    st.markdown("## 🛡️ Corporate Governance, Risk & Compliance (GRC)")
    st.markdown("##### Mandated enterprise architecture guidelines, strict infrastructure whitelists, and validation workflow controls.")
    st.markdown("---")
    
    g1, g2 = st.columns(2)
    with g1:
        with st.container(border=True):
            st.markdown("#### 🔒 Infrastructure Whitelist Controls")
            st.markdown("""
            * **Execution Substrate:** Hardened local runtime execution environments completely decoupled from external edge endpoints.
            * **Inference Pipeline Layer:** Dedicated sandboxed deployments on internal enterprise nodes using local execution blocks. Zero payload tracking or external storage vectors.
            * **Data Asset Boundary:** All metrics sanitized dynamically before entering ingestion views.
            """)
    with g2:
        with st.container(border=True):
            st.markdown("#### 🛡️ Human Management Authorization Gates")
            st.markdown("""
            * **Validation Gate 1:** Continuous monitoring validation reviews required from designated Delivery Tower Operations leads prior to code deployment.
            * **Validation Gate 2:** Release cycles strictly bound to standard automated testing criteria and rollback procedures.
            * **Fallback Loop Priority:** System defaults immediately to structural queues if confidence metrics slide beneath the 85% operational index threshold.
            """)