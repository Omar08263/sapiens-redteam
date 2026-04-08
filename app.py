import streamlit as st
import google.generativeai as genai

# إعداد واجهة المنصة
st.set_page_config(page_title="SAPIENS RED TEAM", layout="wide")

st.title("🛡️ SAPIENS-RED-TEAM Intelligence Suite")

# ربط الـ API Key
if "GOOGLE_API_KEY" not in st.secrets:
    st.error("❌ Missing GOOGLE_API_KEY in Secrets!")
    st.stop()

try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    # استخدام اسم الموديل المباشر
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"❌ Connection Error: {e}")
    st.stop()

# الأقسام
tabs = st.tabs(["📊 Dashboard", "🎯 Analysis", "🧠 AI Assistant"])

with tabs[0]:
    st.subheader("Assets")
    st.file_uploader("Upload Scanning Results", type=['csv', 'json'])

with tabs[1]:
    st.subheader("Tactical Target Analysis")
    target = st.text_input("Enter Target Info:")
    if st.button("Run Analysis"):
        if target:
            with st.spinner("Processing..."):
                try:
                    res = model.generate_content(f"Analyze this target: {target}")
                    st.markdown(res.text)
                except Exception as e:
                    st.error(f"Error: {e}")

with tabs[2]:
    st.subheader("AI Assistant")
    query = st.text_input("Ask AI:")
    if query:
        try:
            res = model.generate_content(query)
            st.markdown(res.text)
        except Exception as e:
            st.error(f"AI Offline: {e}")
