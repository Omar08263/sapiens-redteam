import streamlit as st
import google.generativeai as genai

# إعدادات الصفحة واللوجو
st.set_page_config(page_title="SAPIENS-RED-TEAM", layout="wide")
st.title("🛡️ SAPIENS-RED-TEAM Ultimate Research Suite v2.0")

# جلب المفتاح السري من الإعدادات
try:
    google_api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=google_api_key)
    model = genai.GenerativeModel('gemini-pro')
except:
    st.error("⚠️ خطأ: مفتاح GOOGLE_API_KEY غير موجود في Secrets!")
    st.stop()

# التبويبات (Tabs)
tab1, tab2, tab3 = st.tabs(["📥 Upload & Dashboard", "🚀 Run New Campaign", "🧠 AI Analyst"])

with tab1:
    st.header("تحميل البيانات")
    uploaded_file = st.file_uploader("ارفع ملف CSV أو JSON", type=['csv', 'json'])
    if uploaded_file:
        st.success("تم تحميل الملف بنجاح! جاهز للتحليل.")

with tab2:
    st.header("بدء مهمة جديدة")
    campaign_goal = st.text_area("صف هدف المهمة أو النطاق المستهدف:")
    if st.button("بدء التحليل"):
        if campaign_goal:
            response = model.generate_content(f"كخبير Red Teaming، حلل هذا الهدف: {campaign_goal}")
            st.markdown(response.text)

with tab3:
    st.header("المحلل الذكي (Chat)")
    user_query = st.text_input("اسأل الذكي الاصطناعي عن أي ثغرة أو كود:")
    if user_query:
        response = model.generate_content(user_query)
        st.write(response.text)
