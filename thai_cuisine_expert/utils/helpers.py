import os
import traceback
from typing import Dict, Any, Optional

import streamlit as st


def setup_environment(api_key: str) -> None:

    if api_key:
        os.environ['OPENAI_API_KEY'] = api_key
        st.session_state['OPENAI_API_KEY'] = api_key


def display_error(error: Exception, show_details: bool = True) -> None:

    error_msg = f"Error: {str(error)}"
    st.error(error_msg)
    
    if show_details:
        with st.expander("Error details", expanded=False):
            st.error(f"{traceback.format_exc()}")


def validate_api_key(api_key: str) -> bool:

    if not api_key:
        st.warning("⚠️ Please enter your OpenAI API key to proceed. "
                  "Don't have one? Get it from: "
                  "https://platform.openai.com/settings/organization/api-keys")
        return False
    return True


def initialize_session_state() -> None:

    if "messages_history" not in st.session_state:
        print("messages_history not found in session state")
        st.session_state.messages_history = []
        
    if "agent" not in st.session_state:
        print("agent not found in session state")
        st.session_state.agent = None
        
    if "knowledge_loaded" not in st.session_state:
        print("knowledge_loaded not found in session state")
        st.session_state.knowledge_loaded = False