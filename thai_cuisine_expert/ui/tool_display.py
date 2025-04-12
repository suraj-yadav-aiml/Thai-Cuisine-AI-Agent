import json
from typing import Any, Dict, List, Optional

import streamlit as st


class ToolDisplay:
    
    @staticmethod
    def extract_tool_calls(response: Any) -> List[Dict[str, Any]]:

        tool_calls = []
        
        if hasattr(response, 'tools') and response.tools:
            for tool in response.tools:
                tool_call = {
                    'name': tool.get('tool_name', ''),
                    'args': tool.get('tool_args', {}),
                    'result': tool.get('content', '')[:1000]  # Truncate long results
                }
                tool_calls.append(tool_call)
                
        return tool_calls

    @staticmethod
    def display_tool_calls(tool_calls: List[Dict[str, Any]]) -> None:

        if not tool_calls:
            return
            
        with st.expander("View tool calls"):
            for i, tool_call in enumerate(tool_calls,1):
                st.markdown(f"**Tool #{i}: {tool_call['name']}**")
                
                # Format arguments
                args = tool_call.get('args', {})
                if isinstance(args, dict):
                    args_str = json.dumps(args, indent=2)
                else:
                    args_str = str(args)
                
                st.code(f"Arguments: {args_str}", language="json")
                
                # Show truncated result preview
                result = tool_call.get('result', '')
                if isinstance(result, str) and len(result) > 300:
                    st.markdown(f"**Result:** (truncated)\n```\n{result[:300]}...\n```")
                else:
                    st.markdown(f"**Result:** \n```\n{result}\n```")