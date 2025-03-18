import streamlit as st
import requests
import uuid  # To generate unique session IDs

# FastAPI backend URL
FASTAPI_URL = "http://ai_tutor_backend:8000/ask"


# Streamlit UI
st.set_page_config(page_title="AI Data Science Tutor", layout="wide")

st.title("🧠 AI Data Science Tutor")
st.write("Ask any question related to AI, Machine Learning, and Data Science.")

# Generate unique session ID
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())  # Unique per user session

# Initialize chat history in Streamlit session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    role, content = msg["role"], msg["content"]
    with st.chat_message(role):
        st.markdown(content)

# User input
user_input = st.chat_input("Type your question here...")

if user_input:
    # Display user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Send user input to FastAPI backend
    payload = {"user_input": user_input, "session_id": st.session_state.session_id}
    response = requests.post(FASTAPI_URL, json=payload)

    if response.status_code == 200:
        bot_reply = response.json()["response"]["content"]

        # Display AI response
        st.session_state.messages.append({"role": "ai", "content": bot_reply})
        with st.chat_message("ai"):
            st.markdown(bot_reply)
    else:
        st.error("Error communicating with FastAPI backend. Please try again.")
