import streamlit as st
import google.generativeai as genai

# إعدادات الصفحة
st.set_page_config(page_title="SAPIENS-RED-TEAM", layout="wide")
st.title("🛡️ SAPIENS-RED-TEAM Ultimate Research Suite v2.0")

# إعداد الاتصال بـ Gemini
try:
    if "GOOGLE_API_KEY" not in st.secrets:
        st.error("⚠️ مفتاح API غير موجود في إعدادات Secrets!")
        st.stop()
        
    google_api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=google_api_key)
    
    # التعديل الجوهري: إضافة models/ قبل اسم الموديل
    model = genai.GenerativeModel('models/gemini-1.5-flash')
    
except Exception as e:
    st.error(f"⚠️ فشل في إعداد النظام: {e}")
    st.stop()

# التبويبات
tab1, tab2, tab3 = st.tabs(["📥 Upload & Dashboard", "🚀 Run New Campaign", "🧠 AI Analyst"])

with tab1:
    st.header("تحميل البيانات")
    uploaded_file = st.file_uploader("ارفع ملف CSV أو JSON", type=['csv', 'json'])
    if uploaded_file:
        st.success("تم تحميل الملف بنجاح!")

with tab2:
    st.header("بدء مهمة جديدة")
    campaign_goal = st.text_area("صف هدف المهمة:")
    if st.button("بدء التحليل"):
        if campaign_goal:
            try:
                # محاولة توليد المحتوى بالاسم الكامل للموديل
                response = model.generate_content(f"Analyze this target as a Red Team expert: {campaign_goal}")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"خطأ في التحليل: {e}")

with tab3:
    st.header("(Chat) المحلل الذكي")
    user_query = st.text_input("اسأل عن أي ثغرة أو كود:")
    if user_query:
        try:
            response = model.generate_content(user_query)
            st.markdown(response.text)
        except Exception as e:
            st.error(f"المحلل غير متاح: {e}")
