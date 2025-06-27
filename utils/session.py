import streamlit as st

def get_user_role():
    return st.session_state.get("user_role", None)
