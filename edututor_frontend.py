import streamlit as st
from utils.session import get_user_role

st.set_page_config(page_title="EduTutor AI", layout="centered")

# Simulated login (just for testing)
st.title("🔐 EduTutor AI Login")
user_email = st.text_input("Enter your email")
role = st.selectbox("Select your role", ["student", "educator"])

if st.button("Login"):
    if user_email and role:
        st.session_state["user_email"] = user_email
        st.session_state["user_role"] = role
        st.success(f"Welcome, {role.title()} {user_email}!")
    else:
        st.error("Please enter your email and select a role.")

# Show dashboard after login
if "user_email" in st.session_state and "user_role" in st.session_state:
    st.write("---")
    st.header(f"{st.session_state['user_role'].title()} Dashboard")

    if st.session_state["user_role"] == "student":
        st.subheader("📚 Assignments")
        st.info("Assignments will be listed here.")

    elif st.session_state["user_role"] == "educator":
        st.subheader("📤 Upload Content")
        uploaded_file = st.file_uploader("Upload a note or document")
        if uploaded_file:
            st.success("File uploaded (processing not yet implemented)")

        st.subheader("📊 View Uploaded Materials")
        st.info("Uploaded materials will be displayed here.")
