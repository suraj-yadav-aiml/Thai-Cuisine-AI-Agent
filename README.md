# 🍜 Thai Cuisine Expert AI

An conversational agent specialized in authentic Thai cuisine, powered by Agno AI to provide expert knowledge about recipes, ingredients, techniques, and cultural context.

## Project Overview

Thai Cuisine Expert AI is an interactive application that combines AI language understanding with a specialized knowledge base of Thai recipes to help users explore and learn about authentic Thai cooking. The agent can answer questions about ingredients, recipes, cooking techniques, and the cultural significance of Thai dishes, providing a rich, educational experience for cooking enthusiasts, home chefs, and anyone interested in Thai cuisine.

### Key Features

- **AI-powered Thai cuisine expertise**: Access detailed knowledge about traditional Thai recipes, ingredients, and cooking methods
- **Web-enhanced information**: Supplements core knowledge with internet search capabilities
- **Intelligent conversations**: Ask questions in natural language about any aspect of Thai cuisine
- **Cultural context**: Learn about the historical and cultural significance of Thai dishes
- **Ingredient substitutions**: Get practical advice on finding or substituting traditional Thai ingredients
- **Structured recipe sharing**: Receive clear, well-organized recipes with ingredient lists and step-by-step instructions

## Technologies Used

- **Python**: Core programming language
- **Streamlit**: Web interface framework
- **Agno AI**: Agent framework for building conversational AI systems
- **OpenAI**: GPT models for natural language processing (gpt-4o-mini)
- **LanceDB**: Vector database for knowledge retrieval
- **DuckDuckGo Search**: Web search integration for supplemental information
- **PDF Knowledge Base**: Document storage for specialized Thai cuisine information

## Installation

### Prerequisites

- Python 3.7+
- OpenAI API key

### Installation Steps

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Thai-Cuisine-AI-Agent.git
cd Thai-Cuisine-AI-Agent
```

2. Create and activate a virtual environment (optional but recommended):
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Set up your OpenAI API key:
   - Create a `.env` file in the project root directory
   - Add your API key to the file:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```
   - Alternatively, you can enter your API key in the application sidebar when running the app

## Usage

### Running the Application

Start the Streamlit application:

```bash
python app.py
```

Or directly with Streamlit:

```bash
streamlit run thai_cuisine_expert/ui/streamlit_app.py
```

Once running, the application will be available at `http://localhost:8501` in your web browser.

### Using the Thai Cuisine Expert

1. Enter your OpenAI API key in the sidebar if not set through environment variables
2. Click "Load/Reload Knowledge Base" to initialize the AI agent's knowledge
3. Type your questions about Thai cuisine in the chat input
4. View the agent's responses, including any web searches or knowledge base lookups it performs

Example questions to ask:
- "What are the essential ingredients in Tom Yum soup?"
- "How do I make authentic Pad Thai at home?"
- "What's the cultural significance of Som Tam (papaya salad)?"
- "Can you suggest substitutes for galangal?"
- "What are the key flavor principles in Thai cooking?"

## Project Structure

```
📂 Thai-Cuisine-AI-Agent/
  📄 app.py                # Application entry point
  📄 requirements.txt      # Project dependencies
  📂 thai_cuisine_expert/  # Main package
    📄 __init__.py
    📄 agent.py            # Thai cuisine AI agent implementation
    📄 config.py           # Configuration settings
    📂 ui/
      📄 __init__.py
      📄 streamlit_app.py  # Streamlit interface implementation
      📄 tool_display.py   # UI components for tool visualization
    📂 utils/
      📄 __init__.py
      📄 helpers.py        # Utility functions
```

### Key Components

- **agent.py**: Defines the CuisineAgent class that initializes and configures the AI agent with specialized Thai cuisine knowledge
- **config.py**: Contains configuration parameters including model settings, knowledge base URLs, and agent instructions
- **streamlit_app.py**: Implements the web interface using Streamlit
- **tool_display.py**: Handles the visualization of tool calls (knowledge base searches, web searches)
- **helpers.py**: Provides utility functions for API key validation, error handling, and session state management

## License

This project is licensed under the MIT License

## Credits & Acknowledgments

- Thai cuisine knowledge base: [ThaiRecipes.pdf](https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf)
- Built with [Agno AI](https://github.com/agno-agi/agno) framework
- UI powered by [Streamlit](https://streamlit.io/)


## Resources

- [Agno AI Documentation](https://docs.agno.com/introduction)
- [Streamlit Documentation](https://docs.streamlit.io/)