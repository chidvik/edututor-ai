import streamlit as st
import os
from datetime import date
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone, ServerlessSpec

# --- Initialize Pinecone ---
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

if not PINECONE_API_KEY:
    st.error("⚠️ Please set the PINECONE_API_KEY environment variable.")
    st.stop()

pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index("edututor-index")

# --- Load Sentence Transformer Model ---
model = SentenceTransformer("all-MiniLM-L6-v2")

# --- Streamlit App UI ---
st.set_page_config(page_title="EduTutor AI", page_icon="🎓", layout="wide")

st.title("🎓 EduTutor AI")
st.write("Empowering education with smart search and content delivery.")

username = st.text_input("Enter username (start with 'student' or 'educator')")

if username:
    if username.startswith("student"):
        st.success("Welcome, student!")

        tab1, tab2 = st.tabs(["📚 Course Notes", "📊 Assignments"])

        with tab1:
            st.header("Course Notes")
            query = st.text_input("Search notes")

            if st.button("Search"):
                if query:
                    vec = model.encode(query).tolist()
                    result = index.query(vector=vec, top_k=5, include_metadata=True)

                    if not result.matches:
                        st.warning("No relevant notes found.")
                    else:
                        for match in result.matches:
                            metadata = match.metadata
                            st.markdown(f"**{metadata.get('title')}** ({metadata.get('type')})")
                            st.caption(f"Score: {match.score:.4f}")
                            st.write("---")
                else:
                    st.warning("Please enter a query to search.")

        with tab2:
            st.header("Assignments")
            st.info("📋 Assignment list functionality can be integrated here (e.g., from a backend or classroom API).")

    elif username.startswith("educator"):
        st.success("Welcome, educator!")

        tab1, tab2 = st.tabs(["📝 Upload Notes", "🧠 Add Assignment"])

        with tab1:
            st.header("Upload Course Notes")
            note_title = st.text_input("Note Title")
            note_content = st.text_area("Note Content")
            note_type = st.selectbox("Note Type", ["lecture", "reference", "note"])

            if st.button("Upload Note"):
                if note_title and note_content:
                    vector = model.encode(note_content).tolist()

                    index.upsert([{
                        "id": f"{username}_{note_title}",
                        "values": vector,
                        "metadata": {
                            "title": note_title,
                            "type": note_type,
                            "uploader": username
                        }
                    }])
                    st.success("✅ Note uploaded to Pinecone!")
                else:
                    st.warning("⚠️ Please provide both title and content.")

        with tab2:
            st.header("Create Assignment")
            assignment_title = st.text_input("Assignment Title")
            assignment_desc = st.text_area("Description")
            due_date = st.date_input("Due Date", min_value=date.today())

            if st.button("Publish Assignment"):
                st.success(f"✅ Assignment '{assignment_title}' published successfully!")
    else:
        st.error("❌ Invalid username. Use 'student_xyz' or 'educator_abc'.")
