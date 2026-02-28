import streamlit as st
import pandas as pd

st.set_page_config(page_title="Job Acceptance Dashboard", layout="wide")

# Load Dataset
df = pd.read_csv("cleaned_job_dataset.csv")

# ---------------- KPI Calculations ---------------- #

total_candidates = len(df)

placed_candidates = df[df['status'] == 1].shape[0]
placement_rate = (placed_candidates / total_candidates) * 100

avg_interview_score = df['interview_score'].mean()
avg_skills_match = df['skills_match_percentage'].mean()

rejected_offers = df[df['status'] == 0].shape[0]
offer_dropout_rate = (rejected_offers / total_candidates) * 100

high_risk_candidates = df[df['placement_score'] < df['placement_score'].median()].shape[0]
high_risk_percentage = (high_risk_candidates / total_candidates) * 100

# ---------------- Custom Style ---------------- #

st.markdown("""
    <style>
    .metric-card {
        background: linear-gradient(135deg, #1f77b4, #00c6ff);
        padding: 20px;
        border-radius: 15px;
        color: white;
        text-align: center;
        box-shadow: 2px 4px 10px rgba(0,0,0,0.2);
    }
    .metric-title {
        font-size: 18px;
    }
    .metric-value {
        font-size: 28px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🎯 Job Acceptance Prediction Dashboard")
st.markdown("### 📊 Key Performance Indicators")

# ---------------- KPI Layout ---------------- #

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">👥 Total Candidates</div>
        <div class="metric-value">{total_candidates}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">✅ Placement Rate</div>
        <div class="metric-value">{placement_rate:.2f}%</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">📉 Offer Dropout Rate</div>
        <div class="metric-value">{offer_dropout_rate:.2f}%</div>
    </div>
    """, unsafe_allow_html=True)

col4, col5, col6 = st.columns(3)

with col4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">🎤 Avg Interview Score</div>
        <div class="metric-value">{avg_interview_score:.2f}</div>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">🛠 Avg Skills Match</div>
        <div class="metric-value">{avg_skills_match:.2f}%</div>
    </div>
    """, unsafe_allow_html=True)

with col6:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">⚠ High Risk Candidates</div>
        <div class="metric-value">{high_risk_percentage:.2f}%</div>
    </div>
    """, unsafe_allow_html=True)