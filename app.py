import streamlit as st
from model import extract_skills

st.set_page_config(
    page_title="Job Skill Extractor",
    page_icon="🧠",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .title { text-align: center; color: #1a1a2e; font-size: 3em; font-weight: bold; }
    .subtitle { text-align: center; color: #16213e; font-size: 1.2em; margin-bottom: 30px; }
    .skill-badge {
        display: inline-block;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 6px 16px;
        border-radius: 20px;
        margin: 4px;
        font-size: 0.9em;
        font-weight: 500;
    }
    .tool-badge {
        display: inline-block;
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 6px 16px;
        border-radius: 20px;
        margin: 4px;
        font-size: 0.9em;
    }
    .soft-badge {
        display: inline-block;
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        color: white;
        padding: 6px 16px;
        border-radius: 20px;
        margin: 4px;
        font-size: 0.9em;
    }
    .info-card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        border-left: 5px solid #667eea;
    }
    .section-title {
        color: #1a1a2e;
        font-size: 1.3em;
        font-weight: bold;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<p class="title">🧠 Job Description Skill Extractor</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Powered by Groq LLM + LangChain | Innomatics Research Labs</p>', unsafe_allow_html=True)
st.divider()

# Input
jd_input = st.text_area("📋 Paste Job Description Here", height=200,
                         placeholder="Paste any job description here...")

col_btn1, col_btn2, col_btn3 = st.columns([2, 1, 2])
with col_btn2:
    extract_btn = st.button("🚀 Extract Skills", use_container_width=True)

if extract_btn:
    if jd_input.strip():
        with st.spinner("🔍 Analyzing Job Description..."):
            result = extract_skills(jd_input)

        st.success("✅ Extraction Complete!")
        st.divider()

        # Top info cards
        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown(f"""
                <div class="info-card">
                    <div class="section-title">🏷️ Job Title</div>
                    <div style="font-size:1.4em; color:#667eea; font-weight:bold;">
                        {result.get("job_title", "N/A")}
                    </div>
                </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
                <div class="info-card">
                    <div class="section-title">💼 Experience</div>
                    <div style="font-size:1.4em; color:#f5576c; font-weight:bold;">
                        {result.get("experience", "N/A")}
                    </div>
                </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
                <div class="info-card">
                    <div class="section-title">🎓 Education</div>
                    <div style="font-size:1em; color:#00f2fe; font-weight:bold;">
                        {result.get("education", "N/A")}
                    </div>
                </div>
            """, unsafe_allow_html=True)

        st.divider()

        # Skills section
        col4, col5, col6 = st.columns(3)

        with col4:
            st.markdown('<div class="section-title">🛠️ Required Skills</div>', unsafe_allow_html=True)
            badges = " ".join([f'<span class="skill-badge">✔ {s}</span>'
                               for s in result.get("required_skills", [])])
            st.markdown(badges, unsafe_allow_html=True)

        with col5:
            st.markdown('<div class="section-title">💻 Tools & Technologies</div>', unsafe_allow_html=True)
            badges = " ".join([f'<span class="tool-badge">🔧 {t}</span>'
                               for t in result.get("tools_technologies", [])])
            st.markdown(badges, unsafe_allow_html=True)

        with col6:
            st.markdown('<div class="section-title">🤝 Soft Skills</div>', unsafe_allow_html=True)
            badges = " ".join([f'<span class="soft-badge">💬 {s}</span>'
                               for s in result.get("soft_skills", [])])
            st.markdown(badges, unsafe_allow_html=True)

        st.divider()

        # Raw JSON
        with st.expander("📦 View Raw JSON Output"):
            st.json(result)

    else:
        st.warning("⚠️ Please paste a job description first.")