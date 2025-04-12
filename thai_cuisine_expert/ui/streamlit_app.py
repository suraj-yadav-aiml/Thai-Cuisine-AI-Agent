import streamlit as st

from thai_cuisine_expert.agent import CuisineAgent
from thai_cuisine_expert.config import Config
from thai_cuisine_expert.ui.tool_display import ToolDisplay
from thai_cuisine_expert.utils.helpers import (
    setup_environment,
    display_error,
    validate_api_key,
    initialize_session_state
)


def setup_page() -> None:
    config = Config()
    st.set_page_config(
        page_title=config.PAGE_TITLE,
        page_icon=config.PAGE_ICON,
        layout=config.LAYOUT
    )


def render_sidebar() -> str:

    with st.sidebar:
        st.header("About")
        st.markdown("""
        This app uses AI to provide expert information about Thai cuisine. 
        It has access to a knowledge base of Thai recipes and can search the web 
        for additional information.
        """)
        
        api_key = st.text_input(label="Enter OpenAI API Key", type="password")
        setup_environment(api_key)
        validate_api_key(api_key)
        

        st.header("Knowledge Base")
        if st.button("Load/Reload Knowledge Base"):
            load_knowledge_base(api_key)
            
        if st.button("Clear Chat"):
            st.session_state.messages_history = []
            st.rerun()
        
        # Footer
        st.markdown("---")
        st.markdown("Powered by Agno AI and Streamlit")
        

def load_knowledge_base(api_key: str) -> None:

    with st.spinner("Loading knowledge base... This might take a minute..."):
        try:

            cuisine_agent = CuisineAgent(api_key=api_key).get_agent()

            if cuisine_agent.knowledge is not None:
                cuisine_agent.knowledge.load()
            
            st.session_state.agent = cuisine_agent
            st.session_state.knowledge_loaded = True
            st.success("Knowledge base loaded successfully!")
        
        except Exception as e:
            display_error(e)


def render_chat_history() -> None:
    for message in st.session_state.messages_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

            # Display tool calls if present
            if "tool_calls" in message and message["tool_calls"]:
                ToolDisplay.display_tool_calls(message["tool_calls"])


def process_user_query(query: str) -> None:

    if not st.session_state.knowledge_loaded:
        st.warning("Please load the knowledge base first from the sidebar.")
        return
        
    st.session_state.messages_history.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)

    with st.chat_message("assistant"):
        thinking_placeholder = st.empty()
        thinking_placeholder.markdown("🧠 Thinking...")
        with st.spinner(text="",show_time=True):
            try:
                response = st.session_state.agent.run(query)

                tool_calls = ToolDisplay.extract_tool_calls(response)
                
                thinking_placeholder.empty()
                st.markdown(response.content)

                if tool_calls:
                    ToolDisplay.display_tool_calls(tool_calls)
                
                st.session_state.messages_history.append({
                    "role": "assistant", 
                    "content": response.content,
                    "tool_calls": tool_calls
                })
        
            except Exception as e:
                thinking_placeholder.empty()
                display_error(e)
                st.session_state.messages_history.append({
                    "role": "assistant", 
                    "content": f"⚠️ Error: {str(e)}"
                })


def run_app() -> None:

    setup_page()
    initialize_session_state()
    
    st.title("🍜 Thai Cuisine Expert")
    st.markdown("Ask anything about Thai recipes, cooking techniques, or the history of Thai cuisine!")
    
    render_sidebar()
    
    render_chat_history()
    
    if user_query := st.chat_input("Ask about Thai cuisine..."):
        process_user_query(user_query)
