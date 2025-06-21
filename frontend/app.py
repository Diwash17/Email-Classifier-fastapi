import streamlit as st
import requests

# FastAPI URL
API_URL = "http://localhost:8000/predict"  # Change if deployed

# Streamlit UI
st.set_page_config(page_title="Email Spam Classifier", layout="centered")
st.title("📧 Email Spam Classifier")
st.markdown("Type an email message and we'll tell you if it's **Spam** or **Not Spam**.")

# Input
email_text = st.text_area("Email Text", height=200)

if st.button("Classify"):
    if not email_text.strip():
        st.warning("Please enter an email message.")
    else:
        try:
            with st.spinner("Classifying..."):
                response = requests.post(API_URL, json={"text": email_text})
                result = response.json()
                
                label = result.get("label", "unknown").lower()

                if label == "spam":
                    st.error("🚨 This email is **SPAM**!")
                elif label == "ham":
                    st.success("✅ This email is **NOT SPAM**.")
                else:
                    st.warning("⚠️ Unable to classify the email.")
        except Exception as e:
            st.exception(f"API error: {e}")