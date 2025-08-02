import streamlit as st
import google.generativeai as genai

# ✅ Load external CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ✅ Call the function to load your CSS file
load_css("style.css")   # <-- Make sure style.css is in the same folder

# ✅ Set your Gemini API Key
genai.configure(api_key="AIzaSyCBwUrPUFjVmrEKamOFOKk2dsHbhfACm-E")  # Replace with your key

# ✅ Use a working model name
model = genai.GenerativeModel("gemini-1.5-flash")

# ✅ UI starts here
st.markdown("<h1 class='title'>📧 AI Email Tone Improver</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Rewrite your emails in a tone of your choice</p>", unsafe_allow_html=True)


email_text = st.text_area("✍️ Enter your email:")
tone = st.selectbox("🎯 Choose the tone:", ["Formal", "Friendly", "Concise", "Polite"])

if st.button("✨ Improve Email"):
    if email_text.strip():
        prompt = f"Rewrite the following email in a {tone} tone:\n\n{email_text}"
        with st.spinner("⏳ AI is rewriting your email..."):
            response = model.generate_content(prompt)
            improved_email = response.text
        
        # ✅ Show improved email with styling
        st.markdown("### ✅ Improved Email:")
        st.markdown(f"<div class='email-box'>{improved_email}</div>", unsafe_allow_html=True)
        
    else:
        st.warning("⚠️ Please enter an email first.")


