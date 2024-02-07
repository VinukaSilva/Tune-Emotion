import streamlit as st
from rag_with_palm import RAGPaLMQuery
# Instantiate the class
rag_palm_query_instance = RAGPaLMQuery()

st.markdown(f"<h1 style='color:white;'>TuneEmotion Assistant 🎵🎭</h1>", unsafe_allow_html=True)
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
# React to user input
if prompt := st.chat_input("Need songs? Drop your question here!"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    response = rag_palm_query_instance.query_response(prompt)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})