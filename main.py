import streamlit as st

def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []

def main():
    st.title("Simple Chat Application")
    
    # Initialize session state
    initialize_session_state()
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    # Chat input
    if prompt := st.chat_input("What's on your mind?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.write(prompt)
        
        # Add assistant response
        response = f"CivIA: {prompt}"  # Simple echo response for now
        st.session_state.messages.append({"role": "assistant", "content": response})
        
        # Display assistant response
        with st.chat_message("assistant"):
            st.write(response)

if __name__ == "__main__":
    main()
