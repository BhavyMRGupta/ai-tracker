import streamlit as st
import pandas as pd
import datetime

# --- PAGE CONFIGURATION & STYLING ---
st.set_page_config(
    page_title="AI Pro Mission Control",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling for modern look
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .metric-card {
        background: linear-gradient(135deg, #1e293b, #0f172a);
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #334155;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ AI Pro Quota & Observability Hub")
st.caption("Live monitoring for Bhavy's workspace across projects and categories.")

# --- SIDEBAR: SYNC WITH REAL GOOGLE AI PRO USAGE ---
with st.sidebar:
    st.header("⚙️ Live Quota Settings")
    st.write("Sync with your Google Pro limit screen:")
    current_pct = st.slider("Current Session Usage (%)", min_value=0, max_value=100, value=3)
    weekly_pct = st.slider("Weekly Limit Usage (%)", min_value=0, max_value=100, value=0)
    reset_time = st.text_input("Next Reset At", value="7:27 PM")
    
    st.divider()
    st.subheader("➕ Log a Session")
    user_name = st.selectbox("Profile", ["Bhavy", "Monika", "Rohit"])
    cat = st.selectbox("Category", ["Pure_Academic", "Fun_learning", "others"])
    proj = st.text_input("Project Name", value="learning1")
    tokens_in = st.number_input("Estimated Tokens / Prompts", min_value=100, max_value=500000, value=2500, step=500)
    
    if st.button("Log Activity", type="primary"):
        st.toast(f"Logged {tokens_in:,} tokens for {proj}!", icon="🚀")

# --- TOP ROW: REAL PRO PLAN GAUGES ---
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Session Quota Used", f"{current_pct}%", delta=f"Resets at {reset_time}", delta_color="inverse")
    st.progress(current_pct / 100)

with col2:
    st.metric("Weekly Quota Used", f"{weekly_pct}%", delta="Resets Oct 14", delta_color="inverse")
    st.progress(weekly_pct / 100)

with col3:
    if current_pct >= 85:
        st.error("🚨 HIGH USAGE: Switch to Gemini Flash-Lite!")
    elif current_pct >= 50:
        st.warning("⚠️ Moderate velocity: Watch high-context files.")
    else:
        st.success("✅ Safe Bandwidth: Gemini 3.8 Flash running fast.")

st.divider()

# --- ACTIVITY BREAKDOWN ---
st.subheader("📊 Workspace Activity Log")

# Live Data Table
log_data = pd.DataFrame([
    {"Timestamp": "15:49", "Profile": "Bhavy", "Category": "Fun_learning", "Project": "learning1", "Model": "Flash 3.8", "Tokens": 12000},
    {"Timestamp": "17:49", "Profile": "Bhavy", "Category": "Fun_learning", "Project": "learning1", "Model": "Flash 3.8", "Tokens": 18500},
    {"Timestamp": "18:49", "Profile": "Bhavy", "Category": "others", "Project": "Other1", "Model": "Pro 3.1", "Tokens": 24000},
])

c_table, c_chart = st.columns([1.2, 1])

with c_table:
    # Fixed deprecation: replaced use_container_width with width='stretch'
    st.dataframe(log_data, width="stretch")

with c_chart:
    st.bar_chart(log_data.set_index("Category")["Tokens"])