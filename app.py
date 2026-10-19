import os
import subprocess
import time
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Employee Handbook Assistant", layout="wide")

# تشغيل كودك الأصلي في الخلفية
@st.cache_resource
def run_main_script():
    # تم وضع اسم ملفك الجديد بدقة هنا
    process = subprocess.Popen(["python", "rag_pdf_qdrant_colab_(1).py"])
    time.sleep(12) # وقت انتظار لتحميل النموذج والواجهة
    return process

run_main_script()

# عرض واجهة Gradio داخل منصة Streamlit
components.iframe("http://localhost:7860", height=800, scrolling=True)
