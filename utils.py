import streamlit as st
import uuid

# tag::write_message[]
def write_message(role, content, save = True):
    """
    This is a helper function that saves a message to the
     session state and then writes a message to the UI
    """
    # Append to session state
    if save:
        st.session_state.messages.append({"role": role, "content": content})

    # Write to UI
    with st.chat_message(role):
        st.markdown(content)
# end::write_message[]

#Create a get_session_id() function to retrieve the session ID from Streamlit
def get_session_id():
    """
    Get the session ID from Streamlit
    """
    # Ensure session state has a unique identifier
    if 'session_id' not in st.session_state:
        st.session_state.session_id = str(uuid.uuid4())

    return st.session_state.session_id



