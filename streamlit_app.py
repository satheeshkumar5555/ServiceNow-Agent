import streamlit as st
from config import USERNAME, INSTANCE

from agent import ServiceNowAgent

if "agent" not in st.session_state:
    st.session_state.agent = ServiceNowAgent()

st.set_page_config(page_title="ServiceNow AI Assistant", page_icon="🤖", layout="wide")

# ---------------- Sidebar ----------------

with st.sidebar:
    st.title("🤖 AI Agent")

    st.divider()

    st.subheader("Connection Status")

    st.success("✅ Amazon Bedrock")
    st.success("✅ ServiceNow")

    st.divider()

    st.subheader("Supported Tools")

    st.write("✔ Create Incident")
    st.write("🚧 Get Incident")
    st.write("🚧 Update Incident")
    st.write("🚧 Resolve Incident")

    st.divider()

    st.caption("Built with Python + Amazon Bedrock + ServiceNow")

# ---------------- Main Page ----------------

# ---------------- Main Page ----------------

st.title("🤖 ServiceNow AI Assistant")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
if "bedrock_messages" not in st.session_state:
    st.session_state.bedrock_messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Type your message..."):

    # Show user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # Dummy assistant response
    with st.spinner("Thinking..."):
        response = st.session_state.agent.chat(
            prompt, st.session_state.bedrock_messages
        )

    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
        st.markdown(response)
