import streamlit as st
import google.generativeai as genai

# 1. إعدادات المنصة الاحترافية
st.set_page_config(
    page_title="SAPIENS RED TEAM",
    page_icon="🛡️",
    layout="wide"
)

# تصميم الواجهة (CSS بسيط لتحسين الشكل)
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #ff4b4b; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ SAPIENS-RED-TEAM | Intelligence Suite v2.0")
st.subheader("Advanced Penetration Testing & AI Analysis")

# 2. ربط النظام بـ Gemini (الضمان القاتل للـ 404)
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    # استخدام الموديل الأحدث والأقوى
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("❌ Critical Error: System Configuration Missing")
    st.stop()

# 3. تنظيم الأدوات (Tabs)
tab1, tab2, tab3 = st.tabs(["📊 Dashboard", "🎯 Target Analysis", "🤖 AI Offensive Assistant"])

with tab1:
    st.header("Project Assets")
    uploaded_file = st.file_uploader("Upload Scanning Results (CSV/JSON)", type=['csv', 'json'])
    if uploaded_file:
        st.success("✅ Files Loaded Successfully. Ready for Analysis.")

with tab2:
    st.header("Tactical Target Analysis")
    target_info = st.text_area("Enter Target Domain, IP, or Scope:", placeholder="example.com or 192.168.1.1...")
    
    col1, col2 = st.columns(2)
    with col1:
        analyze_btn = st.button("Generate Attack Surface Report")
    with col2:
        vuln_btn = st.button("Identify Potential Vulnerabilities")

    if analyze_btn or vuln_btn:
        if target_info:
            with st.spinner("Analyzing..."):
                prompt = f"Act as a Senior Red Team Lead. Analyze this: {target_info}"
                if vuln_btn: prompt += " focusing on critical vulnerabilities and exploits."
                
                try:
                    response = model.generate_content(prompt)
                    st.markdown("### 📋 Expert Findings")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"Analysis Failed: {e}")
        else:
            st.warning("⚠️ Please provide target information.")

with tab3:
    st.header("AI Red Team Assistant")
    user_input = st.text_input("Ask about exploits, payloads, or methodology:")
    if user_input:
        with st.spinner("Consulting AI Intelligence..."):
            try:
                chat_res = model.generate_content(user_input)
                st.info("AI Recommendation:")
                st.markdown(chat_res.text)
            except Exception as e:
                st.error(f"Assistant Offline: {e}")

# تذييل الصفحة
st.markdown("---")
st.caption("Secure Intelligence Environment © 2026 SAPIENS RED TEAM")
