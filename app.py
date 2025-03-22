import logging
import os
import traceback

import fitz  # PyMuPDF for PDF extraction
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
tavily_api_key = os.getenv("TAVILY_API_KEY")

# Initialize LangChain tools
llm = ChatGroq(model_name="gemma2-9b-it", api_key=groq_api_key)
search = TavilySearchResults(api_key=tavily_api_key)

# Create prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        MessagesPlaceholder(
            variable_name="chat_history"
        ),  # Maintain conversation history
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)

# Define agent & executor
tools = [search]
agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools)

# Initialize conversation history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Setup logging
logging.basicConfig(filename="error.log", level=logging.ERROR)


############################
# 🖥️ UI Enhancements
############################
col1, col2 = st.columns([7, 1])
with col1:
    st.title("🌍 Autonomous Web Agent")
    st.markdown("Llama 3.3 🔗 Web Search 🔗 AI-Powered Responses")
with col2:
    theme = st.selectbox("🎨 Theme:", ["Light", "Dark"])
    st.markdown(
        f"<style>body {{ background-color: {'#000' if theme == 'Dark' else '#fff'}; }}</style>",
        unsafe_allow_html=True,
    )

# File Upload Feature (PDF, CSV)
uploaded_file = st.file_uploader("📄 Upload a file (PDF/CSV)", type=["pdf", "csv"])
if uploaded_file:
    file_extension = uploaded_file.name.split(".")[-1]
    if file_extension == "pdf":
        pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        text = "\n".join(page.get_text() for page in pdf)
        st.text_area("Extracted Text", text)
    elif file_extension == "csv":
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)


############################
# 💬 Chat Interaction
############################
query = st.text_input("🔍 Enter your query:")

if query:
    # Append user query to chat history
    st.session_state.chat_history.append(("human", query))

    # Display user query
    with st.chat_message("user", avatar="👤"):
        st.markdown(query)

    # AI Processing & Response
    with st.chat_message("assistant", avatar="🤖"):
        response_placeholder = st.empty()
        full_response = ""

        try:
            for step in agent_executor.stream(
                {"input": query, "chat_history": st.session_state.chat_history}
            ):
                if "output" in step:
                    full_response += step["output"]
                    response_placeholder.markdown(full_response, unsafe_allow_html=True)
            # Append response to chat history
            st.session_state.chat_history.append(("ai", full_response))
        except Exception as e:
            logging.error(traceback.format_exc())
            st.error("⚠️ An error occurred. Please try again.")
