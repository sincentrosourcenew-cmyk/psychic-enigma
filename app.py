import streamlit as st
import time
import random

st.set_page_config(page_title="OMINIBOOKS", page_icon="📚")

# CSS
st.markdown("""
<style>
.stApp { background: #0a0a0f; color: #e8e8f0; }
h1 { color: #63b3ed !important; text-align: center; }
</style>
""", unsafe_allow_html=True)

# حالة الجلسة
if 'page' not in st.session_state:
    st.session_state.page = 'login'
    st.session_state.logged_in = False

# صفحة تسجيل الدخول
if st.session_state.page == 'login':
    st.markdown("<h1>أومنيبوكس</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;color:rgba(255,255,255,0.5);'>نوفر لك الوقت</p>", unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["تسجيل الدخول", "إنشاء حساب"])
    
    with tab1:
        email = st.text_input("البريد الإلكتروني")
        password = st.text_input("كلمة المرور", type="password")
        if st.button("دخول", use_container_width=True):
            st.session_state.logged_in = True
            st.session_state.page = 'dashboard'
            st.rerun()
    
    with tab2:
        st.text_input("الاسم")
        st.text_input("البريد")
        st.text_input("كلمة المرور", type="password")
        if st.button("إنشاء", use_container_width=True):
            st.success("تم!")

# لوحة التحكم
elif st.session_state.page == 'dashboard':
    st.markdown("<h1>أومنيبوكس</h1>", unsafe_allow_html=True)
    
    st.info("""
    ⚡ الوضع المتوازي
    
    • 64 فصل simultaneously
    • AMD MI300A · 2.197 ExaFLOPS
    • حتى 5,000 فصل
    """)
    
    if st.button("✦ إنشاء كتاب جديد", use_container_width=True, type="primary"):
        st.session_state.page = 'create'
        st.rerun()
    
    if st.button("تسجيل الخروج"):
        st.session_state.logged_in = False
        st.session_state.page = 'login'
        st.rerun()

# إنشاء كتاب
elif st.session_state.page == 'create':
    st.markdown("## إنشاء كتاب جديد")
    
    title = st.text_input("عنوان الكتاب")
    chapters = st.slider("عدد الفصول", 1, 10, 3)
    
    if st.button("← رجوع"):
        st.session_state.page = 'dashboard'
        st.rerun()
    
    if st.button("⚡ إنشاء الكتاب", type="primary"):
        with st.spinner("جارٍ التوليد..."):
            time.sleep(2)
        
        # توليد محتوى وهمي
        html = f"""<!DOCTYPE html>
<html dir="rtl">
<head><meta charset="UTF-8"><title>{title}</title></head>
<body style="font-family:Arial;max-width:600px;margin:40px auto;">
<h1>{title}</h1>
<p>بقلم المؤلف</p>
<hr>
"""
        for i in range(chapters):
            html += f"<h2>الفصل {i+1}</h2><p>" + " ".join([f"نص{random.randint(1,100)}" for _ in range(100)]) + "</p>"
        
        html += "</body></html>"
        
        st.success("تم!")
        st.download_button("📄 تحميل HTML", html, file_name=f"{title}.html")
        
        if st.button("العودة"):
            st.session_state.page = 'dashboard'
            st.rerun()
