
import os
from typing import Optional

import streamlit as st
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.embedder.openai import OpenAIEmbedder
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.lancedb import LanceDb, SearchType

from thai_cuisine_expert.config import Config


class CuisineAgent:
    
    def __init__(self, api_key: Optional[str] = None):
 
        self.config = Config()
        self.api_key = api_key
    
    def _get_api_key(self) -> str:

        return (
            self.api_key or 
            os.getenv('OPENAI_API_KEY') or 
            st.session_state.get('OPENAI_API_KEY', '')
        )

    def get_agent(self) -> Agent:

        api_key = self._get_api_key()
        
        return Agent(
            model=OpenAIChat(
                id=self.config.AGENT_MODEL, 
                api_key=api_key
            ),
            description=self.config.AGENT_DESCRIPTION,
            instructions=self.config.AGENT_INSTRUCTIONS,
            knowledge=self._setup_knowledge_base(api_key),
            tools=[DuckDuckGoTools()],
            show_tool_calls=True,
            markdown=True,
            # debug_mode=True
        )
    
    
    def _setup_knowledge_base(self, api_key: str) -> PDFUrlKnowledgeBase:

        return PDFUrlKnowledgeBase(
            urls=self.config.KNOWLEDGE_BASE_URL,
            vector_db=LanceDb(
                uri=self.config.VECTOR_DB_URI,
                table_name=self.config.VECTOR_DB_TABLE,
                search_type=SearchType.hybrid,
                embedder=OpenAIEmbedder(
                    id=self.config.EMBEDDER_MODEL,
                    api_key=api_key
                )
            )
        )