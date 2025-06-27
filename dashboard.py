import streamlit as st

def student_dashboard(user_email):
    st.title("📚 Student Dashboard")
    st.write(f"Welcome, {user_email}!")
    st.success("Here you'll see your courses, notes, and assignments.")

def educator_dashboard(user_email):
    st.title("🧑‍🏫 Educator Dashboard")
    st.write(f"Welcome, {user_email}!")
    st.success("Here you can create, upload, and manage content.")

def show_dashboard(role, email):
    if role == "Student":
        student_dashboard(email)
    elif role == "Educator":
        educator_dashboard(email)
    else:
        st.error("Invalid role.")
